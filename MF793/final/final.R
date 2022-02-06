library(forecast)
library(tseries)

#Problem 1
ret <- rep(0,500);muy <- 0.10/252	;sigy <- 0.15/sqrt(252)
phi1 <- 0.5;phi2 <- 0.2
alpha <- muy*(1-phi1-phi2)
sige  <- sigy * sqrt(1-phi1^2-phi2^2)
ret[1] <- muy;epst   <- rnorm(500,0,sige)
ret[2] <- alpha + muy*phi1 + epst[i]
for (i in 3:500) 	{ ret[i] <- alpha+ phi1*ret[i-1] + phi2*ret[i-2] + epst[i]}
par(mfrow=c(1,2),mgp=c(1.5,0.5,0),mar=c(3,3,2,0.5))
Acf(ret,lag.max=30);title("ACF of Return")	
lines(seq(1,22),phi^seq(1,22),col="red")
Acf(ret,lag.max=30,type="partial")
title("PACF of Return")

#Problem 2
cutoff1 <- qf(c(0.025,0.975),47,23)
cutoff2 <- qf(c(0.025,0.975),1007,503)

#Problem 6
e <- rnorm(10000,0,1)
std <- rchisq(10000,8) / 8
rand<- rnorm(10000,sd(std))

nms <- std * e
Kur <- mean(((nms-mean(nms))/sd(nms))^4) 
Kur
par(mfrow=c(1,1))
qqnorm(nms)
qqline(nms,col="red")









