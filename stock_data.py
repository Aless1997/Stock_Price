import yfinance as yf
import pandas as pd

def get_stock_data(symbol, period):
    try:
        stock = yf.Ticker(symbol)
        df = stock.history(period=period)
        return df
    except Exception as e:
        print(f"Errore nel recupero dei dati per {symbol}: {e}")
        return None