**Stock Price Forecasting**
========================

A Python-based web application that uses the Prophet library for time series forecasting and FastAPI for API
endpoints. The application collects historical stock prices using Yahoo Finance's yfinance library.

**Introduction**
---------------

This project aims to provide a simple and efficient way to forecast stock prices using historical data. The
application collects data from Yahoo Finance, processes it with the Prophet library, and provides API endpoints
for users to retrieve forecasts.

**Getting Started**
------------------

To run the application locally:

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment: `source venv/bin/activate` (on Linux/Mac) or `venv\Scripts\activate` (on
Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Run the application: `python main.py`

**Features**
------------

* **Prophet-based forecasting**: The application uses the Prophet library to forecast stock prices based on
historical data.
* **FastAPI endpoints**: Users can retrieve forecasts through API endpoints, including:
        + `/predict`: Retrieves the forecast for a specific stock symbol.

**Requirements**
----------------

* Python 3.8+
* FastAPI
* Prophet
* yfinance
* pandas
