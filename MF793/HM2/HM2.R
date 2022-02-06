

#Problem 2

#a)
u <- runif(10000,-2,2)
v <- runif(10000,u,2)

plot(density(v),xlab = 'v',main = 'The marginal univariate density of v')

library(MASS)	# package needed for kde2d
bivden<-kde2d(u,v)
persp(bivden,theta=-30,phi=25,col="green", xlab="u",ylab="v",ticktype="detailed",main = 'The bivariate density of (u,v)')

#b)
mean(v) 
library(lattice)
library(plyr)
library(Rmisc)
CI(v,ci=0.95)





#Problem 4

#b)
mu1 <- 0
sigma1 <- 0.2
testvalue<- matrix(0,nrow=1,ncol=100)
toptvalue<- matrix(0,nrow=10000,ncol=5)
randvalue<- matrix(0,nrow=10000,ncol=1)

for (j in 1:10000){
  

  for (i in 1:100){
    stock_return <- rnorm(250*4,0,0.2)
    tt<- t.test(stock_return,mu=0)$statistic
    testvalue[1,i] <- abs(tt)
  }
  topt <- sort(testvalue,decreasing=TRUE)[1:5]
  rant <- sample(testvalue,size=1)
  toptvalue[j,] <- topt
  randvalue[j,] <- rant
}

#create the table for answer
answertable <- matrix(0,nrow=3,ncol=3)
answertable[1,1] <- mean(toptvalue[,1])
answertable[1,2] <- mean(toptvalue[,5])
answertable[1,3] <- mean(randvalue)
answertable[2,1] <- colSums(abs(toptvalue>=1.96)/nrow(toptvalue))[1] # not sure whether i should choose 1.96 or not.
answertable[2,2] <- colSums(abs(toptvalue>=1.96)/nrow(toptvalue))[5]
answertable[2,3] <- colSums(abs(randvalue>=1.96)/nrow(toptvalue))[1]
answertable[3,1] <- quantile(toptvalue[,1],0.975)
answertable[3,2] <- quantile(toptvalue[,5],0.975)
answertable[3,3] <- quantile(randvalue[,1],0.975)
answertable

#c)
t1 <- toptvalue[,1]
t5 <- toptvalue[,5]
t0 <- randvalue[,1]
plot(density(t1),main='The density of t1,t5 and t0',col=2,xlim=c(0,4.5),ylim=c(0,2.1),xlab = "Value",ylab ="Probability")
lines(density(t5),col=3)
lines(density(t0),col=4)
legend('topright',pch=c(15,15),legend=c('t1','t5','t0'),col=c(2,3,4),bty='n')






# Problem 5
library(readr)
FF_Factors_day <- read.csv("C:/Users/MSI_NB/Desktop/BU FALL 2021/MF793/HM2/FF-Factors-day.csv",header =T)
FF_Factors_week <- read.csv("C:/Users/MSI_NB/Desktop/BU FALL 2021/MF793/HM2/FF-Factors-week.csv",header=T)
FF_Factors_mon <- read.csv("C:/Users/MSI_NB/Desktop/BU FALL 2021/MF793/HM2/FF-Factors-mon.csv",header=T)
FF_Factors_year <- read.csv("C:/Users/MSI_NB/Desktop/BU FALL 2021/MF793/HM2/FF-Factors-year.csv",header=T)

daily <- (FF_Factors_day[14304:19360,2]+FF_Factors_day[14304:19360,5])/100
logdaily <- log(1+daily)
week <- (FF_Factors_week[2740:3783,2]+FF_Factors_week[2740:3783,5])/100
logweek <- log(1+week)
month <- (FF_Factors_mon[631:870,2]+FF_Factors_mon[631:870,5])/100
logmon <- log(1+month)
year <- (FF_Factors_year[53:72,2]+FF_Factors_year[53:72,5])/100
logyear <- log(1+year)

#check the daily number
mean(logdaily) #0.00063, right
sd(logdaily) #0.00982, right
library(EnvStats)
skewness(logdaily)
kurtosis(logdaily)+3
acf(logdaily, plot = FALSE)[1]# p(1)

table2 <- matrix(0,3,7)
table2[1,1] <- mean(logweek)
table2[1,2] <- sd(logweek)
table2[1,3] <- sum(logweek)/20
table2[1,4] <- sd(logweek)*((252/5)**0.5)
table2[1,5] <- skewness(logweek)
table2[1,6] <- kurtosis(logweek)+3
table2[1,7] <- as.numeric(unlist(acf(logweek, plot = FALSE)[1]))[1]

table2[2,1] <- mean(logmon)
table2[2,2] <- sd(logmon)
table2[2,3] <- sum(logmon)/20
table2[2,4] <- sd(logmon)*((252/21)**0.5)
table2[2,5] <- skewness(logmon)
table2[2,6] <- kurtosis(logmon)+3
table2[2,7] <- as.numeric(unlist(acf(logmon, plot = FALSE)[1]))[1]

table2[3,1] <- mean(logyear)
table2[3,2] <- sd(logyear)
table2[3,3] <- sum(logyear)/20
table2[3,4] <- sd(logyear)
table2[3,5] <- skewness(logyear)
table2[3,6] <- kurtosis(logyear)+3
table2[3,7] <- as.numeric(unlist(acf(logyear, plot = FALSE)[1]))[1]
table2
