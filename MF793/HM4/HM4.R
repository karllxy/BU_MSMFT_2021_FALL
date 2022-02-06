# problem 2.b
t <- 1/12
S <- 2960
X <- 2960
callreal <- 116.60 # we can change the parameter here
rf <- 0
upper <- 1
lower <- 0
sigma <- 0.5

d1 <- (log(S/X)+(rf+0.5*(sigma**2))*t)/sigma/(t**0.5)
d2 <- d1 - sigma*(t**0.5)
call <- S*pnorm(d1) - X * exp(-rf*t)*pnorm(d2)
call
while (abs(call-callreal)>=0.0001){
  if ((call-callreal)<0){
    lower<- sigma
  }
  if ((call-callreal)>0){
    upper <- sigma
  }
  if ((call-callreal)==0){
    break
  }
  sigma <- (lower+upper)/2
  d1 <- (log(S/X)+(rf+0.5*(sigma**2))*t)/sigma/(t**0.5)
  d2 <- d1 - sigma*(t**0.5)
  call <- S*pnorm(d1) - X * exp(-rf*t)*pnorm(d2)
}
call
sigma

call1 <- 0.3110576
call2 <- 0.3421874
(call2-call1)/call1
