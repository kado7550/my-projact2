import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# 페이지 제목
st.title("전세계 시가총액 Top 10 기업 주가 변동")

# 기업 목록 및 티커
companies = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Alphabet (Google)": "GOOGL",
    "Amazon": "AMZN",
    "Nvidia": "NVDA",
    "Berkshire Hathaway": "BRK-B",
    "Meta Platforms": "META",
    "Tesla": "TSLA",
    "TSMC": "TSM",
    "Saudi Aramco": "2222.SR"  # 주의: 데이터 안 나올 수 있음
}

# 기간 선택
period = st.selectbox("조회 기간", ["1mo", "3mo", "6mo", "1y", "2y", "5y"])

# 기업 선택 (다중 선택)
selected_companies = st.multiselect("기업 선택", options=list(companies.keys()), default=list(companies.keys())[:5])

# 데이터 조회 및 시각화
for name in selected_companies:
    ticker = companies[name]
    try:
        data = yf.download(ticker, period=period)
        if not data.empty:
            st.subheader(f"{name} ({ticker}) 주가 추이")
            st.line_chart(data['Close'])
        else:
            st.warning(f"{name} ({ticker}) 데이터가 없습니다.")
    except Exception as e:
        st.error(f"{name} 데이터를 불러오는 중 오류 발생: {e}")
