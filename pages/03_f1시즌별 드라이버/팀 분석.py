import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# 상태 초기화
if "page" not in st.session_state:
    st.session_state.page = "main"
if "season" not in st.session_state:
    st.session_state.season = None
if "driver" not in st.session_state:
    st.session_state.driver = None
if "team" not in st.session_state:
    st.session_state.team = None

# 드라이버 데이터
driver_history = {
    "Max Verstappen": {
        "World Championships": 4,
        "Wins": 70,
        "Podiums": 100,
        "Debut": "2015",
        "image": "https://raw.githubusercontent.com/f1-data/images/main/drivers/max_verstappen.jpg",
        "seasons": {"2020": 2, "2021": 1, "2022": 1, "2023": 1, "2024": 1}
    },
    "Lewis Hamilton": {
        "World Championships": 7,
        "Wins": 103,
        "Podiums": 195,
        "Debut": "2007",
        "image": "https://raw.githubusercontent.com/f1-data/images/main/drivers/lewis_hamilton.jpg",
        "seasons": {"2020": 1, "2021": 2}
    }
}

# 팀 데이터
team_history = {
    "Red Bull Racing": {
        "World Championships": 6,
        "Wins": 113,
        "Debut": "2005",
        "logo": "https://raw.githubusercontent.com/f1-data/images/main/teams/red_bull.png",
        "seasons": {"2022": 1, "2023": 1}
    },
    "Mercedes": {
        "World Championships": 8,
        "Wins": 125,
        "Debut": "1954",
        "logo": "https://raw.githubusercontent.com/f1-data/images/main/teams/mercedes.png",
        "seasons": {"2020": 1, "2021": 1}
    },
    "McLaren": {
        "World Championships": 9,
        "Wins": 183,
        "Debut": "1966",
        "logo": "https://raw.githubusercontent.com/f1-data/images/main/teams/mclaren.png",
        "seasons": {"2024": 1}
    }
}

# 시즌 데이터
f1_data = {
    "2024": {
        "winner_driver": "Max Verstappen",
        "winner_team": "McLaren",
        "highlights": "Verstappen의 4연패, McLaren의 대반전 시즌",
        "tech": "하이브리드 파워 유닛의 정점, 경량화 섀시",
        "highlight_video": "https://www.youtube.com/watch?v=example2024",
        "tech_detail": "2024 시즌에는 하이브리드 시스템의 효율과 경량화를 극대화한 섀시가 도입되며 McLaren의 퍼포먼스에 큰 영향을 미쳤습니다."
    },
    "2023": {
        "winner_driver": "Max Verstappen",
        "winner_team": "Red Bull Racing",
        "highlights": "Verstappen의 3연패, Red Bull의 압도적인 득점력",
        "tech": "효율적인 그라운드 이펙트 설계",
        "highlight_video": "https://www.youtube.com/watch?v=example2023",
        "tech_detail": "Red Bull은 2023년 시즌에서 그라운드 이펙트를 최적화한 설계로 다운포스를 높이고 직선 속도를 유지했습니다."
    },
    "2022": {
        "winner_driver": "Max Verstappen",
        "winner_team": "Red Bull Racing",
        "highlights": "Ferrari와 치열한 경쟁 끝에 우승",
        "tech": "18인치 타이어와 그라운드 이펙트 적용",
        "highlight_video": "https://www.youtube.com/watch?v=example2022",
        "tech_detail": "18인치 타이어가 도입되며 전략 변화가 발생했고, 차량 하부 그라운드 이펙트를 이용한 설계가 경기력 향상에 기여했습니다."
    },
    "2021": {
        "winner_driver": "Max Verstappen",
        "winner_team": "Mercedes",
        "highlights": "Verstappen vs Hamilton의 역사적 시즌",
        "tech": "고속 코너링 설계, 세트업 전쟁",
        "highlight_video": "https://www.youtube.com/watch?v=example2021",
        "tech_detail": "고속 코너에서의 접지력 개선을 위한 서스펜션 세트업이 시즌의 성패를 가른 주요 기술 요소였습니다."
    },
    "2020": {
        "winner_driver": "Lewis Hamilton",
        "winner_team": "Mercedes",
        "highlights": "COVID-19 단축 시즌, Hamilton의 7번째 타이틀",
        "tech": "DAS 시스템, 하이브리드 효율성",
        "highlight_video": "https://www.youtube.com/watch?v=example2020",
        "tech_detail": "Mercedes는 DAS(Dual Axis Steering) 시스템을 도입하여 타이어 온도를 능동적으로 조절하며 퍼포먼스를 유지했습니다."
    }
}

