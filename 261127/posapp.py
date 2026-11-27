# 1. 기본 환경 및 모듈 임포트 > 2번

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

uploaded = st.sidebar.file_uploader("추가 매출 CSV 업로드(UTF-8)", type=["csv"])

# 3. 사이드바 데이터 로드 및 초기화 > 3번

if st.button("요약 캐시 초기화"):
    get_cached_summary.clear()
    st.sidebar.success("캐시를 초기화했습니다.")

# 3. 사이드바 데이터 로드 및 초기화 > 4번

if st.button("POS 입력 내역 초기화"):
    st.session_state.pos_orders = []
    st.sidebar.success("현장 주문 내역이 초기화되었습니다.")



