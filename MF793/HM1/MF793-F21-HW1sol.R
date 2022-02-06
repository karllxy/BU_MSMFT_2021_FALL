#
# HOMEWORK 1
#
# PROBLEM 1

Overflows !!
choose(171,5)		# OK
factorial(365)		# poof	factorial(171) overflows
factorial(365-166+1)# bim
prod((365-165):360)	# bam
365^171				# boom	365^121 overflows

logprob<-log(choose(171,5))+lfactorial(36^)-lfactorial(36^-165) -171*log(365)
exp(logprob)

Question d) with the log approach:

round(1-exp(lfactorial(365)-lfactorial(365-171+1)-171*log(365)),12)

#
# PROBLEM 2
#
retmat<-read.csv("FF-Factors-week.csv",header=T)
names(retmat)
range(retmat[,1])

# The time series command is useful to know. It creates a date variable. 
# But it works only for a regular frequency, not for weekly data.
# For example, for monthly data from July 1926
# tsret<-ts(retmat[,2],frequency=12,start=c(1926,7))
# Then we can do a nice ts plot ts.plot(tsret)

rets<-retmat[ retmat[,1]>20120000 & retmat[,1]<20210000, ]

# Compare weekly stock returns to risk-free rate
apply(rets[2:5],2,mean)*52	

zrets<-rets[,2]+rets[,5]
xrets<-rets[,2]
length(xrets)
length(xrets[xrets>0])
sum(xrets>0)		# does the same

# unconditional p(Rm-Rf>0)  62%	!
length(xrets[xrets>0])/length(xrets)
sum(xrets>0)/length(xrets)


# conditional p(Rt > 0 | Rt-1 > 0)

pair<-cbind(xrets[1:469],xrets[2:470]) 
# Of course we "lose" week 1 
# and we will ignore weeks 123 and 124 with 0 return

count<-matrix(0,ncol=2,nrow=2)
# positive return second week
count[2,2]<-length(pair[pair[,1]>0 & pair[,2]>0,1])  
count[1,2]<-length(pair[pair[,1]<0 & pair[,2]>0,1])  

# negative return second week
count[1,1]<-length(pair[pair[,1]<0&pair[,2]<0,1])  
count[2,1]<-length(pair[pair[,1]>0&pair[,2]<0,1])  

count
jprob <- count/sum(count);jprob
cprob <- jprob*0

cprob[1,]<- jprob[1,]/sum(jprob[1,])
cprob[2,]<- jprob[2,]/sum(jprob[2,])
cprob

# d) success of the conditional rule
# P(C) = p(C|Rt-1>0) p(Rt-1>0) + p(C|Rt-1<0) p(Rt-1<0) 
cprob[2,2]* (290/467) + cprob[1,1]*(177/467)		# Why 467?

#
# PROBLEM 4
#

# Get and Prepare Data

fundret<- read.csv("funds-1288g-mon.csv",header=T)    
facmon <- read.csv("FF-Factors-mon.csv",header=T)
facmon <-facmon[facmon[,1]>201000&facmon[,1]<202107,]

rmret<-(facmon[,2]+facmon[,5])/100 	
	# add back the Tbill, scale Rm to match fund returns

dim(fundret);dim(facmon)
cbind(fundret[,2],facmon[,1]) # check Dates are lined up!

#
# Question a)
#
murm <-mean(rmret)
murm1<-mean(rmret[43:90])  	# 2013/7 - 2017/6
murm2<-mean(rmret[91:138]) 	# 2017/7 - 2021/6 

mufu1<-apply(fundret[43:90,3:1290],2,mean)
mufu2<-apply(fundret[91:138,3:1290],2,mean)

