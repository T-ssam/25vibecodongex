import streamlit as st

# 📘 MBTI별 전공 학과 추천
mbti_majors = {
    "INTJ": ["📊 산업공학과", "🧠 인공지능학과", "📈 경영정보학과"],
    "INTP": ["🔬 물리학과", "💻 컴퓨터공학과", "📐 수학과"],
    "ENTJ": ["📈 경영학과", "📊 경제학과", "🏛️ 행정학과"],
    "ENTP": ["📰 미디어커뮤니케이션학과", "💡 창의공학부", "🎮 콘텐츠IT학과"],
    "INFJ": ["🧘 상담심리학과", "🌱 사회복지학과", "📚 교육학과"],
    "INFP": ["🎨 시각디자인학과", "📖 국어국문학과", "🎭 연극영화과"],
    "ENFJ": ["👨‍🏫 교육학과", "🗣️ 커뮤니케이션학과", "👥 청소년지도학과"],
    "ENFP": ["🎤 공연예술학과", "📸 방송영상학과", "🌍 관광학과"],
    "ISTJ": ["📂 회계학과", "⚖️ 법학과", "📐 토목공학과"],
    "ISFJ": ["👩‍⚕️ 간호학과", "📑 행정학과", "🧵 패션산업학과"],
    "ESTJ": ["📊 경영학과", "🔧 기계공학과", "📈 세무회계학과"],
    "ESFJ": ["👩‍🏫 유아교육과", "🍽️ 외식경영학과", "👨‍👩‍👧‍👦 가족복지학과"],
    "ISTP": ["🚗 자동차공학과", "🛠️ 로봇공학과", "🎮 게임소프트웨어학과"],
    "ISFP": ["🎨 디자인학과", "🎶 음악학과", "🌸 원예학과"],
    "ESTP": ["📢 마케팅학과", "🎬 광고홍보학과", "🛠️ 산업디자인학과"],
    "ESFP": ["🎤 연극영화과", "📸 실용음악과", "🍳 호텔조리학과"]
}

# 🌟 페이지 설정
st.set_page_config(page_title="🎓 MBTI 학과 추천기", page_icon="📚", layout="centered")

# ✨ 타이틀
st.markdown("""
    <div style='text-align: center; padding: 20px 0;'>
        <h1 style='font-size: 3em; color: #0984e3;'>🎓 MBTI 기반 학과 추천기 🧠</h1>
        <h4>성격에 딱 맞는 전공을 찾아보세요! ✨</h4>
    </div>
""", unsafe_allow_html=True)

# 🧭 MBTI 선택
st.markdown("### 👉 당신의 MBTI를 선택해보세요!")
selected_mbti = st.selectbox("📌 MBTI 유형", list(mbti_majors.keys()))

# 📋 추천 학과 표시
if selected_mbti:
    st.markdown(f"## 📚 {selected_mbti} 유형에게 어울리는 전공")
    st.markdown("### ✅ 아래 전공들을 고려해보세요:")
    majors = mbti_majors[selected_mbti]

    for i, major in enumerate(majors, 1):
        st.markdown(f"**{i}. {major}**")

    st.success("📘 자신에게 맞는 학과를 탐색해보는 것은 멋진 첫 걸음이에요!")

# 푸터
st.markdown("""
    <hr>
    <div style='text-align:center; font-size: 16px;'>
        📖 진로 설계 플랫폼 • MBTI 전공 추천기<br>
        Made with 💙 by AI Assistant
    </div>
""", unsafe_allow_html=True)
