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



n = length(logreturn1)
t.test(logreturn2)
t.test(logreturn1-logreturn2)

#得不到正确答案
#1.3
library(EnvStats)
skw1 = skewness(as.numeric(logreturn1))
kur1 = kurtosis(as.numeric(logreturn1))+3
mean(((((mean(logreturn1)-logreturn1))/sd(logreturn1))**4))
mean(((mean(logreturn1)-logreturn1)/sd(logreturn1))**3)
SES = sqrt(6*n*(n-1)/(n-2)/(n+1)/(n+3))# standard error
KSD  =sqrt( 4*(n^2-1) * SES^2 / ((n-3)*(n+5)) )

#1.4 no rejection of zero skewness, massive rejection of kur
#1.5
JB <- function(skw,kur) skw**2 * n/6 + (kur-3)**2 *n / 24
JB(skw1,kur1)
if(!require(tseries)){install.packages('tseries')}
jarque.bera.test(logreturn1)
jarque.bera.test(logreturn2)

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