par(mgp=c(1.5,0.5,0),mar=c(2.5,2.5,1.5,0.2)) # What does this do? Look it up.
hist(mufu1*12,xlab="Annualized Mean Return",freq=T,
nclass=100,main="")
title("Figure 1a: Histogram, 1288 growth fund returns, 2013/7-17/6",line=0.2)
box()
abline(v=mean(mufu1)*12,col="red",lwd=2)
abline(v=murm1*12,col="blue",lwd=2)
legend("topleft",c("Avg. Fund","Market"),bty="n",
col=c("red","blue"),lwd=c(1,2),lty=1)

# Let's remove the crazy loser funds to see better

par(mgp=c(1.5,0.5,0),mar=c(2.5,2.5,2.5,0.2))
hist(mufu1[mufu1>0]*12,xlab="Mean Return",freq=T,nclass=100,main="")
title("Figure 1b: Histogram, 1288 growth fund returns, 2013/7-2017/6 \n Negative return funds removed",line=0.2)
box()
abline(v=mean(mufu1[mufu1>0])*12,col="red",lwd=2)
abline(v=murm1*12,col="blue",lwd=2)
legend("topleft",c("Avg. Fund","Market"),bty="n",
col=c("red","blue"),lwd=c(1,2),lty=1)


murm1*12						# Mean market return 
quantile(mufu1)*12
length(mufu1[mufu1>murm1])/1288	# 0.31
murm1*12-median(mufu1)*12		# Why the median?

#
# Question b)
# Persistence
#

axisrange<-range(c(mufu1,mufu2))*12		# total range of mean returns
par(mgp=c(1.5,0.5,0),mar=c(2.5,2.5,1.5,0.2))			plot(mufu1*12,mufu2*12,xlab="13/7-17/6 Mean Return",ylab="17/7-21/6 Mean Return", xlim=axisrange, ylim=axisrange,col="gray")		# Same range on x and y
title("Figure 2: 1288 Fund, second vs first period returns",line=0.2)
abline(lsfit(mufu1*12,mufu2*12),lty=3,lwd=1,col="gray")
points(murm1*12,murm2*12,pch="M")
abline(h=murm2*12,lty=2);abline(v=murm1*12,lty=2)


# Removing crazy funds from period 1

axisrange<-range(c(mufu1[mufu1>0],mufu2[mufu1>0]))*12	# range of >0 mean returns
par(mgp=c(1.5,0.5,0),mar=c(2.5,2.5,1.5,0.2))	plot(mufu1[mufu1>0]*12,mufu2[mufu1>0]*12,xlab="13/7-17/6 Mean Return",ylab="17/7-21/6 Mean Return", xlim=axisrange,ylim=axisrange,col="gray")		# Have the same range on x and y
title("Figure 2b: 1288 Fund, second vs first period returns",line=0.2)
abline(lsfit(mufu1[mufu1>0]*12,mufu2[mufu2>0]*12),lty=3,col="gray")
points(murm1*12,murm2*12,pch="M")
abline(h=murm2*12,lty=2);abline(v=murm1*12,lty=2)

# The ranks plot of persistence
# With not performance, funds should be randomly scattered on the square.
rank1<-rank(mufu1)			# See what rank does
rank2<-rank(mufu2)
plot(rank1,rank2,xlab="Period 1 rank",ylab="Period 2 rank")
title("Figure 2c: Funds rank persistence, Period 1 to Period 2",line=0.5)
abline(lsfit(rank1,rank2))

# Two-way counts cutoffs

brs<-cbind(quantile(mufu1,c(0.15,0.85)),quantile(mufu2,c(0.15,0.85))) 
brs*12*100
0.15*1288=193	0.7*1288=902

# many ways to do this, can just count:
cmat<-matrix(0,ncol=3,nrow=3)
cmat[1,1]<-length(mufu1[mufu1<brs[1,1]&mufu2<brs[1,2]])	# Lose Lose
cmat[1,3]<-length(mufu1[mufu1<brs[1,1]&mufu2>brs[2,2]])	# Lose Win
cmat[1,2]<-193-cmat[1,1]-cmat[1,3] 			# Lose Middle, why 193?		

