data <- read.csv("/Users/liuxuyang/Desktop/BU\ FALL\ 2021/MF793/HM3/Vanguard.csv",header =T)
vsiax <- data[,2]
vsgax <- data[,3]

# compute log return
logreturn1 <- matrix(0,nrow=length(vsiax)-1,ncol=1)
for ( i in 2:length(vsiax)){
  logreturn1[i-1] <- log(vsiax[i])-log(vsiax[i-1])
}

logreturn2 <- matrix(0,nrow=length(vsiax)-1,ncol=1)
for ( i in 2:length(vsgax)){
  logreturn2[i-1] <- log(vsgax[i])-log(vsgax[i-1])
  
}

#1.2
t.test(logreturn1)
c(mean(logreturn1)-qt(0.975,df=n-1)*sd(logreturn1)/sqrt(n),                 mean(logreturn1) +qt(0.975,df=n-1)*sd(logreturn1)/sqrt(n))
c(mean(logreturn1)*52-qt(0.975,df=n-1)*sd(logreturn1)*52/sqrt(n) ,    mean(logreturn1)*52 +qt(0.975,df=n-1)*sd(logreturn1)*52/sqrt(n))#这个是对的


n = length(logreturn1)
t.test(logreturn2)
t.test(logreturn1-logreturn2)

#得不到正确答案
c(sd(logreturn1)-qt(0.975,df=n-1)*sd(logreturn1)/sqrt(2*n),sd(logreturn1) +qt(0.975,df=n-1)*sd(logreturn1)/sqrt(2*n))#approximate, use this way
c(sd(logreturn1) * sqrt((n-1)/qchisq(0.975,df=n-1)) , sd(logreturn1) * sqrt((n-1)/qchisq(0.025,df=n-1)))#exact, i compute wrongly
c(sd(logreturn2) * sqrt((n-1)/qchisq(0.975,n-1)) , sd(logreturn2) * sqrt((n-1)/qchisq(0.025,n-1)))
c(sd(logreturn1-logreturn2) * sqrt((n-1)/qchisq(0.975,n-1)) , sd(logreturn1-logreturn2) * sqrt((n-1)/qchisq(0.025,n-1)))
c(mean(logreturn1)*52-qt(0.975,df=n-1)*sd(logreturn1)*sqrt(52)/sqrt(n),mean(logreturn1)*52 +qt(0.975,df=n-1)*sd(logreturn1)*sqrt(52)/sqrt(n))

c(sd(logreturn1)*sqrt(52)-qt(0.975,df=n-1)*sd(logreturn1)*52/sqrt(2*n/52),sd(logreturn1)*sqrt(52) +qt(0.975,df=n-1)*sd(logreturn1)*52/sqrt(2*n/51))#approximate, use this way
c(sd(logreturn1)*sqrt(52) * sqrt((n)/qchisq(0.975,n-1)) , sd(logreturn1) * sqrt(52)* sqrt((n)/qchisq(0.025,n-1)))
c(sd(logreturn2)*sqrt(52) * sqrt((n)/qchisq(0.975,n-1)) , sd(logreturn2) * sqrt(52)* sqrt((n)/qchisq(0.025,n-1)))



#1.3
library(EnvStats)
skw1 = skewness(as.numeric(logreturn1))
kur1 = kurtosis(as.numeric(logreturn1))+3
mean(((((mean(logreturn1)-logreturn1))/sd(logreturn1))**4))
mean(((mean(logreturn1)-logreturn1)/sd(logreturn1))**3)
SES = sqrt(6*n*(n-1)/(n-2)/(n+1)/(n+3))# standard error
KSD  =sqrt( 4*(n^2-1) * SES^2 / ((n-3)*(n+5)) )

c(skw1-1.96*SES, skw1+1.96*SES)
c(kur1 - 1.644 * KSD, kur1 + 1.644 * KSD)

skw2 = skewness(as.numeric(logreturn2))
kur2 = kurtosis(as.numeric(logreturn2))+3
c(skw2-1.96*SES, skw2+1.96*SES)
c(kur2 - 1.644 * KSD, kur2 + 1.644 * KSD)

#1.4 no rejection of zero skewness, massive rejection of kur
#1.5
JB <- function(skw,kur) skw**2 * n/6 + (kur-3)**2 *n / 24
JB(skw1,kur1)
if(!require(tseries)){install.packages('tseries')}
jarque.bera.test(logreturn1)
jarque.bera.test(logreturn2)

#1.6
diff = logreturn1 - logreturn2
mean(diff)
sd(diff)
c(mean(diff)-qt(0.975,df=n-1)*sd(diff)/sqrt(n),mean(diff) +qt(0.975,df=n-1)*sd(diff)/sqrt(n))
c(sd(diff) * sqrt((n-1)/qchisq(0.975,n-1)) , sd(diff) * sqrt((n-1)/qchisq(0.025,n-1)))

