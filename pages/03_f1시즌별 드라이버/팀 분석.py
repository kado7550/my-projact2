import streamlit as st

# 샘플 데이터 (실제 앱에서는 이 부분을 데이터베이스나 API와 연동 가능)
f1_data = {
    "2021": {
        "winner_driver": "Max Verstappen",
        "winner_team": "Red Bull Racing",
        "highlights": "Verstappen vs Hamilton 대결, 마지막 경기에서 역전 우승",
        "tech": "하이 레이크(Rake) 컨셉, 공기역학 업그레이드",
        "driver_history": {
            "Max Verstappen": {
                "World Championships": 3,
                "Wins": 60,
                "Podiums": 90,
                "Debut": "2015"
            }
        },
        "team_history": {
            "Red Bull Racing": {
                "World Championships": 6,
                "Wins": 120,
                "Debut": "2005"
            }
        }
    },
    "2020": {
        "winner_driver": "Lewis Hamilton",
        "winner_team": "Mercedes",
        "highlights": "COVID-19 팬데믹 시즌, Hamilton의 지배적인 우승",
        "tech": "DAS 시스템 (Dual Axis Steering)",
        "driver_history": {
            "Lewis Hamilton": {
                "World Championships": 7,
                "Wins": 103,
                "Podiums": 195,
                "Debut": "2007"
            }
        },
        "team_history": {
            "Mercedes": {
                "World Championships": 8,
                "Wins": 115,
                "Debut": "1954"
            }
        }
    }
}

# 앱 시작
st.title("🏎️ 시즌별 드라이버/팀 순위 분석")

# 시즌 선택
season = st.selectbox("시즌을 선택하세요", sorted(f1_data.keys(), reverse=True))

if st.button("해당 시즌 분석 보기"):
    data = f1_data[season]
    st.subheader(f"🏁 {season} 시즌 결과")
    
    # 우승자와 우승팀 표시
    driver_col, team_col = st.columns(2)
    
    with driver_col:
        if st.button(f"드라이버 우승자: {data['winner_driver']}"):
            driver_stats = data["driver_history"][data["winner_driver"]]
            st.markdown(f"**{data['winner_driver']} 역대 성적**")
            st.json(driver_stats)

    with team_col:
        if st.button(f"컨스트럭터 우승팀: {data['winner_team']}"):
            team_stats = data["team_history"][data["winner_team"]]
            st.markdown(f"**{data['winner_team']} 팀의 역대 성적**")
            st.json(team_stats)

    # 관전 포인트와 기술 요소
    st.markdown("### 🎯 관전 포인트")
    st.write(data["highlights"])

    st.markdown("### 🔧 대표적인 기술")
    st.write(data["tech"])
