from job_roles import job_roles

all_skills = set()

for role in job_roles:
    all_skills.update(job_roles[role])


def analyze_resume(text, job_description=""):

    text = text.lower()

    skills = []

    for skill in all_skills:
        if skill in text:
            skills.append(skill)

    score = min(len(skills)*10,100)

    best_role = ""
    max_match = 0
    missing = []

    for role, role_skills in job_roles.items():

        match = len(set(role_skills) & set(skills))

        if match > max_match:

            max_match = match
            best_role = role
            missing = list(set(role_skills) - set(skills))

    jd_match = 0

    if job_description:

        jd_words = job_description.lower().split()

        common = set(jd_words) & set(text.split())

        jd_match = int(len(common)/len(jd_words)*100)

    suggestions = []

    if "project" not in text:
        suggestions.append("Add project experience")

    if "experience" not in text:
        suggestions.append("Include work experience")

    if "education" not in text:
        suggestions.append("Add education section")

    if score < 50:
        suggestions.append("Add more technical skills")

    return {

        "skills":skills,
        "score":score,
        "role":best_role,
        "missing":missing,
        "jd_match":jd_match,
        "suggestions":suggestions

    }
