import streamlit as st
import folium
from streamlit.components.v1 import html

# 여행지 데이터 (예시로 10곳)
places = [
    {"name": "서울", "lat": 37.5665, "lon": 126.9780, "desc": "대한민국의 수도, 전통과 현대의 조화"},
    {"name": "부산", "lat": 35.1796, "lon": 129.0756, "desc": "해운대와 광안리 해변이 유명한 해양 도시"},
    {"name": "제주도", "lat": 33.4996, "lon": 126.5312, "desc": "자연의 아름다움과 독특한 풍경의 섬"},
    {"name": "경주", "lat": 35.8562, "lon": 129.2247, "desc": "천년의 역사, 신라의 고도"},
    {"name": "강릉", "lat": 37.7519, "lon": 128.8761, "desc": "동해안의 맑은 바다와 커피거리"},
    {"name": "인천", "lat": 37.4563, "lon": 126.7052, "desc": "차이나타운과 송도 센트럴파크가 인기"},
    {"name": "속초", "lat": 38.2044, "lon": 128.5912, "desc": "설악산과 바다, 자연이 어우러진 도시"},
    {"name": "남해", "lat": 34.8370, "lon": 127.8924, "desc": "바다를 끼고 드라이브하기 좋은 곳"},
    {"name": "전주", "lat": 35.8242, "lon": 127.1480, "desc": "한옥마을과 맛의 도시"},
    {"name": "안동", "lat": 36.5684, "lon": 128.7294, "desc": "하회마을로 유명한 전통의 본고장"},
]

# 지도 생성
m = folium.Map(location=[36.5, 127.8], zoom_start=7)

# 마커 추가
for place in places:
    folium.Marker(
        location=[place["lat"], place["lon"]],
        popup=f"<b>{place['name']}</b><br>{place['desc']}",
        icon=folium.Icon(color="pink", icon="heart", prefix='fa')
    ).add_to(m)

# HTML 지도 저장
m.save("map.html")

# Streamlit 앱 구성
st.markdown("<h1 style='text-align: center; color: #ff69b4;'>💖 한국인이 사랑하는 TOP 10 여행지 💖</h1>", unsafe_allow_html=True)

# 지도를 HTML로 삽입
with open("map.html", 'r', encoding='utf-8') as f:
    map_html = f.read()
html(map_html, height=600)

# 간단한 설명
st.markdown("여행지는 아름다운 추억의 시작이에요. 🌸 <br> 아래는 추천 여행지 목록입니다!", unsafe_allow_html=True)

# 여행지 리스트 출력
for place in places:
    st.markdown(f"### 📍 {place['name']}")
    st.markdown(f"**{place['desc']}**")
