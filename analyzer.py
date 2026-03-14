import re

skill_keywords = [
    "python",
    "java",
    "c++",
    "machine learning",
    "deep learning",
    "data science",
    "sql",
    "html",
    "css",
    "javascript",
    "react",
    "node",
    "tensorflow",
    "pytorch",
]

def analyze_resume(text):

    text = text.lower()

    found_skills = []

    for skill in skill_keywords:
        if skill in text:
            found_skills.append(skill)

    score = min(len(found_skills) * 10, 100)

    return {
        "skills": found_skills,
        "score": score
    }
