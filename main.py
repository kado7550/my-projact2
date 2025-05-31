import streamlit as st

st.title("MBTI 기반 직업 추천기")

mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

mbti = st.selectbox("당신의 MBTI 유형을 선택하세요:", mbti_types)

mbti_jobs = {
    "ISTJ": ["회계사", "경찰관", "판사"],
    "ISFJ": ["간호사", "교사", "사회복지사"],
    "INFJ": ["심리상담사", "작가", "교수"],
    "INTJ": ["전략기획가", "데이터 분석가", "과학자"],
    "ISTP": ["엔지니어", "파일럿", "정비사"],
    "ISFP": ["디자이너", "예술가", "물리치료사"],
    "INFP": ["작가", "예술가", "심리상담사"],
    "INTP": ["연구원", "개발자", "이론물리학자"],
    "ESTP": ["기업가", "세일즈 매니저", "스포츠 선수"],
    "ESFP": ["이벤트 플래너", "배우", "가수"],
    "ENFP": ["마케팅 전문가", "기획자", "카피라이터"],
    "ENTP": ["벤처 창업가", "변호사", "광고 전문가"],
    "ESTJ": ["군인", "경영 관리자", "프로젝트 매니저"],
    "ESFJ": ["HR 매니저", "교사", "간호사"],
    "ENFJ": ["멘토", "리더십 트레이너", "사회운동가"],
    "ENTJ": ["CEO", "변호사", "전략 컨설턴트"]
}

if mbti in mbti_jobs:
    st.subheader(f"{mbti} 유형에게 추천되는 직업:")
    for job in mbti_jobs[mbti]:
        st.write(f"- {job}")
