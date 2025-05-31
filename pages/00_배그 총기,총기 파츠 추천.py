import streamlit as st

st.set_page_config(page_title="배그 총기 추천기", layout="centered")

st.title("🔫 배틀그라운드 총기 및 파츠 추천기")
st.write("당신의 실력에 맞는 최적의 무기 조합을 알려드립니다!")

# 사용자 입력 받기
kd = st.slider("K/D 비율", 0.0, 10.0, 1.0, 0.1)
avg_damage = st.slider("평균 딜량", 0, 1000, 150)
win_rate = st.slider("승률 (%)", 0, 100, 5)

# 추천 로직
def recommend_weapon(kd, dmg, win):
    score = (kd * 2 + dmg / 100 + win / 10)

    if score < 10:
        return {
            "레벨": "초보자",
            "총기": "M416",
            "파츠": ["수직 손잡이", "소음기", "확장 탄창"]
        }
    elif score < 18:
        return {
            "레벨": "중급자",
            "총기": "Beryl M762",
            "파츠": ["앵글 손잡이", "보정기", "퀵드로우 탄창"]
        }
    else:
        return {
            "레벨": "고수",
            "총기": "Mk14",
            "파츠": ["DMR 손잡이", "소음기", "대용량 탄창"]
        }

# 결과 추천
if st.button("🔍 추천 받기"):
    result = recommend_weapon(kd, avg_damage, win_rate)
    st.subheader(f"🎯 추천 결과 - {result['레벨']}")
    st.markdown(f"**추천 총기:** {result['총기']}")
    st.markdown("**추천 파츠:**")
    for part in result["파츠"]:
        st.markdown(f"- {part}")
