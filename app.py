import streamlit as st
from analyzer import analyze_resume
from resume_parser import extract_resume_text

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

st.title("📄 AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])

if uploaded_file is not None:

    text = extract_resume_text(uploaded_file)

    st.subheader("Extracted Resume Text")
    st.text_area("", text, height=250)

    result = analyze_resume(text)

    st.subheader("Resume Analysis")

    st.write("### Skills Detected")
    st.write(result["skills"])

    st.write("### Resume Score")
    st.progress(result["score"] / 100)

    st.write("Score:", result["score"])
