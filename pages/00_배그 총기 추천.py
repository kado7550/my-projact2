import streamlit as st

st.title("MBTI별 배틀그라운드 추천 총기")

mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

mbti = st.selectbox("당신의 MBTI 유형을 선택하세요:", mbti_types)

# 각 MBTI에 대해: (AR 또는 SMG, DMR 또는 SR)
mbti_guns = {
    "ISTJ": ("M416 (AR)", "SKS (DMR)"),
    "ISFJ": ("M16A4 (AR)", "Mini 14 (DMR)"),
    "INFJ": ("QBZ (AR)", "QBU (DMR)"),
    "INTJ": ("AUG A3 (AR)", "MK14 (DMR)"),
    "ISTP": ("Beryl M762 (AR)", "SLR (DMR)"),
    "ISFP": ("UMP45 (SMG)", "Mini 14 (DMR)"),
    "INFP": ("Tommy Gun (SMG)", "VSS (DMR)"),
    "INTP": ("SCAR-L (AR)", "MK12 (DMR)"),
    "ESTP": ("Beryl M762 (AR)", "M24 (SR)"),
    "ESFP": ("Vector (SMG)", "Kar98k (SR)"),
    "ENFP": ("SCAR-L (AR)", "SKS (DMR)"),
    "ENTP": ("Groza (AR)", "AWM (SR)"),
    "ESTJ": ("M416 (AR)", "SLR (DMR)"),
    "ESFJ": ("M16A4 (AR)", "QBU (DMR)"),
    "ENFJ": ("AUG A3 (AR)", "Kar98k (SR)"),
    "ENTJ": ("Groza (AR)", "MK14 (DMR)")
}

if mbti in mbti_guns:
    st.subheader(f"{mbti} 유형에게 추천되는 배그 총기:")
    st.write(f"- 돌격소총 / SMG: **{mbti_guns[mbti][0]}**")
    st.write(f"- DMR / 저격소총: **{mbti_guns[mbti][1]}**")
