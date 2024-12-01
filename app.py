from flask import Flask, render_template, request
from data_fetcher import fetch_data
from calculations import calculate_metrics
from visualizations import create_visualization

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    tickers = request.form['tickers'].split(',')
    start_date = request.form['start_date']
    end_date = request.form['end_date']

    data = {}
    metrics = {}
    
    # Fetch data and calculate metrics for each ticker
    for ticker in tickers:
        try:
            ticker_data = fetch_data(ticker.strip(), start_date, end_date)
            data[ticker] = ticker_data
            metrics[ticker] = calculate_metrics(ticker_data)
        except Exception as e:
            print(f"Error processing {ticker}: {e}")
            data[ticker] = None
            metrics[ticker] = {"error": str(e)}

    # Create visualization and get the path to the chart image
    chart_path = create_visualization(data, tickers)

    # Render the results page with metrics and the chart image
    return render_template('results.html', metrics=metrics, chart_path=chart_path)

if __name__ == "__main__":
    app.run(debug=True)
