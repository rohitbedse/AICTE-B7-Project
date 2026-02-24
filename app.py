import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

st.set_page_config(page_title="Job Application Intelligence", page_icon="🧠", layout="centered")
st.title("🧠 Job Application Intelligence System")
st.caption("Resume vs Job Description – Parallel AI Brain")

# 1. LLM
llm = GoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.2)

# 2. Prompts
match_prompt = PromptTemplate.from_template("""
You are an ATS system.
Given Resume and Job Description, calculate skill match percentage (0-100).
Return ONLY JSON:
{{
  "match_percentage": number
}}

Resume:
{resume}

Job Description:
{jd}
""")

missing_prompt = PromptTemplate.from_template("""
You are a recruiter.
Find missing skills from resume compared to job description.
Return ONLY JSON:
{{
  "missing_skills": [ "skill1", "skill2" ]
}}

Resume:
{resume}

Job Description:
{jd}
""")

improve_prompt = PromptTemplate.from_template("""
You are a career coach.
Suggest improvements to the resume for this job.
Return ONLY JSON:
{{
  "improvement_suggestions": [ "point1", "point2" ]
}}

Resume:
{resume}

Job Description:
{jd}
""")

cover_prompt = PromptTemplate.from_template("""
You are an HR professional.
Write a short 3-line professional cover note for this job.
Return ONLY JSON:
{{
  "cover_note": "3 lines cover note"
}}

Resume:
{resume}

Job Description:
{jd}
""")

parser = JsonOutputParser()

parallel_chain = RunnableParallel({
    "match": match_prompt | llm | parser,
    "missing": missing_prompt | llm | parser,
    "improve": improve_prompt | llm | parser,
    "cover": cover_prompt | llm | parser,
})

# UI Inputs
resume_text = st.text_area("📄 Paste your Resume", height=180)
jd_text = st.text_area("📌 Paste Job Description", height=180)

if st.button("Analyze Resume vs JD 🚀"):
    if not resume_text.strip() or not jd_text.strip():
        st.warning("Please provide both Resume and Job Description.")
    else:
        with st.spinner("Analyzing with Parallel AI Brain..."):
            result = parallel_chain.invoke({
                "resume": resume_text,
                "jd": jd_text
            })

        st.subheader("📊 Results")

        st.metric("Match Percentage", f"{result['match']['match_percentage']}%")

        st.markdown("### ❌ Missing Skills")
        st.write(result["missing"]["missing_skills"])

        st.markdown("### ✍️ Improvement Suggestions")
        for i, point in enumerate(result["improve"]["improvement_suggestions"], 1):
            st.write(f"{i}. {point}")

        st.markdown("### 📨 Custom Cover Note")
        st.info(result["cover"]["cover_note"])
