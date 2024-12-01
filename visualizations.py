import matplotlib.pyplot as plt

def create_visualization(data, tickers):
    plt.figure(figsize=(10, 6))
    for ticker in tickers:
        rebased = data[ticker] / data[ticker].iloc[0] * 100
        plt.plot(rebased, label=ticker)
    plt.legend()
    plt.title('Stock Prices Rebased to 100')

    # Save the plot to the 'static' folder with a dynamic name
    chart_path = f'static/stock_chart_{"_".join(tickers)}.png'
    plt.savefig(chart_path)
    plt.close()  # Close the plot to free up memory
    return chart_path