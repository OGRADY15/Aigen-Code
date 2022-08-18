#Sean O'Grady - IEDP 544 Final Project Code
#Done in conjunction with lab partner: Marcus Leong

#FTSE 100 Index

library(astsa)
install.packages("tseries")
library(tseries)
install.packages("forecast")
library(forecast)
EuStockMarkets
FTSE=EuStockMarkets[,4]
plot(FTSE, main="FTSE in Levels")
logftse=log(FTSE)
plot(logftse, main="FTSE in Logs Levels")
dlogftse=diff(logftse,1)
plot(dlogftse, main="FTSE in Returns")
acf(dlogftse)
pacf(dlogftse)
adf.test(dlogftse)
ftsemodel=auto.arima(logftse, ic="aic", trace=TRUE)
sarima(logftse,1,1,0)
dlogftse2=(dlogftse)^2
plot(dlogftse2, main="Squared of FTSE Returns")
resu=sarima(logftse,1,1,0)
resu2=(resid(resu$fit))^2
plot(resu2, main="Plot of Squared of Standa")
acf(resu2)
pacf(resu2)

auto.arima(resu2, ic="aic", trace=TRUE)

library(fGarch)
summary(garchFit(~arma(1,0)+garch(1,1),dlogftse))

# Bitcoin

bc = read.csv("C:/Users/ograd/Downloads/BTC-USD (4).csv")
bc
btctime=ts(bc[,6], frequency=12, start=c(2015,1))
plot(btctime, main="Bitcoin Price")
logbtctime=log(btctime)
plot(logbtctime, main="Bitcoin in Logs Price")
dlbc=diff(logbtctime,1)
plot(dlbc, main="Bitcoin in Returns")
adf.test(dlbc)
acf(dlbc)
pacf(dlbc)
auto.arima(logbtctime, ic="aic", trace=TRUE)
sarima(logbtctime,0,1,0)
dlbc2=(dlbc)^2
plot(dlbc2, main="Squared of Bitcoin")
resu=sarima(dlbc,0,0,0)
resu2=(resid(resu$fit))^2
plot(resu2, main="Plot of Squared of Standardized Residuals")
acf(resu2)
pacf(resu2)

auto.arima(resu2, ic="aic", trace=TRUE)

library(fGarch)
summary(garchFit(~arma(0,0)+garch(1,2),dlbc))
