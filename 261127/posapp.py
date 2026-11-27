# 1. 기본 환경 및 모듈 임포트 > 2번

import pandas as pd
import streamlit as st

from pathlib import Path
from common import parse_sales, summarize

uploaded = st.file_uploader("UTF-8 CSV", type=["csv"])


# 1. 기본 환경 및 모듈 임포트 > 3번

st.set_page_config(page_title="미니 POS & 매출 분석기", layout="wide")


# 1. 기본 환경 및 모듈 임포트 > 4번

st.title("🏪올인원 미니 POS & 매출 분석기")
st.write("**학습 목료** : 입력('form'), 상태 유지('session_state'), 캐싱('cache_data'), 데이터 시각화를 하나로 통합합니다.")
# st.title(페이지의 큰 제목) / st.write(페이지 내용)






# 2. 세션 상태 및 캐싱 함수 > 1번

if "pos_order" not in st.session_state:
    st.session_state = []


# 2. 세션 상태 및 캐싱 함수 > 2번

if "message" not in st.session_state:
    st.session_state = [{"role": "assistant", "content": "안녕하세요! '총매출', '인기상품', '주문건수' 등을 물어보세요."}]


# 2. 세션 상태 및 캐싱 함수 > 3번

@st.cache_data(ttl=60)

def get_cached_summary(rows):
    return summarize(rows)







# 3. 사이드바 데이터 로드 및 초기화 > 1번

st.sidebar.header("⚙️ 데이터 관리")

# 3. 사이드바 데이터 로드 및 초기화 > 2번

st.sidebar.file_uploader("추가 매출 CSV 업로드(UTF-8)", type=["csv"])

# 3. 사이드바 데이터 로드 및 초기화 > 3번



# 3. 사이드바 데이터 로드 및 초기화 > 4번

if uploaded is None:
    sample_path = Path(__file__).resolve().parents[1] / "data" / "sales.csv"
    base_rows = parse_sales(sample_path.read_bytes())
    base_rows = [{"product": "book", "quantity" : 2, "price" : 12000}, {"product": "pen", "quantity": 5, "price": 1500}]

else:
    try:
        base_rows = parse_sales(uploaded.getvalue())
        st.sidebar.success(f"CSV에서 {len(base_rows)}행을 불러왔습니다.")
                    
    except ValueError as exc:
        st.sidebar.error(str(exc))

# 3. 사이드바 데이터 로드 및 초기화 > 5번


