import yfinance as yf
aapl =yf.Ticker("AAPL")
aapl_historical = aapl.history(start="2021-01-02", end="2021-03-02", interval="30m")
print(aapl_historical)
print(aapl)
print(dir(aapl))