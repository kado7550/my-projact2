import streamlit as st

# 시즌별 데이터
f1_data = {
    "2024": {
        "winner_driver": "Max Verstappen",
        "winner_team": "McLaren",
        "highlights": "Verstappen의 4연패 달성, McLaren의 26년 만의 컨스트럭터 우승",
        "tech": "하이브리드 파워 유닛의 최적화",
    },
    "2023": {
        "winner_driver": "Max Verstappen",
        "winner_team": "Red Bull Racing",
        "highlights": "Red Bull의 압도적인 시즌, Verstappen의 3연패",
        "tech": "효율적인 에어로다이내믹 패키지",
    },
    # ... (1990년부터 2022년까지의 데이터 추가)
    "1990": {
        "winner_driver": "Ayrton Senna",
        "winner_team": "McLaren",
        "highlights": "Senna와 Prost의 치열한 경쟁",
        "tech": "액티브 서스펜션 도입",
    },
}

# 드라이버 성적 데이터
driver_history = {
    "Max Verstappen": {
        "World Championships": 4,
        "Wins": 70,
        "Podiums": 100,
        "Debut": "2015",
    },
    "Ayrton Senna": {
        "World Championships": 3,
        "Wins": 41,
        "Podiums": 80,
        "Debut": "1984",
    },
    # ... (기타 드라이버 데이터 추가)
}

# 팀 성적 데이터
team_history = {
    "McLaren": {
        "World Championships": 9,
        "Wins": 183,
        "Debut": "1966",
    },
    "Red Bull Racing": {
        "World Championships": 6,
        "Wins": 113,
        "Debut": "2005",
    },
    # ... (기타 팀 데이터 추가)
}

# Streamlit 앱 구성
st.title("🏎️ 시즌별 드라이버/팀 순위 분석")

# 시즌 선택
season = st.selectbox("시즌을 선택하세요", sorted(f1_data.keys(), reverse=True))

if st.button("해당 시즌 분석 보기"):
    data = f1_data[season]
    st.subheader(f"🏁 {season} 시즌 요약")

    # 관전 포인트 및 기술
    st.markdown("### 🎯 관전 포인트")
    st.write(data["highlights"])

    st.markdown("### 🔧 대표적인 기술")
    st.write(data["tech"])

    # 드라이버 & 팀 클릭 시 성적 표시
    st.markdown("### 🏆 시즌 우승자 및 팀")

    col1, col2 = st.columns(2)

    with col1:
        if st.button(f"드라이버 우승자: {data['winner_driver']}"):
            name = data['winner_driver']
            if name in driver_history:
                st.markdown(f"#### {name} 역대 성적")
                st.json(driver_history[name])
            else:
                st.warning("드라이버 정보가 없습니다.")

    with col2:
        if st.button(f"컨스트럭터 우승팀: {data['winner_team']}"):
            team = data['winner_team']
            if team in team_history:
                st.markdown(f"#### {team} 팀 역대 성적")
                st.json(team_history[team])
            else:
                st.warning("팀 정보가 없습니다.")

