import streamlit as st

st.title("MBTI별 배틀그라운드 추천 총기")

mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

mbti = st.selectbox("당신의 MBTI 유형을 선택하세요:", mbti_types)

mbti_guns = {
    "ISTJ": ["M416", "SKS"],
    "ISFJ": ["M16A4", "Mini 14"],
    "INFJ": ["QBU", "DP-28"],
    "INTJ": ["SLR", "MK14"],
    "ISTP": ["AKM", "Win94"],
    "ISFP": ["UMP45", "Tommy Gun"],
    "INFP": ["VSS", "Crossbow"],
    "INTP": ["MK12", "M24"],
    "ESTP": ["Beryl M762", "S12K"],
    "ESFP": ["Vector", "Micro UZI"],
    "ENFP": ["SCAR-L", "Kar98k"],
    "ENTP": ["AUG A3", "Groza"],
    "ESTJ": ["M416", "DP-28"],
    "ESFJ": ["M16A4", "UMP45"],
    "ENFJ": ["SCAR-L", "SKS"],
    "ENTJ": ["Groza", "AWM"]
}

if mbti in mbti_guns:
    st.subheader(f"{mbti} 유형에게 추천되는 배그 총기:")
    for gun in mbti_guns[mbti]:
        st.write(f"- {gun}")
