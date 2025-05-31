import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="MBTI 총기 추천기", page_icon="🔫")
st.title("🔫 MBTI별 배틀그라운드 총기 추천기")

mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

mbti = st.selectbox("당신의 MBTI 유형을 선택하세요:", mbti_types)

# 총기 정보: 이미지 경로, 파츠, 탄약 종류
gun_info = {
    "M416": {
        "img": "images/m416.png",
        "parts": ["보정기", "수직 손잡이", "확장 탄창", "레드도트"],
        "ammo": "5.56mm"
    },
    "SKS": {
        "img": "images/sks.png",
        "parts": ["소음기", "치크패드", "6배율"],
        "ammo": "7.62mm"
    },
    "UMP45": {
        "img": "images/ump45.png",
        "parts": ["소음기", "확장 탄창", "버티컬 그립", "홀로그램"],
        "ammo": "0.45 ACP"
    },
    "Mini 14": {
        "img": "images/mini14.png",
        "parts": ["보정기", "치크패드", "4배율"],
        "ammo": "5.56mm"
    },
    "Groza": {
        "img": "images/groza.png",
        "parts": ["소음기", "확장 탄창", "홀로그램"],
        "ammo": "7.62mm"
    },
    "MK14": {
        "img": "images/mk14.png",
        "parts": ["소음기", "치크패드", "8배율"],
        "ammo": "7.62mm"
    },
    "Vector": {
        "img": "images/vector.png",
        "parts": ["소음기", "확장 탄창", "레이저 포인터"],
        "ammo": "9mm"
    },
    "Kar98k": {
        "img": "images/kar98k.png",
        "parts": ["소음기", "치크패드", "6배율"],
        "ammo": "7.62mm"
    }
}

# MBTI별 추천 무기 (AR/SMG, DMR/SR)
mbti_guns = {
    "ISTJ": ("M416", "SKS"),
    "ISFJ": ("UMP45", "Mini 14"),
    "INFJ": ("M416", "Mini 14"),
    "INTJ": ("Groza", "MK14"),
    "ISTP": ("UMP45", "Kar98k"),
    "ISFP": ("Vector", "Mini 14"),
    "INFP": ("UMP45", "SKS"),
    "INTP": ("M416", "MK14"),
    "ESTP": ("Groza", "Kar
