import streamlit as st

# 드라이버 이력 및 사진
driver_history = {
    "Max Verstappen": {
        "World Championships": 4,
        "Wins": 70,
        "Podiums": 100,
        "Debut": "2015",
        "image": "https://upload.wikimedia.org/wikipedia/commons/8/88/Max_Verstappen_2017_Malaysia_3.jpg"
    },
    "Lewis Hamilton": {
        "World Championships": 7,
        "Wins": 103,
        "Podiums": 195,
        "Debut": "2007",
        "image": "https://upload.wikimedia.org/wikipedia/commons/2/2e/Lewis_Hamilton_2016_Malaysia_3.jpg"
    },
}

# 팀 이력 및 로고
team_history = {
    "Red Bull Racing": {
        "World Championships": 6,
        "Wins": 113,
        "Debut": "2005",
        "logo": "https://upload.wikimedia.org/wikipedia/en/thumb/6/6e/Red_Bull_Racing_logo.svg/320px-Red_Bull_Racing_logo.svg.png"
    },
    "Mercedes": {
        "World Championships": 8,
        "Wins": 125,
        "Debut": "1954",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/Mercedes-Benz_in_Formula_One_logo.svg/320px-Mercedes-Benz_in_Formula_One_logo.svg.png"
    },
    "McLaren": {
        "World Championships": 9,
        "Wins": 183,
        "Debut": "1966",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/McLaren_Racing_logo.svg/320px-McLaren_Racing_logo.svg.png"
    }
}

# 시즌 데이터
f1_data = {
    "2024": {
        "winner_driver": "Max Verstappen",
        "winner_team": "McLaren",
        "highlights": "Verstappen의 4연패, McLaren의 대반전 시즌",
        "tech": "하이브리드 파워 유닛의 정점, 경량화 섀시",
    },
    "2023": {
        "winner_driver": "Max Verstappen",
        "winner_team": "Red Bull Racing",
        "highlights": "Verstappen의 3연패, Red Bull의 압도적인 득점력",
        "tech": "효율적인 그라운드 이펙트 설계",
    },
    "2022": {
        "winner_driver": "Max Verstappen",
        "winner_team": "Red Bull Racing",
        "highlights": "새로운 규정 아래 Ferrari와 경쟁, 후반기 압도",
        "tech": "18인치 타이어 도입, 바운싱 문제",
    },
    "2021": {
        "winner_driver": "Max Verstappen",
        "winner_team": "Mercedes",
        "highlights": "Verstappen vs Hamilton 극적인 결말",
        "tech": "고속 직선 vs 다운포스 전략",
    },
    "2020": {
        "winner_driver": "Lewis Hamilton",
        "winner_team": "Mercedes",
        "highlights": "COVID-19 단축 시즌, Hamilton의 7번째 타이틀",
        "tech": "DAS 시스템, 하이브리드 전략",
    },
}

# ---------------- Streamlit UI ----------------

st.title("🏁 F1 시즌 분석 대시보드")

# 메뉴 선택
menu = st.sidebar.selectbox("메뉴를 선택하세요", ["시즌별 분석", "드라이버 이력", "팀 이력"])

# 시즌별 분석
if menu == "시즌별 분석":
    season = st.selectbox("시즌을 선택하세요", sorted(f1_data.keys(), reverse=True))
    if st.button("해당 시즌 분석 보기"):
        data = f1_data[season]
        st.subheader(f"🏆 {season} 시즌 요약")
        st.markdown("### 🎯 관전 포인트")
        st.write(data["highlights"])

        st.markdown("### 🔧 대표 기술")
        st.write(data["tech"])

        st.markdown("### 🏎️ 우승 드라이버 및 팀")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown(f"#### 🧑‍✈️ {data['winner_driver']}")
            if data["winner_driver"] in driver_history:
                st.image(driver_history[data["winner_driver"]]["image"], width=200)
                st.write(driver_history[data["winner_driver"]])
            else:
                st.warning("드라이버 정보가 없습니다.")

        with col2:
            st.markdown(f"#### 🏢 {data['winner_team']}")
            if data["winner_team"] in team_history:
                st.image(team_history[data["winner_team"]]["logo"], width=200)
                st.write(team_history[data["winner_team"]])
            else:
                st.warning("팀 정보가 없습니다.")

# 드라이버 이력
elif menu == "드라이버 이력":
    driver = st.selectbox("드라이버를 선택하세요", sorted(driver_history.keys()))
    info = driver_history[driver]
    st.markdown(f"## {driver}")
    st.image(info["image"], width=250)
    st.write({k: v for k, v in info.items() if k != "image"})

# 팀 이력
elif menu == "팀 이력":
    team = st.selectbox("팀을 선택하세요", sorted(team_history.keys()))
    info = team_history[team]
    st.markdown(f"## {team}")
    st.image(info["logo"], width=250)
    st.write({k: v for k, v in info.items() if k != "logo"})


