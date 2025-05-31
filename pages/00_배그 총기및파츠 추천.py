import streamlit as st

st.set_page_config(page_title="MBTI 총기 추천기", page_icon="🔫")
st.title("🔫 MBTI별 배틀그라운드 총기 추천기")

mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

mbti = st.selectbox("당신의 MBTI 유형을 선택하세요:", mbti_types)

# 총기 정보: 이미지 URL, 파츠, 탄약 종류
gun_info = {
    "M416": {
        "img": "https://i.ibb.co/Pg0qJNd/m416.png",
        "parts": ["보정기", "수직 손잡이", "확장 탄창", "레드도트"],
        "ammo": "5.56mm"
    },
    "SKS": {
        "img": "https://i.ibb.co/yR6zGr4/sks.png",
        "parts": ["소음기", "치크패드", "6배율"],
        "ammo": "7.62mm"
    },
    "UMP45": {
        "img": "https://i.ibb.co/LJyKy2v/ump45.png",
        "parts": ["소음기", "확장 탄창", "버티컬 그립", "홀로그램"],
        "ammo": "0.45 ACP"
    },
    "Mini 14": {
        "img": "https://i.ibb.co/ZJQhfXg/mini14.png",
        "parts": ["보정기", "치크패드", "4배율"],
        "ammo": "5.56mm"
    },
    "Groza": {
        "img": "https://i.ibb.co/J3qXnLD/groza.png",
        "parts": ["소음기", "확장 탄창", "홀로그램"],
        "ammo": "7.62mm"
    },
    "MK14": {
        "img": "https://i.ibb.co/ynzK49W/mk14.png",
        "parts": ["소음기", "치크패드", "8배율"],
        "ammo": "7.62mm"
    },
    "Vector": {
        "img": "https://i.ibb.co/v1s1cTW/vector.png",
        "parts": ["소음기", "확장 탄창", "레이저 포인터"],
        "ammo": "9mm"
    },
    "Kar98k": {
        "img": "https://i.ibb.co/synmZQW/kar98k.png",
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
    "ESTP": ("Groza", "Kar98k"),
    "ESFP": ("Vector", "Kar98k"),
    "ENFP": ("M416", "Mini 14"),
    "ENTP": ("Groza", "SKS"),
    "ESTJ": ("M416", "SKS"),
    "ESFJ": ("UMP45", "Mini 14"),
    "ENFJ": ("M416", "Kar98k"),
    "ENTJ": ("Groza", "MK14")
}

# 추천 결과 출력
if mbti in mbti_guns:
    gun1, gun2 = mbti_guns[mbti]

    st.markdown("### 🔸 추천 무기 1 (AR 또는 SMG)")
    st.image(gun_info[gun1]["img"], caption=f"{gun1} ({gun_info[gun1]['ammo']})", width=300)
    st.markdown("**추천 파츠:**")
    for part in gun_info[gun1]["parts"]:
        st.write(f"- {part}")

    st.markdown("### 🔸 추천 무기 2 (DMR 또는 SR)")
    st.image(gun_info[gun2]["img"], caption=f"{gun2} ({gun_info[gun2]['ammo']})", width=300)
    st.markdown("**추천 파츠:**")
    for part in gun_info[gun2]["parts"]:
        st.write(f"- {part}")
else:
    st.warning("이 MBTI 유형에 대한 총기 정보가 아직 준비되지 않았습니다.")
