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
st.title("🔍 JEE Advanced Branch Predictor (Round 5 - Gen, Gender Neutral)")

rank = st.number_input("Enter your JEE Advanced Rank", min_value=1992, step=1)
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
        st.dataframe(close_open, use_container_width=True)
