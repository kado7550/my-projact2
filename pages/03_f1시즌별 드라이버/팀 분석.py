import streamlit as st

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
        "tech": "새로운 18인치 타이어, 바운싱 문제 해결",
    },
    "2021": {
        "winner_driver": "Max Verstappen",
        "winner_team": "Mercedes",
        "highlights": "Verstappen vs Hamilton 시즌 전체 대결, 아부다비에서 극적인 결말",
        "tech": "하이 다운포스 vs 고속 직선 주행 세팅 전략",
    },
    "2020": {
        "winner_driver": "Lewis Hamilton",
        "winner_team": "Mercedes",
        "highlights": "COVID-19로 축소된 시즌, Hamilton의 7번째 타이틀",
        "tech": "DAS 시스템 (Dual-Axis Steering), 하이브리드 효율성",
    },
}

# 드라이버 이력
driver_history = {
    "Max Verstappen": {
        "World Championships": 4,
        "Wins": 70,
        "Podiums": 100,
        "Debut": "2015",
    },
    "Lewis Hamilton": {
        "World Championships": 7,
        "Wins": 103,
        "Podiums": 195,
        "Debut": "2007",
    },
}

# 팀 이력
team_history = {
    "Red Bull Racing": {
        "World Championships": 6,
        "Wins": 113,
        "Debut": "2005",
    },
    "Mercedes": {
        "World Championships": 8,
        "Wins": 125,
        "Debut": "1954",
    },
    "McLaren": {
        "World Championships": 9,
        "Wins": 183,
        "Debut": "1966",
    },
}

# ---------- 스트림릿 앱 ----------

st.title("🏁 F1 시즌 분석 대시보드")

# 메뉴 선택 (사이드바)
menu = st.sidebar.selectbox("메뉴를 선택하세요", ["시즌별 분석", "드라이버 이력", "팀 이력"])

# 1. 시즌별 분석
if menu == "시즌별 분석":
    season = st.selectbox("시즌을 선택하세요", sorted(f1_data.keys(), reverse=True))
    if st.button("해당 시즌 분석 보기"):
        data = f1_data[season]
        st.subheader(f"🏆 {season} 시즌 요약")
        
        st.markdown("### 🎯 관전 포인트")
        st.write(data["highlights"])

        st.markdown("### 🔧 대표 기술")
        st.write(data["tech"])

        st.markdown("### 🚗 우승 드라이버 및 팀")
        col1, col2 = st.columns(2)

        with col1:
            if st.button(f"드라이버: {data['winner_driver']}"):
                name = data['winner_driver']
                st.markdown(f"#### {name} 역대 성적")
                st.json(driver_history.get(name, "정보 없음"))

        with col2:
            if st.button(f"팀: {data['winner_team']}"):
                team = data['winner_team']
                st.markdown(f"#### {team} 역대 성적")
                st.json(team_history.get(team, "정보 없음"))

# 2. 드라이버 이력
elif menu == "드라이버 이력":
    driver = st.selectbox("드라이버 선택", sorted(driver_history.keys()))
    st.subheader(f"🏎️ {driver}의 커리어")
    st.json(driver_history[driver])

# 3. 팀 이력
elif menu == "팀 이력":
    team = st.selectbox("팀 선택", sorted(team_history.keys()))
    st.subheader(f"🔧 {team} 팀 정보")
    st.json(team_history[team])

