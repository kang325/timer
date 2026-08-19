import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# 1. 페이지 기본 설정 (넓은 화면 레이아웃 사용)
st.set_page_config(
    page_title="주사위 타워 디펜스 게임",
    page_icon="🎲",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. HTML 파일 경로 지정
HTML_PATH = Path(__file__).resolve().parent / "htmls" / "index.html"

# 3. HTML 파일 읽기 및 화면 출력
try:
    if HTML_PATH.exists():
        with open(HTML_PATH, "r", encoding="utf-8") as f:
            html_content = f.read()
        
        # Streamlit 컴포넌트를 통해 HTML 출력
        components.html(html_content, height=850, scrolling=True)
    else:
        st.error("⚠️ `htmls/index.html` 파일을 찾을 수 없습니다. 경로를 확인해 주세요.")
except Exception as e:
    st.error(f"⚠️ HTML 파일을 불러오는 중 오류가 발생했습니다: {e}")
