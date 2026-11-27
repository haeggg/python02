# 1. 기본 환경 및 모듈 임포트 > 1, 2번

import pandas as pd
import streamlit as st

from pathlib import Path
from common import parse_sales, summarize


# 1. 기본 환경 및 모듈 임포트 > 3번

st.set_page_config(page_title="미니 POS & 매출 분석기", layout="wide")


# 1. 기본 환경 및 모듈 임포트 > 4번

st.title("🏪올인원 미니 POS & 매출 분석기")
st.write("**학습 목료** : 입력('form'), 상태 유지('session_state'), 캐싱('cache_data'), 데이터 시각화를 하나로 통합합니다.")
# st.title(페이지의 큰 제목) / st.write(페이지 내용)





# 2. 세션 상태 및 캐싱 함수 > 1번

if "pos_order" not in st.session_state:
    st.session_state.pos_order = []
    

# 2. 세션 상태 및 캐싱 함수 > 2번

if "message" not in st.session_state:
    st.session_state.message = [{"role": "assistant", "content": "안녕하세요! '총매출', '인기상품', '주문건수' 등을 물어보세요."}]


# 2. 세션 상태 및 캐싱 함수 > 3번

@st.cache_data(ttl=60)

def get_cached_summary(rows):
    return summarize(rows)





# 3. 사이드바 데이터 로드 및 초기화 > 1번

st.sidebar.header("⚙️ 데이터 관리")

# 3. 사이드바 데이터 로드 및 초기화 > 2번

uploaded = st.sidebar.file_uploader("추가 매출 CSV 업로드(UTF-8)", type=["csv"])

# 3. 사이드바 데이터 로드 및 초기화 > 3번

if st.button("요약 캐시 초기화"):
    get_cached_summary.clear()
    st.sidebar.success("캐시를 초기화했습니다.")

# 3. 사이드바 데이터 로드 및 초기화 > 4번

if st.button("POS 입력 내역 초기화"):
    st.session_state.pos_orders = []
    st.sidebar.warning("현장 주문 내역이 초기화되었습니다.")


# 3. 사이드바 데이터 로드 및 초기화 > 5번

if uploaded is None:
    sample_path = Path(__file__).resolve().parents[1] / "data" / "sales.csv"
    if uploaded in None: 
        base_rows = [{"product": "book", "quantity" : 2, "price" : 12000}, {"product": "pen", "quantity": 5, "price": 1500}]
    else:
        base_rows = parse_sales(sample_path.read_bytes())
        
else:
    try:
        base_rows = parse_sales(uploaded.getvalue())
        st.sidebar.success(f"CSV에서 {len(base_rows)}행을 불러왔습니다.")
                    
    except ValueError as exc:
        st.sidebar.error(str(exc))

# 3. 사이드바 데이터 로드 및 초기화 > 6번

all_rows = base_rows + st.session_state.pos_order



# 4. 메인 3개 탭 구현 요구사항 > 1번

tab1, tab2, tab3= st.tabs(["📊 매출 대시보드", "💳 POS 주문 입력", "💬 매출 도우미 챗봇"])


# 4. 메인 3개 탭 구현 요구사항 > 탭 1: 📊 매출 대시보드 

with tab1:

    # 탭 1: 📊 매출 대시보드 > 1번
    selected = st.selectbox("조회할 상품 선택", ["전체"] + sorted({row["product"] for row in all_rows}))

    # 탭 1: 📊 매출 대시보드 > 2번
    filtered = all_rows if selected == "전체" else[
        r for r in all_rows if r["product"] == selected
    ]
    summary = get_cached_summary(filtered)

    # 탭 1: 📊 매출 대시보드 > 3번
    col1, col2, col3 = st.columns(3)

    col1.metric("총매출" f"{summary['revenue']:,}원")
    col2.metric("총 판매 수량", f"{summary['quantity']:,}개")
    col3.metric("거래 건수", f"{len(filtered)}건")

    # 탭 1: 📊 매출 대시보드 > 4번
    left, right = st.columns(2)
    with left:
        st.subheader("상세 거래 내역")

        # filtered가 있으면
        # df = pd.DataFrame(filtered)에 df["subtotal"] = df["quantity"] * df["price"]를 추가한 뒤
        # st.dataframe(df, use_container_width=True, hide_index=True)로 출력하고,
        # 비어 있으면 st.info("표시할 데이터가 없습니다.")를 출력합니다.

    with right:
        st.subheader("상품별 매출 비중")

        if summary["by_product"] == True:
            st.bar_chart(summary["by_product"])


# 4. 메인 3개 탭 구현 요구사항 > 탭 2: 💳 POS 주문 입력

with tab2:

    # 탭 2: 💳 POS 주문 입력 > 1번
    st.subheader("신규 현장 주문 등록")

    # 탭 2: 💳 POS 주문 입력 > 2-1번
    st.form("pos_form", clear_on_submit=True)
    p_name = st.text_input("상품명 (1~40자): ")

    # 탭 2: 💳 POS 주문 입력 > 2-2번
    c1, c2 = st.columns(2)
    p_qty = c1.number_input("수량: ", min_value=1, max_value=1000, value=1)
    p_price = c2.number_input("단가(원): ", min_value=100, max_value=1_000_000, value=5000, step=500)

    # 탭 2: 💳 POS 주문 입력 > 2-3번
    submitted = st.form_submit_button("주문 추가")

    # 탭 2: 💳 POS 주문 입력 > 3번
    clean_name = p_name.strip()
    if not clean_name or len(clean_name) > 40:
        st.session_state.pos_orders + {"product": clean_name, "quantity": int(p_qty), "price": int(p_price)}
        st.success(f"'{clean_name}' {p_qty}개 (총 {p_qty * p_price}원) 주문이 등록되었습니다! 대시보드 탭에서 확인하세요.")


# 4. 메인 3개 탭 구현 요구사항 > 탭 3: 💬 매출 도우미 챗봇

with tab3:
    st.subheader("데이터 기반 간단 Q & A")

 # 탭 3: 💬 매출 도우미 챗봇 > 1번
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    # 탭 3: 💬 매출 도우미 챗봇 > 2번
    question = st.char_input("매출에 대해 질문해 보세요 (예] 총 매출 알려줘, 가장 잘 팔린 상품은?)")
    st.session_state.message.append(question) #맞는 지 확인

    # 탭 3: 💬 매출 도우미 챗봇 > 2번
