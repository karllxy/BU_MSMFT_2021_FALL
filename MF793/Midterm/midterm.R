daily<-read.csv("/Users/liuxuyang/Desktop/BU\ FALL\ 2021/MF793/HM3/stk-11-day-2010-2017.csv",header =T)
monthly <- read.csv("/Users/liuxuyang/Desktop/BU\ FALL\ 2021/MF793/HM3/stk-11-mon-2010-2017.csv",header =T)
logdaily <- log(1+daily[,2:13])[,2]
logdaily <- logdaily[253:1510]
n1 <- length(logdaily)

logmonth <- log(1+monthly[,2:13])[,2]
logmonth <- logmonth[13:72]
ud = mean(logdaily)
ud
sdd = sd(logdaily)
sdd
sdm <- sd(logmonth)
sdm
n2 <- length(logmonth)
c(sdd * sqrt((n1-1)/qchisq(0.975,n1-1)) , sdd * sqrt((n1-1)/qchisq(0.025,n1-1)))
c(sdm * sqrt((n2-1)/qchisq(0.975,n2-1)) , sdm * sqrt((n2-1)/qchisq(0.025,n2-1)))

sda<-sdd*sqrt(252)
sma<-sdm*sqrt(12)

c(sda * sqrt((n1/252-1)/qchisq(0.975,n1/252-1)) , sda * sqrt((n1/252-1)/qchisq(0.025,n1/252-1)))
c(sma * sqrt((n2/12-1)/qchisq(0.975,n2/12-1)) , sma * sqrt((n2/12-1)/qchisq(0.025,n2/12-1)))