c(mean(diff)*52-qt(0.975,df=n-1)*sd(diff)*sqrt(52)/sqrt(n),mean(diff)*52 +qt(0.975,df=n-1)*sd(diff)*sqrt(52)/sqrt(n))
c(sd(diff)*sqrt(52) * sqrt((n)/qchisq(0.975,n-1)) , sd(diff) * sqrt(52)* sqrt((n)/qchisq(0.025,n-1)))

#1.7
f1 = logreturn1[1:119]#or 118??? 答案不一样
f2 = logreturn1[118:259]
sd(f1)**2*118/119 / (sd(f2)**2*138/139)
var.test(f1,f2)





#2.1
daily<-read.csv("/Users/liuxuyang/Desktop/BU\ FALL\ 2021/MF793/HM3/stk-11-day-2010-2017.csv",header =T)
monthly <- read.csv("/Users/liuxuyang/Desktop/BU\ FALL\ 2021/MF793/HM3/stk-11-mon-2010-2017.csv",header =T)
logdaily <- log(1+daily[,2:13])[,5]
n1 <- length(logdaily)
logmonth <- log(1+monthly[,2:13])[,5]
ud = mean(logdaily)
ud
sdd = sd(logdaily)
sdd
c(ud-qt(0.975,df=n1-1)*sdd/sqrt(n1),ud +qt(0.975,df=n1-1)*sdd/sqrt(n1))
c(sdd * sqrt((n1-1)/qchisq(0.975,n1-1)) , sdd * sqrt((n1-1)/qchisq(0.025,n1-1)))

c(sdm * sqrt((n2-1)/qchisq(0.975,n2-1)) , sdm * sqrt((n2-1)/qchisq(0.025,n2-1)))
pd1 = acf(logdaily,lag.max=2)
pd


#2.2
um = mean(logmonth)
sdm = sd(logmonth)
n2 = length(logmonth)
t = (um-0.01)/(sdm/sqrt(n2))

#2.3
t = (um-0.01)/(sdm/sqrt(n2))
sd#不会写

#2.4&2.5
c(sdm-qt(0.975,n2-1)*sdm/sqrt(2*n2),sdm+qt(0.975,n2-1)*sdm/sqrt(2*n2))#approximate
c(sdm * sqrt((n2-1)/qchisq(0.975,n2-1)) , sdm * sqrt((n2-1)/qchisq(0.025,n2-1)))#Exact

c(sdd-qt(0.975,n1-1)*sdd/sqrt(2*n1),sdd+qt(0.975,n1-1)*sdd/sqrt(2*n1))#approximate
c(sdd * sqrt((n1-1)/qchisq(0.975,n1-1)) , sdd * sqrt((n1-1)/qchisq(0.025,n1-1)))#Exact




#3.1
ffdata <- read.csv("/Users/liuxuyang/Desktop/BU\ FALL\ 2021/MF793/HM3/FF-Factors-day.csv",header =T)
ffreturns <- (ffdata[,2]+ffdata[,5])[4328:24896]/100
ffreturns <- log(1+ffreturns)
nf<- length(ffreturns)
uf <- mean(ffreturns)
sdf <- sd(ffreturns)
c(uf-10*sdf/sqrt(nf),uf+10*sdf/sqrt(nf))
sum(length(ffreturns[ffreturns<uf-1]))
skewness(ffreturns)
kurtosis(ffreturns)



##actual number
sum(length(ffreturns[ffreturns<uf-10*sdf]))
sum(length(ffreturns[ffreturns<uf-5*sdf]))
sum(length(ffreturns[ffreturns<uf-4*sdf]))
sum(length(ffreturns[ffreturns<uf-3*sdf]))
sum(length(ffreturns[ffreturns<uf-2*sdf]))
sum(length(ffreturns[ffreturns<uf-1.96*sdf]))
sum(length(ffreturns[ffreturns<uf-1.646*sdf]))

#expected number
round(pnorm(uf-10*sdf,mean=uf,sd=sdf)*nf)
round(pnorm(uf-5*sdf,mean=uf,sd=sdf)*nf)
round(pnorm(uf-4*sdf,mean=uf,sd=sdf)*nf)
round(pnorm(uf-3*sdf,mean=uf,sd=sdf)*nf)
round(pnorm(uf-2*sdf,mean=uf,sd=sdf)*nf)
round(pnorm(uf-1.96*sdf,mean=uf,sd=sdf)*nf)
round(pnorm(uf-1.646*sdf,mean=uf,sd=sdf)*nf)

a = ffreturns[ffreturns>uf-2*sdf&ffreturns<uf+2*sdf] #remember both side!
skewness(a)



#4
pp <- 275/500
pp*(1-pp)
c(pp-1.96*sqrt(pp*(1-pp)/500),pp+1.96*sqrt(pp*(1-pp)/500))
