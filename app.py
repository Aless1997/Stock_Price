import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from stock_data import get_stock_data

st.set_page_config(page_title="Monitoraggio Azioni", page_icon="📈", layout="wide")

st.title("📈 Monitoraggio Azioni Finanziarie")

# Input per il simbolo dell'azione
stock_symbol = st.text_input("Inserisci il simbolo dell'azione (es. AAPL per Apple):", "AAPL").upper()

# Selezione dell'intervallo di tempo
time_period = st.selectbox("Seleziona il periodo di tempo:", ["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "max"])

# Ottieni i dati dell'azione
df = get_stock_data(stock_symbol, time_period)

if df is not None:
    # Mostra le informazioni principali
    current_price = df['Close'].iloc[-1]
    price_change = df['Close'].iloc[-1] - df['Close'].iloc[0]
    price_change_percent = (price_change / df['Close'].iloc[0]) * 100

    col1, col2, col3 = st.columns(3)
    col1.metric("Prezzo Attuale", f"${current_price:.2f}")
    col2.metric("Variazione", f"${price_change:.2f}")
    col3.metric("Variazione %", f"{price_change_percent:.2f}%")

    # Crea il grafico
    fig = go.Figure()
    fig.add_trace(go.Candlestick(x=df.index,
                                 open=df['Open'],
                                 high=df['High'],
                                 low=df['Low'],
                                 close=df['Close'],
                                 name='Candlestick'))
    fig.update_layout(title=f'Grafico a Candele per {stock_symbol}',
                      xaxis_title='Data',
                      yaxis_title='Prezzo',
                      xaxis_rangeslider_visible=False)

    st.plotly_chart(fig, use_container_width=True)

    # Mostra i dati in una tabella
    st.subheader("Dati storici")
    st.dataframe(df)
else:
    st.error("Impossibile recuperare i dati dell'azione. Verifica il simbolo inserito.")