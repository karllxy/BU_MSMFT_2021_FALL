#
# USING THE LM COMMAND
#

ddd<-read.csv("/Users/liuxuyang/Desktop/Amgen-Chevron.csv")
rets<-ddd[,2:5]
nasd<-ddd$NDAQ
bond<-ddd$BLV
amgn<-ddd$AMGN
cvx <-ddd$CVX

mod2<-lm(cvx~nasd+bond)
mod1<-lm(cvx~nasd)

#
# lm stores fitted.values,coef, vcov, residuals
#         and their degrees of freedom

names(mod2)

coef(mod2)
cvx - fitted.values(mod2) - residuals(mod2)	# What should that be ?
df.residual(mod1);length(cvx)				# nu and T
plot(fitted.values(mod1),residuals(mod1),xlab="Fitted",ylab="Residual")

vcov(mod1)		    # V(b)	 The correct vcov of beta-hat
sqrt(diag(mod1)) 	# Sqrt of diagonal elements of the cov matrix

# For more interesting output we use  summary.lm
# summary gives a full output

names(summary(mod1))		
summary(mod1)
summary(mod1,correlation=T)
acf(residuals(mod2))
###########################################################
#  "summary" stores more interesting values:
#  residuals,coefficients,sigma,fstatistic,r.squared
#  adj.r.squared,cov.unscaled

summary(mod1)$cov			# Careful this is unscaled, just (X'X)^(-1)
summary(mod1)$cov.unscaled	# same thing!

xmat   <-cbind(rep(1,365),nasd)	
xpxinv <- solve(t(xmat) %*% xmat)	# homemade (X'X)-1

summary(mod1)$cov * summary(mod1)$sigma^2
vcov(mod1)

# Confidence intervals for parameters

confint(mod1)
confint(mod2)

##########################################################
# Prediction: Predict.lm
#
predict(mod1)-mod1$fitted	# Just the fitted values again!
predict(mod1,se.fit=T)

# How about at a specific x value

xf<-c(-0.04,0.0038,0.04)
predict(mod1,list(nasd=xf),se.fit=T,interval="pred")
predict(mod1,list(nasd=xf),se.fit=T,interval="conf")


# Are the residuals normally distributed?
# The Jarque Bera test is in the moments package

library(moments)
jarque.test(residuals(mod1))

#
# Autocorrelation of residuals: Acf command
#
acf(mod1$residual)

plot(mod1)


#
# Computing HAC robust standard errors
# requires the sandwich and lmtest packages
# Sandwich has the robust covariance estimators
# 
library(sandwich);library(lmtest)
summary(mod1)$coefficients
coeftest(mod1,vcov=vcovHC)
coeftest(mod1,vcov=vcovHAC)



