import streamlit as st

# 앱 제목
st.title("오늘의 저녁으은?")

# 세션 상태 초기화
if "submitted" not in st.session_state:
    st.session_state.submitted = False

# 질문 항목 (라디오 버튼)
q1 = st.radio("1. 오늘의 기분은?", ["가볍게", "든든하게", "빠르게"])
q2 = st.radio("2. 혼자 먹나요?", ["혼자", "여럿이"])
q3 = st.radio("3. 매운 음식 좋아하시나요?", ["좋아함", "보통", "안 좋아함"])
q4 = st.radio("4. 국물 있는 게 좋으신가요?", ["네", "아니오"])
q5 = st.radio("5. 식사 시간은 얼마나 있나요?", ["짧다", "여유 있다"])
q6 = st.radio("6. 식사 예산은?", ["저렴하게", "중간", "조금 사치"])
q7 = st.radio("7. 건강을 우선하시나요?", ["네", "아니오"])
q8 = st.radio("8. 특별히 먹고 싶은 재료가 있나요?", ["고기", "채소", "해산물", "상관없음"])

# 제출 버튼
if st.button("오늘의 메뉴 추천받기"):
    st.session_state.submitted = True

# 결과 출력
if st.session_state.submitted:
    # 간단한 로직 (조건 몇 개 조합)
    if q3 == "좋아함" and q4 == "네":
        menu = "매운 김치찌개 🍲"
    elif q1 == "빠르게" and q2 == "혼자":
        menu = "편의점 도시락 🍱"
    elif q8 == "고기":
        menu = "삼겹살 구이 🥩"
    elif q8 == "해산물":
        menu = "초밥 세트 🍣"
    elif q8 == "채소":
        menu = "비빔밥 🥗"
    else:
        menu = "치킨 🍗"

    # 학습 유형(성향) 설명
    if q7 == "네":
        style = "건강을 중요시하는 타입이군요! 🥦"
    else:
        style = "맛과 분위기를 더 중시하는 타입이시네요! 🍻"

    st.subheader("✨ 오늘 저녁 추천 ✨")
    st.write(f"👉 추천 메뉴: **{menu}**")
    st.write(f"👉 성향 분석: {style}")
