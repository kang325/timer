import os
import streamlit as st
import streamlit.components.v1 as components

# 페이지 설정
st.set_page_config(
    page_title="스마트 타이머 & 알람 앱",
    page_icon="⏰",
    layout="centered"
)

# 기본 Streamlit 여백 및 패딩 최소화
st.markdown("""
    <style>
        .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
            padding-left: 1rem;
            padding-right: 1rem;
        }
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# HTML 파일 경로 설정
html_file_path = os.path.join("htmls", "index.html")

# HTML 파일 읽기 및 렌더링
if os.path.exists(html_file_path):
    with open(html_file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # iframe 형태로 HTML 삽입 (높이 지정 및 스크롤 허용)
    components.html(html_content, height=850, scrolling=True)
else:
    st.error(f"'{html_file_path}' 파일을 찾을 수 없습니다. 폴더 구조를 확인해 주세요.")
