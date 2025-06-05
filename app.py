import streamlit as st
import os
import json

def load_cutoff_data(folder_path):
    data = []
    for filename in os.listdir(folder_path):
        if filename.startswith("cutoff_data_round5_general_gn_") and filename.endswith(".json"):
            college_key = filename.replace("cutoff_data_round5_general_gn_", "").replace(".json", "")
            college_name = "IIT " + college_key.replace("_", " ").title()

            with open(os.path.join(folder_path, filename), "r") as file:
                branches = json.load(file)
                for branch in branches:
                    branch["college"] = college_name
                    data.append(branch)
    return data

def find_branches_by_rank(rank, cutoff_data, margin=300):
    within_reach = []
    slightly_out_of_reach = []
    close_to_opening = []

    for entry in cutoff_data:
        try:
            opening = int(entry["opening"])
            closing = int(entry["closing"])
        except (ValueError, KeyError):
            continue

        entry_info = {
            "college": entry["college"],
            "branch": entry["branch"],
            "opening": opening,
            "closing": closing
        }

        if rank <= closing:
            within_reach.append(entry_info)
        elif closing < rank <= closing + margin:
            slightly_out_of_reach.append(entry_info)

        if abs(rank - opening) <= margin:
            close_to_opening.append(entry_info)

    return within_reach, slightly_out_of_reach, close_to_opening

def find_desired_branches(rank, cutoff_data, margin):
    desirable_branches = []
    
    for entry in cutoff_data:
        try:
            opening = int(entry["opening"])
            closing = int(entry["closing"])
        except (ValueError, KeyError):
            continue
    
        entry_info = {
            "college": entry["college"],
            "branch": entry["branch"],
            "opening": opening,
            "closing": closing
        }
    
        if rank - closing <= margin and rank >= opening:
          desirable_branches.append(entry_info)
    
    return sorted(desirable_branches, key=lambda x: x["closing"])

# --- UI ---
st.set_page_config(page_title="JEE Branch Predictor", layout="wide")
st.title("🔍 JEE Advanced Branch Predictor (2024 Round 5 - Gen, Gender Neutral)")
st.markdown(
    ":red-badge[:material/warning: NOTE] The current dataset is only for 2024 GENERAL GENDER-NEUTRAL Round 5 cutoffs"
)

rank = st.number_input("Enter your JEE Advanced Rank", min_value=0, step=1)
margin = st.slider("Margin for nearby branches", min_value=50, max_value=1000, value=250, step=50)

if st.button("Search"):
    data = load_cutoff_data("data")
    within, near_miss, close_open = find_branches_by_rank(rank, data, margin)
    desired = find_desired_branches(rank, data, margin)

    if within:
        st.subheader("✅ Branches Within Reach")
        st.dataframe(within, use_container_width=True)
    else:
        st.info("No branches found within reach.")

    if near_miss:
        st.subheader("⚠️ Slightly Out of Reach")
        st.dataframe(near_miss, use_container_width=True)

    if close_open:
        st.subheader("📌 Close to Opening Rank")
        st.dataframe(close_open, use_container_width=True)

    if desired:
        st.subheader("⭐️ Desired Branches")
        st.dataframe(desired, use_container_width=True)

st.header("📚 Explore IIT Curriculum")

# Mapping IIT names to their curriculum URLs (expand as needed)
iit_links = {
    "IIT Bombay": "https://portal.iitb.ac.in/asc/Courses",
    "IIT Delhi": "https://home.iitd.ac.in/uploads/UG%20Programme%20Rules/CoS%202024__UG%20Programme%20Rules.pdf",
    "IIT Kanpur": "https://www.iitk.ac.in/doaa/courses-of-study-aug-24",
    "IIT Kharagpur": "https://erp.iitkgp.ac.in/ERPWebServices/curricula/specialisationList_new_curr.jsp?stuType=UG",
    "IIT Madras": "https://www.iitm.ac.in/sites/default/files/Academic%20Curricula%20Files/Curriculum_-_2024_Batch_B.Tech_Version_1.pdf",
    "IIT Roorkee": "https://acad.iitr.ac.in/Varsity/UGProgrammes_new1.html",
    "IIT Guwahati": "https://iitg.ac.in/acad/CourseStructure/Btech2018/btech.php",
    "IIT Hyderabad": "https://www.iith.ac.in/assets/files/pdf/Courses-of-Study-Bachelors.pdf",
    "IIT BHU": "https://prev.iitbhu.ac.in/deans/doaa/academic/courses/ug/btech"
    # Add more as needed
}

selected_iit = st.selectbox("Select an IIT to view its course curriculum", list(iit_links.keys()))

if selected_iit:
    if st.button(f"Go to {selected_iit}'s Curriculum"):
        st.markdown(f"[Click here to view {selected_iit}'s curriculum]({iit_links[selected_iit]})", unsafe_allow_html=True)
