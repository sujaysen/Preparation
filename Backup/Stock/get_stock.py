import yfinance as yf
data = yf.Ticker("TCS").history(period='1d')
print(data.info())

