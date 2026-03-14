import streamlit as st
from resume_parser import extract_resume_text
from analyzer import analyze_resume
from charts import skill_chart

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

st.title("🚀 AI Resume Analyzer Pro")

st.write("Upload your resume and get ATS analysis")

resume = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

job_description = st.text_area("Paste Job Description (Optional)")

if resume:

    text = extract_resume_text(resume)

    st.subheader("📄 Resume Text")
    st.text_area("", text, height=200)

    result = analyze_resume(text, job_description)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🎯 ATS Score")
        st.progress(result["score"]/100)
        st.write(result["score"])

    with col2:
        st.subheader("💼 Recommended Role")
        st.write(result["role"])

    st.subheader("🧠 Skills Found")
    st.write(result["skills"])

    st.subheader("⚠ Missing Skills")
    st.write(result["missing"])

    st.subheader("📊 Skill Radar Chart")

    fig = skill_chart(result["skills"])
    st.plotly_chart(fig)

    if job_description:

        st.subheader("📑 Resume vs Job Description Match")
        st.write(result["jd_match"], "% match")

    st.subheader("🤖 Resume Suggestions")

    for s in result["suggestions"]:
        st.write("-", s)
