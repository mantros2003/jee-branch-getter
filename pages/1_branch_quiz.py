import streamlit as st

st.set_page_config(page_title="Branch Interest Quiz")

st.header("🧠 Find Your Ideal Engineering Branch")

branch_scores = {
    "Computer Science": 0,
    "Electrical Engineering": 0,
    "Mechanical Engineering": 0,
    "Civil Engineering": 0,
    "Chemical Engineering": 0,
    "Engineering Physics": 0,
    "Biotechnology": 0,
    "Mathematics and Computing": 0,
}

q1 = st.radio("1. What kind of problems do you enjoy solving?", [
    "Logical puzzles", "Real-world physical systems", "Electrical gadgets", "Chemical reactions"])

q2 = st.radio("2. What's your favorite subject?", [
    "Physics", "Math", "Chemistry", "Computer Science"])

q3 = st.radio("3. Do you like building physical things or coding?", [
    "Building", "Coding", "Both"])

q4 = st.radio("4. Are you interested in research or job-ready skills?", [
    "Research", "Job-ready", "Both"])

q5 = st.radio("5. How important is a high salary package?", [
    "Very important", "Somewhat", "Not really"])

if st.button("🔍 Find Best-Fit Branches"):
    scores = {k: 0 for k in branch_scores}

    # Mapping answers to scores (can be fine-tuned)
    if q1 == "Logical puzzles":
        scores["Computer Science"] += 2
        scores["Mathematics and Computing"] += 2
    elif q1 == "Real-world physical systems":
        scores["Mechanical Engineering"] += 2
        scores["Civil Engineering"] += 2
    elif q1 == "Electrical gadgets":
        scores["Electrical Engineering"] += 2
    elif q1 == "Chemical reactions":
        scores["Chemical Engineering"] += 2
        scores["Biotechnology"] += 1

    if q2 == "Physics":
        scores["Engineering Physics"] += 2
        scores["Electrical Engineering"] += 1
    elif q2 == "Math":
        scores["Mathematics and Computing"] += 2
        scores["Computer Science"] += 1
    elif q2 == "Chemistry":
        scores["Chemical Engineering"] += 2
        scores["Biotechnology"] += 1
    elif q2 == "Computer Science":
        scores["Computer Science"] += 2
        scores["Mathematics and Computing"] += 1

    if q3 == "Building":
        scores["Mechanical Engineering"] += 2
        scores["Civil Engineering"] += 2
    elif q3 == "Coding":
        scores["Computer Science"] += 2
    elif q3 == "Both":
        scores["Electrical Engineering"] += 1
        scores["Engineering Physics"] += 1

    if q4 == "Research":
        scores["Engineering Physics"] += 2
        scores["Biotechnology"] += 1
    elif q4 == "Job-ready":
        scores["Computer Science"] += 2
        scores["Mechanical Engineering"] += 1
    elif q4 == "Both":
        scores["Electrical Engineering"] += 1
        scores["Mathematics and Computing"] += 1

    if q5 == "Very important":
        scores["Computer Science"] += 2
        scores["Mathematics and Computing"] += 2
    elif q5 == "Somewhat":
        scores["Electrical Engineering"] += 1
        scores["Mechanical Engineering"] += 1
        scores["Chemical Engineering"] += 1
    elif q5 == "Not really":
        scores["Engineering Physics"] += 1
        scores["Civil Engineering"] += 1
        scores["Biotechnology"] += 1

    # Sort and display top 3
    top = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:3]
    st.success("🎯 Your top recommended branches:")
    for branch, score in top:
        st.markdown(f"- **{branch}** (Score: {score})")
