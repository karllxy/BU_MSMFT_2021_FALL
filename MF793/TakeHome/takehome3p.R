#Problem 3
library(zoo)
winlen <- 63
spret <- read.csv("/Users/liuxuyang/Desktop/BU\ FALL\ 2021/MF793/TakeHome/spret-day-2020.csv",header=T)
azdret <- spret[spret[,1]>20181001 & spret[,1]< 20210000,2]
#RW estimator
varvec <- rollapply(azdret^2,winlen,mean)# use mean = 0 method
rw <- sqrt(varvec * 252)

#RMd
lam <- 0.95
rm <-rep(0,length(varvec))
rm[1]<- varvec[1]
for(i in 64:length(azdret)){
  rm[i-62]<-lam*rm[i-63]+(1-lam)*azdret[i]^2
  }
rm<-sqrt(rm * 252)


spret <- spret[spret[,1]>20190000 & spret[,1]<20210000,c(1,2)]
zdates <- as.Date(as.character(spret[,1]),format="%Y%m%d")
par(mfrow=c(2,1),mgp=c(1.5,0.5,0))
zlength <- length(zdates)
plot(ts(rm),ylab="Annualized Std Deviation",col="blue",xaxt="n")
lines(ts(rw),col="red")
axis(1,at=seq(1,zlength-winlen+1,32),format(zdates[seq(winlen,zlength,32)],"%y/%m"))
title("RW vs RM",line=0.3,cex.main=0.95)
legend("topleft",c("RW","RM"),col=c("red","blue"),lwd=1,bty="n")

#4)
rm_2 <- rep(0,length(varvec))
rm_2[1] <- spret[spret[,1]==20190102,2]^2
for(i in 64:length(azdret)){
  rm_2[i-62]<-lam*rm_2[i-63]+(1-lam)*azdret[i]^2
}
rm_2 <- sqrt(rm_2 * 252)

rm <- rm[1:62]
rn_2 <- rm_2[1:62]
ylim=c(0,0.7)
plot(ts(rm),ylab="Annualized Std",col="red",xaxt="n",ylim=c(0,0.7))
lines(ts(rm_2),col="blue")
axis(1,at=seq(1,62,5),format(zdates[seq(1,62,5)],"%y/%m/%d"))
title("Annualized Std",line=0.3,cex.main=0.95)
legend("topleft",c("RM","RM2"),col=c("red","blue"),lwd=1,bty=1)
















