# import zoo package
library("zoo")

#Read the data
dret = read.csv("/Users/liuxuyang/Desktop/BU\ FALL\ 2021/MF793/TakeHome/spret-day-2020.csv",header=T)

# Use the data from 2018 to 2020
dret = dret[dret[,1]<20210000&dret[,1]>20180000,]

# Days per year
dpy = length(dret[,1])/3

# RW length&lambda
wlen = 63
lam = 0.95

# RW series
rw = sqrt(rollapply(dret[,c(2)]^2,wlen,mean)*dpy)

# Time seq
dates = as.character(dret[(63:length(dret[,c(1)])), c(1)])
dates = as.Date(dates, "%Y%m%d")

# RM series
rm = rep(0,length(rw))
rm[1] = rw[1]^2/dpy

for(i in 2:length(rw))
{
  rm[i]<-lam*rm[i-1]+(1-lam)*dret[wlen+i, c(2)]^2
}
rm = sqrt(rm*dpy)

# The Dataframe of RW&RM time series
df = data.frame(dates, rw, rm)

# Have the first value at 2019-01-02
df = df[df[,c(1)]>as.Date("2019-01-01"),]

# (a)
# Plot
# RM
plot(df[,c(1)], df[,c(3)], type='l',col='red',ylab='Std',xlab='Time')
# RW
lines(df[,c(1)], df[,c(2)], col='blue')
# Title
title("Figure 1:S$P 500, Risk-metrics vx Standard RW")
# Legend
legend("topright",c("RW","RM, lambda=0.95"), col=c("blue", "red"), lwd=1,bty="n")
#x-axis
#axis(1,at=s,format(df[s, c(1)],"%y/%m"))

# (d)
# Start from 2019-01-02
dret2 = dret[dret[,c(1)]>20190000,]

# original method
rm3 = rep(0, 60)
rm3[1] = df[1,3]^2/dpy
for(i in 2:60)
{
  rm3[i]<-lam*rm3[i-1]+(1-lam)*dret2[wlen+i, c(2)]^2
}
rm3 = sqrt(rm3*dpy)

# RM1 equal to RW1
rm2 = rep(0, 60)
rm2[1] = df[1,2]^2/dpy
for(i in 2:60)
{
  rm2[i]<-lam*rm2[i-1]+(1-lam)*dret2[wlen+i, c(2)]^2
}
rm2 = sqrt(rm2*dpy)

plot(df[1:60,1], rm3, type='l',col='blue',ylab='Std',xlab='Time')
lines(df[1:60,1], rm2, type='l',col='red')
title("Figure 2:Different Initialization Method")
legend("topright",c("Original RM","New RM"), col=c("blue", "red"), lwd=1,bty="n")