st.set_page_config(page_title="F1 시즌별 드라이버 팀 분석", layout="wide")

# 라우팅 조건
page = st.session_state.page
selected_season = st.session_state.season
selected_driver = st.session_state.driver
selected_team = st.session_state.team

# 메인 페이지
if page == "main":
    st.title("F1 시즌별 드라이버 팀 분석")
    season = st.selectbox("시즌 선택", sorted(f1_data.keys(), reverse=True))
    if st.button("선택한 시즌 보기"):
        st.session_state.page = "season"
        st.session_state.season = season

# 시즌 상세
elif page == "season" and selected_season:
    season_data = f1_data[selected_season]
    st.title(f"{selected_season} 시즌 분석")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("우승 드라이버")
        driver_name = season_data["winner_driver"]
        if st.button(f"{driver_name} 드라이버 이력 보기"):
            st.session_state.page = "driver"
            st.session_state.driver = driver_name
        st.image(driver_history[driver_name]["image"], width=300)
    with col2:
        st.subheader("우승 팀")
        team_name = season_data["winner_team"]
        if st.button(f"{team_name} 팀 이력 보기"):
            st.session_state.page = "team"
            st.session_state.team = team_name
        st.image(team_history[team_name]["logo"], width=300)

    st.markdown("---")
    st.subheader("🎯 시즌 관전 포인트")
    if st.button("관전 포인트 하이라이트 영상 보기"):
        st.video(season_data["highlight_video"])
    st.write(season_data["highlights"])

    st.subheader("🔧 기술 트렌드")
    if st.button("해당 기술 설명 보기"):
        st.write(season_data["tech_detail"])
    st.write(season_data["tech"])

    st.subheader("📊 드라이버 순위")
    st.write(f"🥇 {season_data['winner_driver']}")

    st.subheader("🏁 팀 순위")
    st.write(f"🥇 {season_data['winner_team']}")

    if st.button("🏠 메인으로 돌아가기"):
        st.session_state.page = "main"
        st.session_state.season = None
        st.session_state.driver = None
        st.session_state.team = None

# 드라이버 상세
elif page == "driver" and selected_driver:
    data = driver_history[selected_driver]
    st.title(f"{selected_driver} 드라이버 이력")
    st.image(data["image"], width=300)
    for k, v in data.items():
        if k not in ["image", "seasons"]:
            st.markdown(f"### {k}: {v}")

    st.subheader("📈 시즌별 챔피언십 순위")
    df = pd.DataFrame({"Season": list(data["seasons"].keys()), "Ranking": list(data["seasons"].values())})
    df = df.sort_values("Season")
    df["Ranking"] = df["Ranking"].astype(int)
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(df["Season"], df["Ranking"], marker="o", linestyle='-', color='blue', label="드라이버 순위")
    for i, txt in enumerate(df["Ranking"]):
        ax.annotate(txt, (df["Season"].iloc[i], df["Ranking"].iloc[i]), textcoords="offset points", xytext=(0, -10), ha='center')
    ax.invert_yaxis()
    ax.set_title("챔피언십 순위 추이 (낮을수록 좋음)")
    ax.set_xlabel("시즌")
    ax.set_ylabel("순위")
    ax.legend()
    st.pyplot(fig)

    if st.button("🏠 메인으로 돌아가기"):
        st.session_state.page = "main"
        st.session_state.driver = None

# 팀 상세
elif page == "team" and selected_team:
    data = team_history[selected_team]
    st.title(f"{selected_team} 팀 이력")
    st.image(data["logo"], width=300)
    for k, v in data.items():
        if k not in ["logo", "seasons"]:
            st.markdown(f"### {k}: {v}")

    st.subheader("📈 시즌별 챔피언십 순위")
    df = pd.DataFrame({"Season": list(data["seasons"].keys()), "Ranking": list(data["seasons"].values())})
    df = df.sort_values("Season")
    df["Ranking"] = df["Ranking"].astype(int)
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(df["Season"], df["Ranking"], marker="s", linestyle='-', color='orange', label="팀 순위")
    for i, txt in enumerate(df["Ranking"]):
        ax.annotate(txt, (df["Season"].iloc[i], df["Ranking"].iloc[i]), textcoords="offset points", xytext=(0, -10), ha='center')
    ax.invert_yaxis()
    ax.set_title("팀 순위 추이 (낮을수록 좋음)")
    ax.set_xlabel("시즌")
    ax.set_ylabel("순위")
    ax.legend()
    st.pyplot(fig)

    if st.button("🏠 메인으로 돌아가기"):
        st.session_state.page = "main"
        st.session_state.team = None
