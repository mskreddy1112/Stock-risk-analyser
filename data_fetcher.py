import yfinance as yf

def fetch_data(ticker, start_date, end_date):
    try:
        data = yf.download(ticker, start=start_date, end=end_date, interval="1d")
        if data.empty:
            raise ValueError(f"No data available for {ticker} in the specified date range.")
        if 'Adj Close' not in data.columns:
            raise KeyError(f"'Adj Close' column not found for {ticker}")
        return data['Adj Close']
    except Exception as e:
        raise ValueError(f"Error fetching data for {ticker}: {e}")