# 🎯 MBTI 진로 추천 웹앱 – Spark!
# 실행 방법:
#   1. pip install streamlit
#   2. streamlit run streamlit_mbti_career_app.py

import streamlit as st
from datetime import datetime
import textwrap

st.set_page_config(
    page_title="MBTI 진로 추천 • Spark!",
    page_icon="✨",
    layout="wide"
)

# ------------------------------
# 🌈 스타일
# ------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Pretendard:wght@400;700;900&display=swap');
html, body, [class*="css"] {
    font-family: 'Pretendard', sans-serif;
}
.hero {
    background: linear-gradient(135deg, #9333EA, #3B82F6, #EC4899);
    color: white;
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.15);
}
.card {
    background: rgba(255,255,255,0.8);
    border-radius: 16px;
    padding: 18px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
    margin-bottom: 12px;
}
.tag {
    display:inline-block;
    padding:6px 10px;
    margin:4px;
    background:rgba(59,130,246,0.1);
    border-radius:10px;
    font-weight:600;
}
</style>
""", unsafe_allow_html=True)

# ------------------------------
# 🧩 MBTI 데이터
# ------------------------------
MBTI_INFO = {
    "INTJ": {
        "title": "INTJ – 전략가 🧠🗺️",
        "traits": ["분석적", "독립적", "계획적", "혁신적"],
        "careers": ["데이터 과학자", "AI 연구원", "전략 컨설턴트", "도시 계획가", "제품 매니저"],
        "study": ["수학", "통계", "컴퓨터 과학", "경제"],
        "activities": ["데이터 분석 프로젝트", "문제 해결 경진대회", "장기 로드맵 설계"]
    },
    "INFP": {
        "title": "INFP – 이상가 🌈🕊️",
        "traits": ["창의적", "가치중심", "감성적", "자율적"],
        "careers": ["작가", "디자이너", "사회적 기업가", "마케터", "스토리텔러"],
        "study": ["문학", "심리학", "예술", "미디어"],
        "activities": ["창작 워크숍", "독서 토론", "사회 캠페인"]
    },
    "ENTP": {
        "title": "ENTP – 발명가 ⚙️💡",
        "traits": ["창의적", "도전적", "논리적", "즉흥적"],
        "careers": ["혁신 컨설턴트", "제품 디자이너", "크리에이터", "스타트업 창업자", "마케팅 전략가"],
        "study": ["디자인", "마케팅", "기술 창업", "스토리텔링"],
        "activities": ["해커톤", "피치데크 경진대회", "디자인 챌린지"]
    },
    "ISFP": {
        "title": "ISFP – 예술가 🎨🍃",
        "traits": ["감성적", "예술적", "자유로움", "조용한 헌신"],
        "careers": ["그래픽 디자이너", "사진작가", "영상편집자", "공예가", "UI 디자이너"],
        "study": ["시각디자인", "색채학", "미디어", "미학"],
        "activities": ["포트폴리오 제작", "스케치북 일기", "브랜딩 실습"]
    },
    "ENFP": {
        "title": "ENFP – 캠페이너 🎉🚀",
        "traits": ["열정적", "사교적", "아이디어 풍부", "자유로움"],
        "careers": ["마케터", "콘텐츠 기획자", "에듀테크 PM", "홍보 전문가", "이벤트 플래너"],
        "study": ["미디어", "교육공학", "마케팅", "창업"],
        "activities": ["홍보 캠페인 기획", "해커톤 참가", "영상 제작"]
    }
}

ALL_TYPES = list(MBTI_INFO.keys())

# ------------------------------
# 🎨 헤더
# ------------------------------
st.markdown(f"""
<div class='hero'>
    <h1>✨ MBTI 진로 추천 • Spark!</h1>
    <h3>나의 성향에 딱 맞는 미래 직업을 찾아보자 🔍</h3>
    <p>자기이해 • 진로탐색 • 학습전략 • 프로젝트 아이디어</p>
</div>
""", unsafe_allow_html=True)

st.write("")

# ------------------------------
# 🎯 선택 영역
# ------------------------------
col1, col2 = st.columns(2)
with col1:
    mbti = st.selectbox("👉 MBTI 유형을 선택하세요", ALL_TYPES, index=0)
with col2:
    goal = st.text_input("🌟 관심 있는 진로 분야 (선택)", placeholder="예: 개발자, 디자이너, 교사, 창업가...")

info = MBTI_INFO[mbti]

# ------------------------------
# 💼 결과 카드
# ------------------------------
st.markdown(f"""
<div class='card'>
<h2>{info['title']}</h2>
<p><b>핵심 성향:</b> {' · '.join(info['traits'])}</p>
{f"<p><b>관심 분야:</b> {goal}</p>" if goal else ""}
</div>
""", unsafe_allow_html=True)

col3, col4 = st.columns(2)
with col3:
    st.markdown("### 💼 추천 직업")
    for job in info["careers"]:
        st.markdown(f"- {job}")

with col4:
    st.markdown("### 📚 추천 학습/활동")
    st.markdown("**추천 과목**: " + ", ".join(info["study"]))
    st.markdown("**활동 아이디어**: " + ", ".join(info["activities"]))

# ------------------------------
# 💡 학습 루틴
# ------------------------------
with st.expander("💡 4주 진로 탐색 루틴 보기"):
    st.markdown("""
    **1주차**: 관심 분야 조사 및 키워드 정리 🔎  
    **2주차**: 관련 실습/체험 활동 🧪  
    **3주차**: 포트폴리오/발표 준비 📘  
    **4주차**: 피드백 받고 계획 보완하기 🧭
    """)

# ------------------------------
# 📥 다운로드
# ------------------------------
plan = textwrap.dedent(f"""
[MBTI 진로 추천 결과]
유형: {mbti} ({info['title']})
관심 분야: {goal or '미입력'}

핵심 성향: {', '.join(info['traits'])}
추천 직업: {', '.join(info['careers'])}
추천 과목: {', '.join(info['study'])}
활동 아이디어: {', '.join(info['activities'])}
""")

st.download_button("📥 내 진로 추천 결과 저장하기", data=plan, file_name=f"{mbti}_진로추천.txt")

st.snow()
