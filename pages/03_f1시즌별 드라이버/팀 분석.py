import streamlit as st
import matplotlib.pyplot as plt

# 드라이버 데이터
driver_history = {
    "Max Verstappen": {
        "World Championships": 4,
        "Wins": 70,
        "Podiums": 100,
        "Debut": "2015",
        "image": "https://upload.wikimedia.org/wikipedia/commons/8/88/Max_Verstappen_2017_Malaysia_3.jpg",
        "seasons": {
            "2020": 2, "2021": 1, "2022": 1, "2023": 1, "2024": 1
        }
    },
    "Lewis Hamilton": {
        "World Championships": 7,
        "Wins": 103,
        "Podiums": 195,
        "Debut": "2007",
        "image": "https://upload.wikimedia.org/wikipedia/commons/2/2e/Lewis_Hamilton_2016_Malaysia_3.jpg",
        "seasons": {
            "2020": 1, "2021": 2
        }
    }
}

# 팀 데이터
team_history = {
    "Red Bull Racing": {
        "World Championships": 6,
        "Wins": 113,
        "Debut": "2005",
        "logo": "https://upload.wikimedia.org/wikipedia/en/thumb/6/6e/Red_Bull_Racing_logo.svg/320px-Red_Bull_Racing_logo.svg.png",
        "seasons": {
            "2022": 1, "2023": 1
        }
    },
    "Mercedes": {
        "World Championships": 8,
        "Wins": 125,
        "Debut": "1954",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/Mercedes-Benz_in_Formula_One_logo.svg/320px-Mercedes-Benz_in_Formula_One_logo.svg.png",
        "seasons": {
            "2020": 1, "2021": 1
        }
    },
    "McLaren": {
        "World Championships": 9,
        "Wins": 183,
        "Debut": "1966",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/McLaren_Racing_logo.svg/320px-McLaren_Racing_logo.svg.png",
        "seasons": {
            "2024": 1
        }
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
        "highlights": "Ferrari와 치열한 경쟁 끝에 우승",
        "tech": "18인치 타이어와 그라운드 이펙트 적용",
    },
    "2021": {
        "winner_driver": "Max Verstappen",
        "winner_team": "Mercedes",
        "highlights": "Verstappen vs Hamilton의 역사적 시즌",
        "tech": "고속 코너링 설계, 세트업 전쟁",
    },
    "2020": {
        "winner_driver": "Lewis Hamilton",
        "winner_team": "Mercedes",
        "highlights": "COVID-19 단축 시즌, Hamilton의 7번째 타이틀",
        "tech": "DAS 시스템, 하이브리드 효율성",
    }
}

# 페이지 구성
st.set_page_config(page_title="F1 시즌별 드라이버 팀 분석", layout="wide")

# 페이지 라우팅
page = st.experimental_get_query_params().get("page", ["main"])[0]
selected_season = st.experimental_get_query_params().get("season", [None])[0]
selected_driver = st.experimental_get_query_params().get("driver", [None])[0]
selected_team = st.experimental_get_query_params().get("team", [None])[0]

# 메인 페이지
if page == "main":
    st.title("F1 시즌별 드라이버 팀 분석")
    season = st.selectbox("시즌 선택", sorted(f1_data.keys(), reverse=True))
    if st.button("선택한 시즌 보기"):
        st.experimental_set_query_params(page="season", season=season)
        st.experimental_rerun()

# 시즌 상세 페이지
elif page == "season" and selected_season:
    season_data = f1_data[selected_season]
    st.title(f"{selected_season} 시즌 분석")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("우승 드라이버")
        driver_name = season_data["winner_driver"]
        st.markdown(f"### [{driver_name}](?page=driver&driver={driver_name})")
        st.image(driver_history[driver_name]["image"], width=300)
    with col2:
        st.subheader("우승 팀")
        team_name = season_data["winner_team"]
        st.markdown(f"### [{team_name}](?page=team&team={team_name})")
        st.image(team_history[team_name]["logo"], width=300)

    st.markdown("---")
    st.subheader("🎯 시즌 관전 포인트")
    st.write(season_data["highlights"])

    st.subheader("🔧 기술 트렌드")
    st.write(season_data["tech"])

    st.markdown("[🏠 메인으로 돌아가기](?page=main)")

# 드라이버 상세 페이지
elif page == "driver" and selected_driver:
    data = driver_history[selected_driver]
    st.title(f"{selected_driver} 드라이버 이력")
    st.image(data["image"], width=300)
    st.write({k: v for k, v in data.items() if k not in ["image", "seasons"]})

    st.subheader("📈 시즌별 챔피언십 순위")
    seasons = list(data["seasons"].keys())
    rankings = list(data["seasons"].values())

    fig, ax = plt.subplots()
    ax.plot(seasons, rankings, marker='o', linestyle='-')
    ax.invert_yaxis()
    ax.set_title("챔피언십 순위 추이 (낮을수록 좋음)")
    ax.set_xlabel("시즌")
    ax.set_ylabel("순위")
    st.pyplot(fig)

    st.markdown("[🏠 메인으로 돌아가기](?page=main)")

# 팀 상세 페이지
elif page == "team" and selected_team:
    data = team_history[selected_team]
    st.title(f"{selected_team} 팀 이력")
    st.image(data["logo"], width=300)
    st.write({k: v for k, v in data.items() if k not in ["logo", "seasons"]})

    st.subheader("📈 시즌별 챔피언십 순위")
    seasons = list(data["seasons"].keys())
    rankings = list(data["seasons"].values())

    fig, ax = plt.subplots()
    ax.plot(seasons, rankings, marker='s', linestyle='-', color='orange')
    ax.invert_yaxis()
    ax.set_title("팀 순위 추이 (낮을수록 좋음)")
    ax.set_xlabel("시즌")
    ax.set_ylabel("순위")
    st.pyplot(fig)

    st.markdown("[🏠 메인으로 돌아가기](?page=main)")



