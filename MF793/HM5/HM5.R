# Problem 1
# a)
monthret <- read.csv("/Users/liuxuyang/Desktop/BU\ FALL\ 2021/MF793/HM5/stk-mon-2019.csv",header=T)
dailyret <- read.csv("/Users/liuxuyang/Desktop/BU\ FALL\ 2021/MF793/HM5/stk-day-2019.csv",header=T)

logmonret <- cbind(monthret[1],log(1 + monthret[,2:7]))
logmonret1 <- logmonret[logmonret$date<="20160630"&logmonret$date>="20120101",]
logmonret2 <- logmonret[logmonret$date<="20191231"&logmonret$date>="20160701",]
length(logmonret1[,1])#54
length(logmonret2[,1])#42
# the distribution : F(v1=53,v2=41)
cutoff <- qf(c(0.05,0.95),41,53)
cutoff


# b)
#compute USVW
ff<- read.csv("/Users/liuxuyang/Desktop/BU\ FALL\ 2021/MF793/HM5/FF-Factors-day.csv",header=T)
ffm <-read.csv("/Users/liuxuyang/Desktop/BU\ FALL\ 2021/MF793/HM5/FF-Factors-mon.csv",header=T)
mkt <- cbind(ff[1],log(1+(ff[2]+ff[5])/100))
mkt1 <- mkt[mkt$X<="20160630"&mkt$X>="20120101",][,2]
mkt2 <- mkt[mkt$X<="20191231"&mkt$X>="20160701",][,2]
mkt1sd <- sd(mkt1)*sqrt(252)
mkt2sd <- sd(mkt2)*sqrt(252)
(mkt2sd/mkt1sd)^2

mktm <- cbind(ffm[1],log(1+(ffm[2]+ffm[5])/100))
mktm1 <- mktm[mktm$X<="20160630"&mktm$X>="20120101",][,2]
mktm2 <- mktm[mktm$X<="20191231"&mktm$X>="20160701",][,2]
mktm1sd <- sd(mktm1)*sqrt(12)
mktm2sd <- sd(mktm2)*sqrt(12)
(mkt2sd/mkt1sd)^2


#compute stocks
sd1 <- apply(logmonret1[,2:7],2,sd)
sd2 <- apply(logmonret2[,2:7],2,sd)
annsd1 <- sd1 * sqrt(12)
annsd2 <- sd2 * sqrt(12)
(annsd2/annsd1)^2
mean((annsd2/annsd1)^2)
# then compute the daily data
logdayret <- cbind(dailyret[1],log(1 + dailyret[,2:7]))
logdayret1 <- logdayret[logdayret$date<="20160630"&logdayret$date>="20120101",]
logdayret2 <- logdayret[logdayret$date<="20191231"&logdayret$date>="20160701",]
sdd1 <- apply(logdayret1[,2:7],2,sd)
sdd2 <- apply(logdayret2[,2:7],2,sd)
annsdd1 <- sdd1 * sqrt(252)
annsdd2 <- sdd2 * sqrt(252)
(annsdd2/annsdd1)^2
mean((annsdd2/annsdd1)^2)


# c
length(logdayret1[,1])#1131
length(logdayret2[,1])#881
# the distribution : F(880,1130)
cutoff2 <- qf(c(0.025,0.975),880,1130)
cutoff2


# d)
#row1 (normal)
number <- length(logdayret1[,1]) + length(logdayret2[,1])
simday <- matrix(rnorm(number*20000,mean=0,sd=1),ncol=20000)
simday1 <- simday[1:1131,]
simday2 <- simday[1132:2012,]
simsd1 <- apply(simday1,2,sd)
simsd2 <- apply(simday2,2,sd)
simvr <- (simsd2/simsd1)^2
c(quantile(simvr,0.025),quantile(simvr,0.975))
rej1 <- (length(simvr[simvr > qf(0.975,880,1130)])  + length(simvr[simvr < qf(0.025,880,1130)]))/length(simvr)

#row2 (t)
simday2 <- matrix(rt(number*20000,5),ncol=20000)
sim2day1 <- simday2[1:1131,]
sim2day2 <- simday2[1132:2012,]
sim2sd1 <- apply(sim2day1,2,sd)
sim2sd2 <- apply(sim2day2,2,sd)
sim2vr <- (sim2sd2/sim2sd1)^2
c(quantile(sim2vr,0.025),quantile(sim2vr,0.975))
rej2 <- (length(sim2vr[sim2vr > qf(0.975,880,1130)])  + length(sim2vr[sim2vr < qf(0.025,880,1130)]))/length(sim2vr)

#row3 (bootstrap)

