library(zoo)

winlen<- 50
mu  <- 0.1 
sig <- 0.15 
simr<-rnorm(200,mu/252,sig/sqrt(252))	# Simulated daily Data
#
# Put an outlier
#
simr[100]<- -6*sig/sqrt(252)				# An Outlier

# RW estimator
sdvec<-rollapply(simr,winlen,sd) 	# Need Zoo for rollapply

#
par(mfrow=c(2,1),mar=c(2.5,2.5,0.5,1),mgp=c(1.5,0.5,0))
ts.plot(simr[winlen:200],ylab="Daily Return",xlab="")

ts.plot(sdvec*sqrt(252),ylab="RW Standard Deviation",xlab="Day",ylim=c(0.1,0.30)) 
abline(h=sig)
mtext(side=1,line=-1,"Window length: 50") 


lam<-0.94
rm <-rep(0,151);rm[1]<-0.5*sdvec[1]^2
for(i in 51:200){rm[i-49]<-lam*rm[i-50]+(1-lam)*simr[i]^2}
rm<-sqrt(rm)
lines(rm*sqrt(252),col="green")

# Regime Shift

winlen <- 50
mu <- 0.1
sig<- 0.15

simrr<- rnorm(200,mu/252,sig/sqrt(252))	# Simulated Daily data
simrr[101:200]<- 3*simrr[101:200]		# New regime
sdvec<-rollapply(simrr,winlen,sd) 

#
par(mfrow=c(2,1),mar=c(3,3,0.5,1),mgp=c(1.8,0.75,0))
ts.plot(simrr[50:200],ylab="Return",xlab="")
mtext(side=3,line=-1,"Daily Returns, Regime Shift at T=51")
ts.plot(sdvec*sqrt(252),ylab="Ann. Std. Deviation", xlab="Day", 
        ylim=range(c(sdvec*sqrt(252),0.1,0.5)))
mtext(side=1,line=-1,"50 day Rolling Window",cex=1.2) 
#
segments(1,0.15,50,col="blue",lw=2)
segments(51,0.45,150,col="blue",lw=2)

lam<-0.95
rm <-rep(0,151);rm[1]<-sdvec[1]^2
for(i in 51:200){rm[i-49]<-lam*rm[i-50]+(1-lam)*simrr[i]^2}
rm<-sqrt(rm)
lines(rm*sqrt(252),col="green")


##################################
# Spurious memory of RW estimators
#

winlen<- 20
mu  <- 0.1 
sig <- 0.15 
simr<-rnorm(2500,mu/252,sig/sqrt(252))	# Simulated daily Data

# RW estimator

sdvec<-rollapply(simr,winlen,sd) 			# Need Zoo for rollapply
acf(sdvec)

sdvec<-rollapply(simr,winlen,sd,by=20) 	# Non-overlapping RW
acf(sdvec)


# REALIZED VOLATILITY /  BlOCK SAMPLING 

# Construct 10 years of hourly log returns
# 		21 days/month , 24 hours/day for simplicity
# Construct corresponding daily returns.
# Compute monthly block sampling estimates of monthly vol 
# 			from daily and hourly returns

# Simulate hourly returns, make daily returns
# 	Use Package zoo for "rollapply" command

rethour <-rnorm(10*12*21*24,0.1/(252*24),0.2/sqrt(252*24)) # hourly return
retday  <-rollapply(rethour,width=24,sum,by=24)

# Two ways to create the block sampling estimate
# 1) apply command
# 	 make matrix with every month in a column
# 	 use apply per column to get monthly vol. estimate

rethour.mat <- matrix(rethour,ncol=10*12) 
# every month in a column
sdhour 		<- apply(rethour.mat,2,sd)*sqrt(24*252)  
# monthly sd from hourly returns

retday.mat <- matrix(retday,ncol=10*12)	# every month in a column
sdday  	   <- apply(retday.mat,2,sd)*sqrt(252) 
# monthly sd from daily rets

# 2) Or use rollapply directly on the vector data:
library(zoo)
rollsdhour<-rollapply(rethour,width=21*24,sd,by=21*24)*sqrt(24*252)
rollsdday <-rollapply(retday, width=21,   sd,by=21)*sqrt(252)

#
# Check the practical gain in precision from using higher
# frequency data in the block sampler
#

ts.plot(cbind(rollsdhour,rollsdday),lty=c(1,1),lwd=c(2,2),col=c("blue","red"),xlab="Month", ylab="Annualized Std. Deviation")
title(line=-2,"Monthly std. dev. from daily and hourly returns \n  true std. dev.: 0.20",cex=1)


#######################################################
#
# mu/sig -> 0 as sampling interval ->0
# Can we ignore the mean to estimate the variance?
# Yes we can !

sdzeroday<- sqrt(rollapply(retday^2,width=21,sum,by=21)*12)
sdzerohr<- sqrt(rollapply(rethour^2,width=21*24,sum,by=21*24)*12)

ts.plot(cbind(rollsdhour,sdzerohr),lty=c(1,1),col=c("blue","red"),xlab="month", 
        ylab="Annualized Std. Deviation",lwd=c(1,2))
mtext(side=3,line=-1,"Std. Dev. from hourly returns, with / without mean",cex=1.2)
legend("bottomleft",c("mean","zero mean"),lty=c(1,2),col=c("blue","red"))