cmat[3,1]<-length(mufu1[mufu1>brs[2,1]&mufu2<brs[1,2]])
cmat[3,3]<-length(mufu1[mufu1>brs[2,1]&mufu2>brs[2,2]])
cmat[3,2]<-193-cmat[3,1]-cmat[3,3]

for (i in c(1:3)){cmat[2,i]<-193-cmat[1,i]-cmat[3,i]}	# middle row
cmat[2,2]<-1288-2*193-cmat[1,2]-cmat[3,2]

# Check what you did !
rowSums(cmat)
colSums(cmat)
sum(cmat)

# The joint prob. table is easy!
probmat<-cmat/1288
round(probmat,2)
sum(probmat)	# check it makes sense

# So is the conditional table

prob1  <- c(0.15,0.7,0.15) # or
prob1  <- rowSums(probmat)
condmat<- probmat/prob1	# What does this do? R recycles the shorter
round(condmat,2)	
rowSums(condmat)		# check it makes sense:

# question c)
# Compare to market

xmufu1 <- mufu1-murm1
xmufu2 <- mufu2-murm2
length(xmufu1[xmufu1>0])/1288
length(xmufu2[xmufu2>0])/1288	# Funds did better as a group in period 2
								# Still worse than random
# Also this way:

beat1<- xmufu1>0	# make indicator variable based on logical expression
beat2<- xmufu2>0
					# Then just make products to get joint counts
					
beatct<-matrix(			# Careful, R fills in matrices by column
c( sum((1-beat1)*(1-beat2)) , sum(beat1 * (1-beat2)) ,
sum((1-beat1)*beat2 ) , sum(beat1*beat2) ) 
,ncol=2)
beatct

beatprob<-beatct / 1288
round(beatprob,2)

prob1 <- c(1288-sum(beat1),sum(beat1))/1288
beatcond<-beatprob/prob1
beatcond

# What is the no-persistence hypothesis
# Unconditional probability of beating the
# market in each period

hist((mufu2-mufu1)*12,nclass=100,xlab="R2-R1");box()
sum((mufu2-mufu1)>0)/1288

prob2 <- c(1288-sum(beat2),sum(beat2))/1288
prob2


#
# Problem 5: Utility
#
# a)

-1/(0.5*(-1/13000)+0.5*(-1/9000))

# b)c)
# 0.9*(10000+B)-B must be ≥0

Bmax<- 90000

BB<- seq(0,Bmax,length=8000)
EW<- 0.5*((10000+BB)*1.3)+0.5*((10000+BB)*0.9)-BB
SD<- sqrt(0.5*((10000+BB)*1.3-BB-EW)^2
         +0.5*((10000+BB)*0.9-BB-EW)^2 )

CE <- -1/(-0.5/((10000+BB)*1.3-BB)-0.5/((10000+BB)*0.9-BB))
BB[CE==max(CE)]			# Borrowing at which CE is maximized


# improve R plots aspect ratios and use of space
par(mgp=c(1.5,0.5,0),mar=c(2.5,2.5,2,0.2))
plot(BB/1000,EW/1000,type="l",xlab="$1,000 Borrowed",ylab="Value in $1,000", ylim=c(8,16),xlim=c(0,60))

# Extra lines and points

lines(BB/1000,CE/1000,col="blue")
points(BB[CE==max(CE)]/1000,max(CE)/1000,pch="o",col="blue",font=2)


# Need to know how to add a legend box

legend("topleft",
c("E(W)","EU, G=2 Power Utility"),
col=c("black","blue"),lty=c(1,1),bty="n")
title("Figure 3 & 4: CE and EW vs Borrowing in $1,000s",line=0.2)

# Use abline or segments to show interesting features
segments(BB[CE==max(CE)]/1000,8,BB[CE==max(CE)]/1000,max(CE)/1000,lty=2,lwd=1,col="purple")

