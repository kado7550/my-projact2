import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="배그 총기 추천기", layout="centered")
st.title("🎮 배그 실력 기반 총기 및 파츠 추천기")
st.write("플레이어의 실력과 플레이 시간에 맞는 근접전/저격전 추천 무기, 파츠, 배율 정보를 제공합니다.")

# 사용자 입력
time_played = st.slider("총 플레이 시간 (시간 단위)", 0, 1000, 50)
days_played = st.slider("플레이한 일 수", 0, 365, 30)
kd = st.slider("K/D 비율", 0.0, 10.0, 1.0, 0.1)
avg_damage = st.slider("평균 딜량", 0, 1000, 150)
win_rate = st.slider("승률 (%)", 0, 100, 5)

# 총기 추천 로직
def recommend_weapons(kd, dmg, win, hours, days):
    score = (kd * 2 + dmg / 100 + win / 10 + hours / 100 + days / 30)

    if score < 10:
        return {
            "레벨": "초보자",
            "근접": [
                {
                    "이름": "UMP45",
                    "성능": "낮은 반동과 안정적인 조작성",
                    "파츠": ["소음기", "수직 손잡이"],
                    "배율": "Red Dot",
                    "탄 종류": ".45 ACP",
                    "이미지": "images/ump45.jpg"
                },
                {
                    "이름": "Vector",
                    "성능": "빠른 연사 속도, 근거리에서 강력함",
                    "파츠": ["소음기", "앵글 손잡이"],
                    "배율": "홀로그램",
                    "탄 종류": ".45 ACP",
                    "이미지": "images/vector.jpg"
                }
            ],
            "저격": [
                {
                    "이름": "SKS",
                    "성능": "초보자에게 적당한 반자동 저격총",
                    "파츠": ["소음기", "척추 손잡이"],
                    "배율": "4배율",
                    "탄 종류": "7.62mm",
                    "이미지": "images/sks.jpg"
                },
                {
                    "이름": "Mini14",
                    "성능": "낮은 탄퍼짐, 빠른 연사",
                    "파츠": ["보정기", "체크 패드"],
                    "배율": "3배율",
                    "탄 종류": "5.56mm",
                    "이미지": "images/mini14.jpg"
                }
            ]
        }
    elif score < 18:
        return {
            "레벨": "중급자",
            "근접": [
                {
                    "이름": "M416",
                    "성능": "전천후 사용 가능, 안정적인 반동 제어",
                    "파츠": ["보정기", "수직 손잡이"],
                    "배율": "Red Dot",
                    "탄 종류": "5.56mm",
                    "이미지": "images/m416.jpg"
                },
                {
                    "이름": "Beryl M762",
                    "성능": "높은 데미지, 어려운 반동",
                    "파츠": ["앵글 손잡이", "보정기"],
                    "배율": "2배율",
                    "탄 종류": "7.62mm",
                    "이미지": "images/beryl.jpg"
                }
            ],
            "저격": [
                {
                    "이름": "SLR",
                    "성능": "강한 반동과 높은 데미지",
                    "파츠": ["보정기", "척추 손잡이"],
                    "배율": "6배율",
                    "탄 종류": "7.62mm",
                    "이미지": "images/slr.jpg"
                },
                {
                    "이름": "Mini14",
                    "성능": "균형 잡힌 저격총",
                    "파츠": ["보정기", "체크 패드"],
                    "배율": "3배율",
                    "탄 종류": "5.56mm",
                    "이미지": "images/mini14.jpg"
                }
            ]
        }
    else:
        return {
            "레벨": "고수",
            "근접": [
                {
                    "이름": "Mk47 Mutant",
                    "성능": "단발 화력 강력, 고난이도",
                    "파츠": ["소음기", "체크 패드"],
                    "배율": "3배율",
                    "탄 종류": "7.62mm",
                    "이미지": "images/mk47.jpg"
                },
                {
                    "이름": "Beryl M762",
                    "성능": "높은 DPS, 반동 제어 필수",
                    "파츠": ["보정기", "수직 손잡이"],
                    "배율": "2배율",
                    "탄 종류": "7.62mm",
                    "이미지": "images/beryl.jpg"
                }
            ],
            "저격": [
                {
                    "이름": "Mk14",
                    "성능": "DMR 중 최강 화력, 반동 높음",
                    "파츠": ["소음기", "DMR 손잡이"],
                    "배율": "6배율",
                    "탄 종류": "7.62mm",
                    "이미지": "images/mk14.jpg"
                },
                {
                    "이름": "AWM",
                    "성능": "가장 강력한 볼트액션 저격총",
                    "파츠": ["소음기"],
                    "배율": "8배율",
                    "탄 종류": ".300 Magnum",
                    "이미지": "images/awm.jpg"
                }
            ]
        }

# 추천 실행
if st.button("🔍 추천 받기"):
    result = recommend_weapons(kd, avg_damage, win_rate, time_played, days_played)
    st.subheader(f"🎯 추천 결과 - {result['레벨']}")

    for category in ["근접", "저격"]:
        st.markdown(f"### 🧩 {category}전 추천")
        for weapon in result[category]:
            st.markdown(f"**🔫 {weapon['이름']}**")
            st.markdown(f"- 성능: {weapon['성능']}")
            st.markdown(f"- 추천 파츠: {', '.join(weapon['파츠'])}")
            st.markdown(f"- 추천 배율: {weapon['배율']}")
            st.markdown(f"- 탄 종류: {weapon['탄 종류']}")
            if os.path.exists(weapon['이미지']):
                st.image(Image.open(weapon['이미지']), width=400)
            else:
                st.markdown("(이미지를 찾을 수 없습니다)")
