import yfinance as yf
import pandas as pd
import numpy as np

def calculate_ml_metrics(tickers, start_date, end_date):
    # Download the adjusted close data for tickers in the specified date range
    data = yf.download(tickers, start=start_date, end=end_date, interval='1mo')['Adj Close']
    data = data.dropna()

    # Calculate monthly returns
    monthly_returns = data.pct_change().dropna() * 100

    # Define trailing periods
    trailing_periods = {
        "1M": 1,
        "3M": 3,
        "6M": 6,
        "1Y": 12,
        "2Y": 24,
        "3Y": 36,
        "5Y": 60
    }

    # Initialize DataFrame to store results
    results = pd.DataFrame(index=trailing_periods.keys(), columns=[
        "Cumulative Return (AAPL)", "Cumulative Return (NDX)",
        "Annualized Return (AAPL)", "Annualized Return (NDX)"
    ])

    # Calculate returns for each trailing period
    for period, months in trailing_periods.items():
        if months <= len(monthly_returns):  # Ensure enough data exists
            # Slice the last N months of data
            recent_returns = monthly_returns.iloc[-months:]

            # Cumulative Returns
            cumulative_aapl = (np.prod(1 + recent_returns['AAPL'] / 100) - 1) * 100
            cumulative_ndx = (np.prod(1 + recent_returns['^NDX'] / 100) - 1) * 100

            # Annualized Returns
            if months <= 12:  # For periods ≤ 1 year
                annualized_aapl = cumulative_aapl
                annualized_ndx = cumulative_ndx
            else:  # For periods > 1 year
                years = months / 12
                annualized_aapl = ((1 + cumulative_aapl / 100) ** (1 / years) - 1) * 100
                annualized_ndx = ((1 + cumulative_ndx / 100) ** (1 / years) - 1) * 100

            # Store results
            results.loc[period] = [cumulative_aapl, cumulative_ndx, annualized_aapl, annualized_ndx]

    results = results.round(2)
    return results