FF_d = ff[ff[,1]>=20120101&ff[,1]<=20191231,]
FF_d_r = log((FF_d$Mkt.RF+FF_d$RF)/100+1)
d_1 <- mkt[mkt$X<="20160630"&mkt$X>="20120101",]
d_2 <- mkt[mkt$X<="20191231"&mkt$X>="20160701",]

M_1 = matrix(sample(FF_d_r,20000*dim(d_1)[1], replace = T),nrow=dim(d_1)[1],ncol = 20000)
M_2 = matrix(sample(FF_d_r,20000*dim(d_2)[1], replace = T),nrow=dim(d_2)[1],ncol = 20000)
M_var_1 = apply(M_1, 2, var)
M_var_2 = apply(M_2, 2, var)
M_VR = M_var_1/M_var_2
M_VR = sort(M_VR)
sum(M_VR>=qf(0.975,880,1130))/20000+sum(M_VR<=qf(0.025,880,1130))/20000
M_VR[20000*0.975]
M_VR[20000*0.025]


# e)
qqplot(qf(ppoints(20000),880,1130),simvr,col="red",main="Figure 1a",xlab="F(880,1130)",ylab="Emperical Ratio")
abline(0,1)

qqplot(qf(ppoints(20000),880,1130),M_VR,col="red",main=" Figure 1b",xlab="F(880,1130)",ylab="Emperical Ratio")
abline(0,1)





#Problem 2
# d)
dstockret <- logdayret[logdayret$date<="20191231"&logdayret$date>="20150101",]
dusvw <- mkt[mkt$X<="20191231"&mkt$X>="20150101",][,2]
dbio <- dstockret[,6]
dpf <- dstockret[,2]
daz <- dstockret[,7]
dnik <- dstockret[,3]
#compiute the sigma d
sd(dbio)* sqrt(252)
sd(dpf)* sqrt(252)
sd(daz)* sqrt(252)
sd(dnik)* sqrt(252)

reg1<- lm(dbio ~ dusvw)
summary(reg1)
-0.0004995877 * 252 #annulize?
reg2 <- lm(dpf ~ dusvw)
summary(reg2)
-4.044e-06 * 252
reg3 <- lm(daz ~dusvw)
summary(reg3)
0.0001390 * 252
reg4 <- lm(dnik ~ dusvw)
summary(reg4)
0.0002192 * 252

#now compute the month data
dstockretm <- logmonret[logmonret$date<="20191231"&logmonret$date>="20150101",]
dusvwm <-   mktm[mktm$X<="20191231"&mktm$X>="201501",][,2]
dbiom <- dstockretm[,6]
dpfm <- dstockretm[,2]
dazm <- dstockretm[,7]
dnikm <- dstockretm[,3]
# sigma month
sd(dbiom)* sqrt(12)
sd(dpfm)* sqrt(12)
sd(dazm)* sqrt(12)
sd(dnikm)* sqrt(12)

regm1<- lm(dbiom ~ dusvwm)
summary(regm1)
-0.01110 * 12 #annulize?
regm2 <- lm(dpfm ~ dusvwm)
summary(regm2)
0.001157 * 12
regm3 <- lm(dazm ~dusvwm)
summary(regm3)
0.005475  * 12
regm4 <- lm(dnikm ~ dusvwm)
summary(regm4)
0.006096 * 12

# Make an equal weighted portfolio “EW Port” of the four stocks and regress it on the US market return
ewpt <- 0.25 * (dbio + dpf +daz + dnik)
regw<- lm(ewpt ~ dusvw)
summary(regw)

ewptm <- 0.25 * (dbiom + dpfm +dazm + dnikm)
regwm<- lm(ewptm ~ dusvwm)
summary(regwm)

# residual cross-correlation
resmatd <- matrix(0,ncol=4, nrow=1258)
resmatd[,1]<- reg1$residuals
resmatd[,2]<- reg2$residuals
resmatd[,3]<- reg3$residuals
resmatd[,4]<- reg4$residuals
cor(resmatd)

resmatm <- matrix(0,ncol=4, nrow=60)
resmatm[,1]<- regm1$residuals
resmatm[,2]<- regm2$residuals
resmatm[,3]<- regm3$residuals
resmatm[,4]<- regm4$residuals
cor(resmatm)


# Problem 3
library(sandwich)	# Contains corrections for cov matrices
library(lmtest)		# contains command coeftest
vcov(reg2)
vcov(summary(reg2))
coeftest(reg2)		# OLS
coefci(reg2)
confint(reg2)

coeftest(reg2,vcov=vcovHC)	# Hal White Heteroskedasticity only
vcovHC(reg2)		
coefci(reg2,vcov=vcovHC,level=0.95)

coeftest(reg2,vcov=vcovHAC)	# Hal White Heteroskedasticity only
vcovHAC(reg2)		
coefci(reg2,vcov=vcovHAC,level=0.95)

  