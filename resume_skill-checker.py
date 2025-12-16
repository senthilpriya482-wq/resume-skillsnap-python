print("RESUME SKILL CHECKER PROJECT")
print("(Developed using Python basics)")

# Sample input
resume_text = "I know Python basics and HTML."

skills = [
    "python basics",
    "html",
    "communication"
]

found_skills = []

for skill in skills:
    if skill in resume_text.lower():
        found_skills.append(skill)

print("\nSkills Found in Resume:")
if len(found_skills) == 0:
    print("No skills detected")
else:
    for s in found_skills:
        print("-", s.capitalize())

skill_count = len(found_skills)

print("\nResume Analysis Result:")
if skill_count >= 3:
    print("Resume Strength: EXCELLENT")
elif skill_count >= 2:
    print("Resume Strength: GOOD")
else:
    print("Resume Strength: NEEDS IMPROVEMENT")
