import pandas as pd
import streamlit as st


from pathlib import Path
from common import parse_sales, summarize

# pandas를 pd로, streamlit을 st로 임포트하고, common 모듈에서 parse_sales와 summarize를 가져옵니다.


st.set_page_config(page_title="미니 POS & 매출 분석기", layout="wide")

# 페이지 설정은 page_title="미니 POS & 매출 대시보드", layout="wide"로 지정합니다.

st.title("🏪올인원 미니 POS & 매출 분석기")
st.write("**학습 목료** : 입력('form'), 상태 유지('session_state'), 캐싱('cache_data'), 데이터 시각화를 하나로 통합합니다.")
# st.title(페이지의 큰 제목) / st.write(페이지 내용)


# st.session_state에 "pos_orders"가 없으면 빈 리스트 []로 초기화합니다.

#if st.session_state 내용 찾기
st.session_state = []

