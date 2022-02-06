# Problem 1.b
p1 <- choose(171,5) * choose(365,1) * choose(364,166) / (365 ** 171)
# p1 reveals 0, because R computes 365 ** 171 as infinite result.

logp <- log(choose(171,5)) + log(choose(365,1)) + log(choose(364,166)) + lfactorial(166) - 171* log(365)
pp1 <- exp(logp)

# Problem 1.e
p2 <- 1 - exp(log(choose(365,171)) + lfactorial(171) - 171*log(365))




#problem 2
wkrf  <- read.csv("C:/Users/MSI_NB/Desktop/BU FALL 2021/MF793/HM1/F-F_Research_Data_Factors_weekly.csv",header=T)
rf = wkrf[4462:4931,2]
rf1 = wkrf[4462:4930,2]
rf2 = wkrf[4463:4931,2]

#simple count table
tablecount <- matrix(0,ncol=2,nrow=2)
tablecount[1,1] <-length(rf1[rf1<=0 & rf2 <=0])
tablecount[1,2] <-length(rf1[rf1<=0 & rf2 >0])
tablecount[2,1] <-length(rf1[rf1>0 & rf2 <=0])
tablecount[2,2] <-length(rf1[rf1>0 & rf2 >0])
tablecount

#joint probability 
tablej = tablecount / length(rf1)
tablej

#condition probability
r1 = length(rf1[rf1<=0]) / length(rf1)
r2 = length(rf1[rf1>0]) / length(rf1)

tablecon = tablej / c(r1,r2)
tablecon

#unconditional
pu = length(rf[rf<=0]) / length(rf)
pd = length(rf[rf>0]) / length(rf)
pu
pd





#Problem 4

#a)
dataa <- read.csv("C:/Users/MSI_NB/Desktop/BU FALL 2021/MF793/HM1/funds-1288g-mon.csv",header = T)	
mkrf  <- read.csv("C:/Users/MSI_NB/Desktop/BU FALL 2021/MF793/HM1/KF-Market-mon.csv",header=T)
rmret<-(mkrf[,2]+mkrf[,3])/100

rm = mean(rmret[1044:1092])
fund <- dataa[43:90,2:1289]
avreturn <- apply(fund,2,mean)

hist(avreturn*12,xlab="Mean Return",freq=T,nclass=100,main="")
title("Figure 1: Histogram of 1288 Fund Mean Returns, 2013/7-2017/6",line=0.2)
box()
abline(v=mean(avreturn)*12,col="black",lwd=2)
abline(v=rm*12,col="blue",lwd=2)
legend("topleft",c("Avg. Fund","Market"),bty="n",col=c("black","blue"),lwd=c(1,2),lty=1)

length(avreturn[avreturn>rm]) # 404 funds beat the market
length(avreturn[avreturn>rm])/1288 #31% of these funds beat the market


#b)

rm2 = mean(rmret[1093:1140])
fund2 <- dataa[91:138,2:1289]
avreturn2 <- apply(fund2,2,mean)

par(mgp=c(1.5,0.5,0))			
plot(avreturn*12,avreturn2*12,xlab="2013/7-2017/6 return",ylab="2017/7-2021/6 return")

title("Figure b1: 1288 fund returns, R1 vs R2",line=0.2)
abline(v=rm*12,lty=2):abline(h=rm2*12,lty=2)
abline(lsfit(avreturn*12,avreturn2*12),lty=3,lwd=2,col='blue')
abline(lsfit(avreturn[avreturn>0]*12,avreturn2[avreturn>0]*12),lty=4,lwd=2,col="red")

#plot ranks
rank1<-rank(avreturn)		
rank2<-rank(avreturn2)
plot(rank1,rank2,xlab="Rank1",ylab="Rank2")
title("Figure b2: Funds rank persistence from 2013/7-2017/6 to 2017/7-2021/6",line=0.5)
abline(lsfit(rank1,rank2))


#fill the tables
condition <- cbind(quantile(avreturn,c(0.15,0.85)),quantile(avreturn2,c(0.15,0.85))) 

#table A
tableA <- matrix(0,ncol=3,nrow=3)

tableA[1,1]<-length(avreturn[avreturn<condition[1,1]&avreturn2<condition[1,2]])
tableA[1,3]<-length(avreturn[avreturn<condition[1,1]&avreturn2>condition[2,2]])
tableA[1,2]<-length(avreturn[avreturn<condition[1,1]]) - tableA[1,1] - tableA[1,3]

tableA[3,1]<-length(avreturn[avreturn>condition[2,1]&avreturn2<condition[1,2]])
tableA[3,3]<-length(avreturn[avreturn>condition[2,1]&avreturn2>condition[2,2]])
tableA[3,2]<-length(avreturn[avreturn>condition[2,1]]) - tableA[3,1] - tableA[3,3]

tableA[2,1]<-length(avreturn[avreturn>condition[1,1]&avreturn<condition[2,1]&avreturn2<condition[1,2]])
tableA[2,3]<-length(avreturn[avreturn>condition[1,1]&avreturn<condition[2,1]&avreturn2>condition[2,2]])
tableA[2,2]<-length(avreturn[avreturn>condition[1,1]&avreturn<condition[2,1]]) - tableA[2,1] - tableA[2,3]

tableA

#table B (joint probability)
tableB = tableA / 1288
tableB

#table C (conditional porbability)
condp = c(0.15,0.7,0.15)
tableC = tableB / condp
tableC

# add a tabldD to show the condition probability with no persisitence
tableD <- matrix(0,ncol=3,nrow=3)
tableD[,1] <- 0.15
tableD[,2] <- 0.7
tableD[,3] <- 0.15
tableD


#c)

table2A <- matrix(0,ncol=2,nrow=2)
table2A[1,1] <- length(avreturn[avreturn<=rm&avreturn2<=rm2])
table2A[1,2] <- length(avreturn[avreturn<=rm&avreturn2>rm2])
table2A[2,1] <- length(avreturn[avreturn>rm&avreturn2<=rm2])
table2A[2,2] <- length(avreturn[avreturn>rm&avreturn2>rm2])
table2A

table2B = table2A / 1288
table2B

table2C = table2B / c(length(avreturn[avreturn<rm]),length(avreturn[avreturn>rm])) * 1288
table2C





#problem 5

BR = seq(0,90000)
EW = 11000 + 0.1 * BR
plot(BR,EW,xlab="Borrowed $B",ylab="$ EXPECTED wealth",type="l")
title("Figure 3: EXPECTED wealth vs the amount borrowed $B",line=0.2)

BR2 = seq(0,90000)
CE<--1/(-0.5/(13000+0.3*BR2)-0.5/(9000-0.1*BR2))
plot(BR2,CE,xlab="Borrowed $B",ylab="$ CE",type="l")
title("Figure 4: $CE vs the amount borrowed $B",line=0.2)
BR2[CE==max(CE)] #the best point is this, when BR2 = 5470		
points(BR2[CE==max(CE)], max(CE),pch=20,col="red")
text(BR2[CE==max(CE)], max(CE),"MAX(CE)",pos=1)








