#Problem 1
#1)
stkmon <- read.csv("/Users/liuxuyang/Desktop/BU\ FALL\ 2021/MF793/TakeHome/stk-11-mon-2010-2017\ .csv",header=T)
stkday <- read.csv("/Users/liuxuyang/Desktop/BU\ FALL\ 2021/MF793/TakeHome/stk-11-day-2010-2017\ .csv",header=T)

logmonret <- cbind(stkmon[1],log(1+stkmon[2]),log(1+stkmon[5]),log(1+stkmon[8]),log(1+stkmon[,12:13]))
logdayret <- cbind(stkday[1],log(1+stkday[2]),log(1+stkday[5]),log(1+stkday[8]),log(1+stkday[,12:13]))
logmonret <- logmonret[logmonret$date>="20120101" & logmonret$date<="20161231",]
logdayret <- logdayret[logdayret$date>="20120101" & logdayret$date<="20161231",]

sdday <- apply(logdayret[,2:6],2,sd)
sdday <- sdday * sqrt(252)
sdmon <- apply(logmonret[,2:6],2,sd)
sdmon <- sdmon * sqrt(12)
mu0sdday <- apply(logdayret[,2:6]^2,2,mean)
mu0sdday <- sqrt(mu0sdday) * sqrt(252)
mu0sdmon <- apply(logmonret[,2:6]^2,2,mean)
mu0sdmon <- sqrt(mu0sdmon) * sqrt(12)


#Problem 2
library(forecast)
library(tseries)
#3)
vix <- read.csv("/Users/liuxuyang/Desktop/BU\ FALL\ 2021/MF793/TakeHome/vix2021-mon.csv",header=T)
vv <- vix[vix$date >="201201" & vix$date <="202112",][,2]
vv <- ts(vv,frequency=12,start=c(2012,1))
ts.plot(vv,ylab="VIX",xlab="Time")

par(mfrow=c(2,1),mar=c(2.5,2.5,2,1),mgp=c(1.5,0.5,0))
acf(vv);title("ACF of VIX")
acf(vv,type="partial");title("PACF of VIX")

#5)
vvar <- arma(vv, order=c(1,0))
summary(vvar)
vvres <- abs(residuals(vvar)[2:length(residuals(vvar))])
par(mfrow=c(1,1))
plot(vv[1:length(vv)-1],vvres,main="Abs(residuals) vs explanatory variable")

#8)
qqnorm(vvres,main="Normal Q-Q Plot for Residuals")
qqline(vvres)
Kurt <- mean(((vvres-mean(vvres))/sd(vvres))^4) 
Kurt

#9)
par(mfrow=c(1,2))
qqnorm(vv,main="Normal ProbPlot of VIX")
qqnorm(log(vv),main="Normal Prob Plot of log(VIX)")

#11)
logvvar <- arma(log(vv), order=c(1,0))
logvvres <- abs(residuals(logvvar)[2:length(residuals(logvvar))])
par(mfrow=c(1,1))
plot(log(vv[1:length(vv)-1]),logvvres,main="Abs(residuals) vs explanatory variable")



#Problem 3
library(zoo)
#1)
spret <- read.csv("/Users/liuxuyang/Desktop/BU\ FALL\ 2021/MF793/TakeHome/spret-day-2020.csv",header=T)
spret <- spret[spret$caldt >= "20180101",]
winlen <- 63
dates = as.character(spret[(63:length(spret[,c(1)])), c(1)])
dates = as.Date(dates, "%Y%m%d")
#RW
sdr <- rollapply(spret[2]^2,winlen,mean)# use mean = 0 method
sdr1 <- sqrt(sdr * 252)
#RM
lamda <- 0.95
rm <- spret[63:length(spret[,2]),2]
rm[1] <- (1-lamda) * sdr[1]^2

for (i in 2:length(rm)){
  rm[i]= (lamda * rm[i-1] + (1-lamda) * rm[i]^2)
}
sdr2 <- sqrt(rm * 252)
# construct the dataframe
df = data.frame(dates, sdr1, sdr2)
df1 = df[df[,c(1)]>as.Date("2019-01-01"),]


par(mfrow=c(2,1),mar=c(2.5,2.5,2,1),mgp=c(1.5,0.5,0))
plot(df1[,1], df1[,3], type='l',col='red',ylab='Std',xlab='Time')
lines(df1[,1], df1[,2], col='blue')
title("Figure 1:Annual Std BY RW and RM")
legend("topright",c("RW","RM, lambda=0.95"), col=c("blue", "red"), lwd=1,bty="n")
#ts.plot(ts(sdr1,frequency=252,start=c(2018,01,02)),ts(sdr2,frequency=252,start=c(2018,01,02)),col=c("blue","red"),xlab="Date",ylab="Std",main="Annual Std By RW and RM")

#2,3) label the points



#4) the other way
spret2 <- spret[spret$caldt >= "20190101" & spret$caldt <= "20190331",]
df2 <- df[df[,c(1)]>as.Date("2019-01-01") & df[,c(1)]<=as.Date("2019-03-31"),]

#old RM
oldrm <- spret[,2]
oldrm[1] <- df2[1,3]^2 / 252

for (i in 2:length(oldrm)){
  oldrm[i]= (lamda * oldrm[i-1] + (1-lamda) * oldrm[i+winlen]^2)
}
sdr3 <- sqrt(oldrm * 252)

# New RM
newrm <- spret[,2]
newrm[1] <-  df2[1,2]^2 / 252

for (i in 2:length(newrm)){
  newrm[i]= (lamda * newrm[i-1] + (1-lamda) * newrm[i+winlen]^2)
}
sdr4 <- sqrt(newrm * 252)


plot(df2[,1], sdr3[1:61], type='l',col='blue',ylab='Std',xlab='Time')
lines(df2[,1], sdr4[1:61], type='l',col='red')
#ts.plot(ts(sdr2[190:250],frequency=252,start=c(2019,1,2)),ts(sdr3[1:61],frequency=252,start=c(2019,1,2)),col=c("blue","red"),xlab="Date",ylab="Std",main="Two Version of RM")
legend("topright",c("Old RM","New RM"), col=c("blue", "red"), lwd=1,bty="n")
title("Figure 2:Different Initialization Method")





















