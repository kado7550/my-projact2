import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta

st.set_page_config(page_title="시가총액 TOP10 변화", layout="wide")
st.title("📈 전 세계 시가총액 TOP10 기업의 3년간 변화")

# 전 세계 시가총액 Top 10 기업 티커 목록 (2024년 기준 예시)
top10_tickers = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Saudi Aramco": "2222.SR",
    "Alphabet": "GOOGL",
    "Amazon": "AMZN",
    "Nvidia": "NVDA",
    "Berkshire Hathaway": "BRK-B",
    "Meta": "META",
    "TSMC": "TSM",
    "Tesla": "TSLA"
}

start_date = datetime.today() - timedelta(days=365 * 3)
end_date = datetime.today()

@st.cache_data
def fetch_market_cap_data(tickers):
    data = {}
    for name, ticker in tickers.items():
        try:
            ticker_obj = yf.Ticker(ticker)
            hist = ticker_obj.history(start=start_date, end=end_date, interval="1mo")
            shares_outstanding = ticker_obj.info.get("sharesOutstanding", None)
            
            if shares_outstanding is None:
                st.warning(f"{name}의 주식 수 데이터를 찾을 수 없습니다.")
                continue

            hist["Market Cap"] = hist["Close"] * shares_outstanding
            hist = hist[["Market Cap"]].rename(columns={"Market Cap": name})
            data[name] = hist
        except Exception as e:
            st.error(f"{name} 데이터 로드 실패: {e}")
    
    return data

data_dict = fetch_market_cap_data(top10_tickers)

# 모든 데이터프레임 병합
if data_dict:
    market_caps = pd.concat(data_dict.values(), axis=1)
    market_caps.index = market_caps.index.strftime("%Y-%m")
    market_caps.dropna(inplace=True)

    # 단위: 조 달러
    fig = go.Figure()
    for company in market_caps.columns:
        fig.add_trace(go.Scatter(x=market_caps.index, y=market_caps[company] / 1e12,
                                 mode='lines+markers', name=company))

    fig.update_layout(
        title="전 세계 시가총액 TOP10 기업의 시가총액 추이 (단위: 조 달러)",
        xaxis_title="날짜",
        yaxis_title="시가총액 (조 달러)",
        hovermode="x unified"
    )

    st.plotly_chart(fig, use_container_width=True)
else:
    st.error("데이터를 불러오지 못했습니다.")

