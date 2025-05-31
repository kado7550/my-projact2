import streamlit as st

st.title("🔫 MBTI별 배틀그라운드 총기 추천기")

mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

mbti = st.selectbox("당신의 MBTI 유형을 선택하세요:", mbti_types)

# 총기 정보 딕셔너리 (이름: {이미지, 파츠})
gun_info = {
    "M416": {
        "img": "https://static.wikia.nocookie.net/pubg/images/2/2c/M416.png",
        "parts": ["보정기", "수직 손잡이", "확장 탄창", "레드도트"]
    },
    "SKS": {
        "img": "https://static.wikia.nocookie.net/pubg/images/f/f2/SKS.png",
        "parts": ["소음기", "치크패드", "6배율"]
    },
    "UMP45": {
        "img": "https://static.wikia.nocookie.net/pubg/images/0/04/UMP45.png",
        "parts": ["소음기", "확장 탄창", "버티컬 그립", "홀로그램"]
    },
    "Mini 14": {
        "img": "https://static.wikia.nocookie.net/pubg/images/f/fe/Mini14.png",
        "parts": ["보정기", "치크패드", "4배율"]
    },
    "Groza": {
        "img": "https://static.wikia.nocookie.net/pubg/images/5/5e/Groza.png",
        "parts": ["소음기", "확장 탄창", "홀로그램"]
    },
    "MK14": {
        "img": "https://static.wikia.nocookie.net/pubg/images/5/54/Mk14.png",
        "parts": ["소음기", "치크패드", "8배율"]
    },
    "Vector": {
        "img": "https://static.wikia.nocookie.net/pubg/images/6/63/Vector.png",
        "parts": ["소음기", "확장 탄창", "레이저 포인터"]
    },
    "Kar98k": {
        "img": "https://static.wikia.nocookie.net/pubg/images/2/2d/Kar98k.png",
        "parts": ["소음기", "치크패드", "6배율"]
    }
}

# MBTI별 추천 총기 (AR/SMG, DMR/SR)
mbti_guns = {
