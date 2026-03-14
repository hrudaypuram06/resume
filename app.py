import streamlit as st
from resume_parser import extract_resume_text
from analyzer import analyze_resume

st.set_page_config(page_title="ProResume Intelligence", layout="wide")

# Load CSS
def local_css(file):
    with open(file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

st.markdown("<h1 class='title'>PRORESUME INTELLIGENCE</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>AI Powered Resume Analyzer</p>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if uploaded_file:

    text = extract_resume_text(uploaded_file)

    result = analyze_resume(text)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("ATS Score")
        st.progress(result["score"]/100)
        st.write(result["score"])
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("Detected Skills")
        st.write(result["skills"])
        st.markdown("</div>", unsafe_allow_html=True)

    with col3:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("Recommended Role")
        st.write(result["role"])
        st.markdown("</div>", unsafe_allow_html=True)

    st.subheader("Missing Skills")
    st.write(result["missing"])

    st.subheader("AI Suggestions")

    for s in result["suggestions"]:
        st.write("-", s)
