skills_db = [
"python","machine learning","data science",
"sql","html","css","javascript","react",
"tensorflow","pytorch","deep learning"
]

roles = {

"Data Scientist":[
"python","machine learning","data science","sql"
],

"AI Engineer":[
"python","tensorflow","pytorch","deep learning"
],

"Web Developer":[
"html","css","javascript","react"
]

}

def analyze_resume(text):

    text = text.lower()

    found_skills = []

    for skill in skills_db:
        if skill in text:
            found_skills.append(skill)

    score = min(len(found_skills)*12,100)

    best_role = ""
    max_match = 0
    missing = []

    for role, role_skills in roles.items():

        match = len(set(role_skills) & set(found_skills))

        if match > max_match:

            max_match = match
            best_role = role
            missing = list(set(role_skills)-set(found_skills))

    suggestions = []

    if "project" not in text:
        suggestions.append("Add projects section")

    if "experience" not in text:
        suggestions.append("Include work experience")

    if "education" not in text:
        suggestions.append("Add education section")

    return {

        "skills":found_skills,
        "score":score,
        "role":best_role,
        "missing":missing,
        "suggestions":suggestions
    }
