def calculate_metrics(data):
    if data is None or data.empty:
        raise ValueError("Data is empty or invalid.")
    monthly_returns = data.pct_change().dropna()
    mean_return = monthly_returns.mean()
    risk = monthly_returns.std()
    # print(monthly_returns,mean_return,risk)
    return {
        "mean_return": mean_return,
        "risk": risk
    }
