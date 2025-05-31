import streamlit as st

st.set_page_config(page_title="MBTI 총기 추천기", page_icon="🔫")
st.title("🔫 MBTI별 배틀그라운드 총기 추천기")

# MBTI 목록
mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

mbti = st.selectbox("당신의 MBTI 유형을 선택하세요:", mbti_types)

# 총기 정보 (이름: 이미지 URL 및 추천 파츠)
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

# MBTI별 추천 총기
mbti_guns = {
    "ISTJ": ("M416", "SKS"),
    "ISFJ": ("UMP45", "Mini 14"),
    "INFJ": ("M416", "Mini 14"),
    "INTJ": ("Groza", "MK14"),
    "ISTP": ("UMP45", "Kar98k"),
    "ISFP": ("Vector", "Mini 14"),
    "INFP": ("UMP45", "SKS"),
    "INTP": ("M416", "MK14"),
    "ESTP": ("Groza", "Kar98k"),
    "ESFP": ("Vector", "Kar98k"),
    "ENFP": ("M416", "Mini 14"),
    "ENTP": ("Groza", "SKS"),
    "ESTJ": ("M416", "SKS"),
    "ESFJ": ("UMP45", "Mini 14"),
    "ENFJ": ("M416", "Kar98k"),
    "ENTJ": ("Groza", "MK14")
}

# 출력
if mbti in mbti_guns:
    gun1, gun2 = mbti_guns[mbti]

    st.markdown("### 🔸 추천 무기 1 (AR 또는 SMG)")
    st.image(gun_info[gun1]["img"], caption=gun1, width=300)
    st.markdown("**추천 파츠:**")
    for part in gun_info[gun1]["parts"]:
        st.write(f"- {part}")

    st.markdown("### 🔸 추천 무기 2 (DMR 또는 SR)")
    st.image(gun_info[gun2]["img"], caption=gun2, width=300)
    st.markdown("**추천 파츠:**")
    for part in gun_info[gun2]["parts"]:
        st.write(f"- {part}")
else:
    st.warning("이 MBTI에 대한 총기 정보가 아직 준비되지 않았습니다.")
