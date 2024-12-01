def calculate_metrics(data):
    if data is None or data.empty:
        raise ValueError("Data is empty or invalid.")
    monthly_returns = data.pct_change().dropna()*100
    mean_return = monthly_returns.mean()
    risk = monthly_returns.std()
    return {
        "mean_return": mean_return,
        "risk": risk
    }