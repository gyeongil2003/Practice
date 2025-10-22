# Streamlit MBTI → Career Recommender (K-12 Career Education)
# ----------------------------------------------------------
# How to run locally:
#   1) pip install streamlit
#   2) streamlit run streamlit_mbti_career_app.py
#
# This app is designed for school career education. It uses colorful UI, emoji-rich visuals, 
# practical study tips, and downloadable results for students.

import streamlit as st
from datetime import datetime
import textwrap

st.set_page_config(
    page_title="MBTI 진로 추천 • Spark!",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ------------------------------
# Custom CSS for a vibrant look
# ------------------------------
ACCENT_GRADIENT = "linear-gradient(135deg, #7C3AED 0%, #22D3EE 50%, #F472B6 100%)"
CARD_BG = "rgba(255, 255, 255, 0.75)"
DARK_CARD_BG = "rgba(20, 20, 20, 0.55)"
BORDER = "rgba(255,255,255,0.5)"

st.markdown(
    f"""
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Pretendard:wght@400;600;800&family=Nunito:wght@600;800&display=swap');
      html, body, [class*="css"]  {{
        font-family: 'Pretendard', 'Nunito', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, 'Apple SD Gothic Neo', 'Noto Sans KR', 'Malgun Gothic', 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol';
      }}
      .hero {{
        padding: 24px 28px; border-radius: 22px; color: #111;
        background: {ACCENT_GRADIENT};
        box-shadow: 0 10px 30px rgba(0,0,0,0.08);
      }}
      .subtitle {{ opacity: 0.9; font-weight: 600; }}
      .card {{
        background: {CARD_BG};
        border: 1px solid {BORDER};
        border-radius: 18px;
        padding: 18px 18px 16px 18px;
        box-shadow: 0 12px 30px rgba(0,0,0,0.06);
        backdrop-filter: blur(6px);
      }}
      .dark .card {{ background: {DARK_CARD_BG}; border-color: rgba(255,255,255,0.15); }}
      .tag {{
        display:inline-block; padding:6px 10px; margin: 2px 6px 4px 0; border-radius: 999px;
        background: rgba(124, 58, 237, 0.14); border:1px solid rgba(124,58,237,0.25);
        font-weight: 700; font-size: 0.88rem;
      }}
      .chip {{
        display:inline-flex; align-items:center; gap:6px; padding:8px 12px; border-radius:14px;
        border:1px dashed rgba(0,0,0,0.1); margin: 4px 8px 0 0; background: rgba(255,255,255,0.6);
      }}
      .muted {{ opacity: 0.7; }}
      .emoji-title {{ font-size: 1.1rem; font-weight: 800; }}
      .footer-note {{ font-size: 0.9rem; opacity: 0.75; }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------------------
# Data
# ------------------------------
MBTI_INFO = {
    "INTJ": {
        "title": "INTJ – 전략가 🧠🗺️",
        "traits": ["분석적", "독립적", "장기계획", "혁신 추구"],
        "careers": [
            ("데이터 과학자", "📊"),
            ("AI 연구원", "🤖"),
            ("전략 컨설턴트", "🧭"),
            ("제품 매니저(PM)", "📌"),
            ("도시/교통 계획가", "🏙️"),
        ],
        "study": ["수학·통계", "컴퓨터 과학", "경제/경영", "시스템 사고"],
        "activities": ["데이터 분석 프로젝트", "문제 해결 챌린지", "장기 로드맵 설계"]
    },
    "INTP": {
        "title": "INTP – 아이디어 메이커 🧪💡",
        "traits": ["논리적", "탐구적", "호기심", "이론화"],
        "careers": [
            ("연구개발(R&D)", "🔬"),
            ("백엔드 개발자", "🧩"),
            ("알고리즘 엔지니어", "📐"),
            ("기술 분석가", "🛠️"),
            ("게임 엔진 개발자", "🎮"),
        ],
        "study": ["수학·물리", "컴퓨터 과학", "논리학", "철학"],
        "activities": ["과학 탐구 대회", "오픈소스 기여", "문제해결 피드"]
    },
    "ENTJ": {
        "title": "ENTJ – 지휘관 🧭👩‍✈️",
        "traits": ["리더십", "목표 지향", "의사결정", "전략적"],
        "careers": [
            ("기업가/스타트업 리더", "🚀"),
            ("프로덕트 매니저", "📌"),
            ("경영 컨설턴트", "📈"),
            ("프로젝트 매니저", "📅"),
            ("세일즈 디렉터", "🤝"),
        ],
        "study": ["경영/경제", "리더십", "데이터 리터러시", "프레젠테이션"],
        "activities": ["모의창업", "캡스톤 프로젝트 리딩", "디베이트"]
    },
    "ENTP": {
        "title": "ENTP – 발명가 ⚙️✨",
        "traits": ["창의", "즉흥", "도전", "토론"],
        "careers": [
            ("프로덕트 디자이너", "🎨"),
            ("UX 전략가", "🧭"),
            ("혁신 컨설턴트", "🧪"),
            ("VC/스타트업 스카우트", "💼"),
            ("크리에이터/콘텐츠 기획", "🎥"),
        ],
        "study": ["디자인 씽킹", "마케팅", "프로토타이핑", "스토리텔링"],
        "activities": ["해커톤", "피치 데크 경진대회", "디자인 챌린지"]
    },
    "INFJ": {
        "title": "INFJ – 옹호자 🌿🔮",
        "traits": ["통찰", "가치지향", "공감", "미래지향"],
        "careers": [
            ("상담/심리", "🗣️"),
            ("교육/교사", "🏫"),
            ("사회정책 기획", "🏛️"),
            ("콘텐츠 작가", "✍️"),
            ("브랜드 스토리 전략가", "📖"),
        ],
        "study": ["심리학", "교육학", "문학/철학", "사회학"],
        "activities": ["봉사 프로젝트", "다큐 해석 토론", "멘토링"]
    },
    "INFP": {
        "title": "INFP – 이상가 🌈🕊️",
        "traits": ["창의", "가치", "자율", "표현"],
        "careers": [
            ("작가/시나리오", "📚"),
            ("일러스트레이터", "🖌️"),
            ("사회적기업 기획", "🤝"),
            ("콘텐츠 마케터", "📣"),
            ("게임 스토리 디자이너", "🧙‍♂️"),
        ],
        "study": ["문학", "언어", "미학", "미디어"],
        "activities": ["창작 워크숍", "독서 토론", "인디 프로젝트"]
    },
    "ENFJ": {
        "title": "ENFJ – 교사형 🌟🤗",
        "traits": ["조직", "격려", "커뮤니케이션", "비전"],
        "careers": [
            ("교사/교육기획", "🏫"),
            ("HRD/러닝 디자이너", "🧩"),
            ("커뮤니티 매니저", "🫶"),
            ("PR/브랜드 커뮤니케이션", "📢"),
            ("비영리 프로젝트 리더", "🕊️"),
        ],
        "study": ["교육학", "커뮤니케이션", "조직심리", "행정"],
        "activities": ["캠페인 기획", "멘토링", "대외활동 리드"]
    },
    "ENFP": {
        "title": "ENFP – 캠페이너 🎉🚀",
        "traits": ["열정", "아이디어", "관계", "도전"],
        "careers": [
            ("크리에이티브 디렉터", "🎬"),
            ("브랜드 마케터", "📣"),
            ("프로덕트 에반젤리스트", "🗯️"),
            ("행사/이벤트 기획", "🎪"),
            ("에듀테크 PM", "💡"),
        ],
        "study": ["마케팅", "미디어", "교육공학", "창업"],
        "activities": ["영상/음성 콘텐츠 제작", "해커톤", "홍보 캠페인"]
    },
    "ISTJ": {
        "title": "ISTJ – 관리자 🗂️🧱",
        "traits": ["책임감", "정확성", "체계", "성실"],
        "careers": [
            ("회계/재무", "💼"),
            ("품질관리(QA)", "🔎"),
            ("공공행정", "🏛️"),
            ("보건/의무기록", "🩺"),
            ("인프라 엔지니어", "🖧"),
        ],
        "study": ["회계", "법/행정", "데이터 관리", "통계"],
        "activities": ["문서 자동화", "절차 개선 프로젝트", "감사 시뮬"]
    },
    "ISFJ": {
        "title": "ISFJ – 수호자 🛡️🌷",
        "traits": ["배려", "책임", "세심함", "협력"],
        "careers": [
            ("간호/보건", "🩺"),
            ("교무/교육행정", "📚"),
            ("서비스 운영", "🧾"),
            ("아동발달/복지", "🧸"),
            ("문서/기록 아카이브", "📁"),
        ],
        "study": ["보건", "교육", "행정", "문서관리"],
        "activities": ["돌봄 봉사", "행사 운영", "매뉴얼 제작"]
    },
    "ESTJ": {
        "title": "ESTJ – 실행가 🧱🚦",
        "traits": ["실용", "조직", "결단", "관리"],
        "careers": [
            ("프로덕션 매니저", "🏭"),
            ("운영 관리자", "⚙️"),
            ("재무/예산 기획", "💹"),
            ("공기업/공공기관", "🏛️"),
            ("세일즈 매니저", "🧾"),
        ],
        "study": ["경영", "회계", "산업공학", "프로세스"],
        "activities": ["워크플로우 개선", "프로젝트 일정관리", "원가분석"]
    },
    "ESFJ": {
        "title": "ESFJ – 사교가 🎀🤝",
        "traits": ["협업", "서비스", "질서", "공감"],
        "careers": [
            ("HR/채용", "🧑‍🤝‍🧑"),
            ("고객성공(CSM)", "💟"),
            ("교육 코디네이터", "🗓️"),
            ("이벤트 운영", "🎉"),
            ("의료 코디네이터", "🏥"),
        ],
        "study": ["커뮤니케이션", "조직행동", "심리", "서비스 디자인"],
        "activities": ["동아리/행사 운영", "서비스 개선 설문", "멘토링"]
    },
    "ISTP": {
        "title": "ISTP – 장인 🔧🧲",
        "traits": ["분석", "손기술", "문제해결", "실험"],
        "careers": [
            ("하드웨어 엔지니어", "💡"),
            ("보안/리버스 엔지", "🛡️"),
            ("드론/로보틱스", "🚁"),
            ("메카트로닉스", "🤖"),
            ("데브옵스/사이트 신뢰성", "🖥️"),
        ],
        "study": ["전자", "기계", "컴퓨터", "보안"],
        "activities": ["메이커톤", "로봇 키트 제작", "IoT 실습"]
    },
    "ISFP": {
        "title": "ISFP –
