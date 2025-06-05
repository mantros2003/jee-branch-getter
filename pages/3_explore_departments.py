import streamlit as st

st.set_page_config(page_title="Explore Departments", layout="wide")

st.title("🔬 Explore Departments at IITs")

st.markdown(
    """
    Use this section to explore the **focus areas, career paths**, and **hot research topics** in different engineering departments offered at IITs.
    """
)

departments = {
    "Computer Science and Engineering": {
        "overview": "CSE deals with computation, algorithms, AI/ML, software systems, and data. It’s one of the most sought-after branches.",
        "careers": [
            "💻 Software Developer",
            "📊 Data Scientist / ML Engineer",
            "🧠 AI Researcher",
            "📈 Quant / FinTech",
            "🧪 PhD / Academia"
        ],
        "research": [
            "Large Language Models (LLMs)",
            "Computer Vision",
            "Cybersecurity",
            "Quantum Computing",
            "Edge AI & Federated Learning"
        ],
        "link": "https://cs.iitd.ac.in"
    },

    "Mechanical Engineering": {
        "overview": "Mech involves mechanics, design, thermodynamics, manufacturing, robotics, and materials science. It offers a mix of theory and practical applications.",
        "careers": [
            "⚙️ Core Engineering (Automotive, Aerospace)",
            "📐 Product Design / CAD",
            "🔧 Robotics & Automation",
            "📉 Consulting",
            "📚 Higher Studies (MS/PhD)"
        ],
        "research": [
            "Autonomous Robotics",
            "3D Printing & Additive Manufacturing",
            "Combustion & Fluid Mechanics",
            "Biomechanics",
            "AI in Mechanical Design"
        ],
        "link": "https://me.iitd.ac.in"
    },

    "Electrical Engineering": {
        "overview": "EE covers power systems, electronics, communication, signal processing, embedded systems, and VLSI.",
        "careers": [
            "⚡ Power & Energy Engineer",
            "📶 Communication Systems",
            "🔋 Embedded Systems Engineer",
            "🔬 Semiconductor & VLSI",
            "📈 Finance / Consulting / SDE"
        ],
        "research": [
            "Smart Grids & Renewable Integration",
            "Signal Processing & ML",
            "Wireless Communication (5G/6G)",
            "Neural Signal Processing",
            "Photonic Systems"
        ],
        "link": "https://ee.iitd.ac.in"
    },

    "Chemical Engineering": {
        "overview": "ChemE focuses on chemical process design, reaction engineering, thermodynamics, and bioprocessing. It’s at the intersection of chemistry and engineering.",
        "careers": [
            "🧪 Process Engineer (Pharma, Oil & Gas)",
            "🌱 Sustainability / Energy sector",
            "💼 FMCG / Supply Chain",
            "🔬 R&D",
            "📘 PhD / Higher Studies"
        ],
        "research": [
            "Catalysis & Reaction Engineering",
            "Battery Tech & Energy Storage",
            "Waste Treatment",
            "Green Hydrogen",
            "Computational Fluid Dynamics"
        ],
        "link": "https://cheme.iitd.ac.in"
    },

    "Civil Engineering": {
        "overview": "Civil covers structures, transportation, geotechnical, water resources, and environmental engineering. It’s essential to infrastructure and urban development.",
        "careers": [
            "🏗️ Structural Engineer",
            "🚧 Project Management",
            "🌊 Environmental Consultant",
            "🚆 Transportation Planner",
            "🏙️ Urban Developer"
        ],
        "research": [
            "Smart & Sustainable Cities",
            "Disaster-Resilient Infrastructure",
            "Water Treatment & Hydrology",
            "Geospatial Mapping (GIS)",
            "Earthquake Engineering"
        ],
        "link": "https://civil.iitd.ac.in"
    },

    "Mathematics and Computing": {
        "overview": "This interdisciplinary branch combines advanced mathematics with computer science. Strong emphasis on algorithms, optimization, and data.",
        "careers": [
            "💹 Quantitative Analyst",
            "💻 SDE / Backend Systems",
            "📊 Data Science / ML",
            "🔬 Research / Theoretical CS",
            "📈 Consulting"
        ],
        "research": [
            "Algorithmic Game Theory",
            "Computational Algebra",
            "Machine Learning Theory",
            "Numerical Optimization",
            "Cryptography"
        ],
        "link": "https://maths.iitd.ac.in"
    },
    "Aerospace Engineering": {
        "overview": "Aerospace Engineering focuses on the design, development, and testing of aircraft, spacecraft, satellites, and missiles. It combines fluid dynamics, materials, propulsion, and control systems.",
        "careers": [
            "🚀 Aerospace Engineer (ISRO, DRDO, HAL)",
            "🛫 Aircraft Design & Control",
            "💻 Simulation & CFD Analyst",
            "🛰️ Satellite Systems Engineer",
            "📚 Research / PhD (Aerospace, Astrodynamics)"
        ],
        "research": [
            "Hypersonic Flight & Reentry Vehicles",
            "Space Propulsion Systems",
            "UAVs and Autonomous Flight",
            "Computational Fluid Dynamics (CFD)",
            "Structural Health Monitoring"
        ],
        "link": "https://aero.iitb.ac.in"
    },

    "Economics": {
        "overview": "Offered in some IITs as a B.S. or M.Sc. program, Economics at IITs emphasizes analytical modeling, data, game theory, and policy. It equips students for industry and research alike.",
        "careers": [
            "📈 Economic Analyst / Policy Advisor",
            "📊 Data & Risk Analyst",
            "💹 Quantitative Finance",
            "🧠 Think Tanks / Development Sector",
            "🎓 PhD in Economics / Public Policy"
        ],
        "research": [
            "Behavioral & Experimental Economics",
            "Development & Environmental Economics",
            "Market Design & Game Theory",
            "Monetary Policy Modeling",
            "Computational Social Science"
        ],
        "link": "https://hss.iitd.ac.in/economics"
    },

    "Data Science / AI": {
        "overview": "Data Science and AI programs, often interdisciplinary, focus on statistics, machine learning, big data engineering, and deep learning. These are among the most in-demand skillsets globally.",
        "careers": [
            "📊 Data Scientist",
            "🧠 ML / AI Engineer",
            "💼 Business Analyst",
            "🔬 AI Researcher (NLP, CV)",
            "🧱 MLOps / Data Engineer"
        ],
        "research": [
            "Large Language Models (LLMs)",
            "Generative AI",
            "Graph Neural Networks",
            "Explainable AI (XAI)",
            "AI for Social Good"
        ],
        "link": "https://scai.iitd.ac.in"
    },

    "Energy Engineering": {
        "overview": "This interdisciplinary branch focuses on renewable energy systems, energy efficiency, sustainability, and power technologies. It combines mechanical, electrical, and environmental domains.",
        "careers": [
            "🌞 Renewable Energy Consultant",
            "⚡ Power Systems Engineer",
            "🏭 Energy Efficiency Auditor",
            "🌱 Sustainability Analyst",
            "🔋 Battery & EV Systems Engineer"
        ],
        "research": [
            "Solar PV & Thermal Systems",
            "Energy Storage (Batteries, Hydrogen)",
            "Smart Grids & Decentralized Energy",
            "Carbon Capture & Utilization",
            "Energy Policy Modeling"
        ],
        "link": "https://ces.iitd.ac.in"
    }
}

selected = st.selectbox("🔎 Choose a Department", list(departments.keys()))

data = departments[selected]

st.subheader("📚 Overview")
st.write(data["overview"])

st.subheader("💼 Typical Career Paths")
for path in data["careers"]:
    st.markdown(f"- {path}")

st.subheader("🧪 Latest Research Topics")
with st.expander("Show current hot areas of research"):
    for topic in data["research"]:
        st.markdown(f"- {topic}")

st.subheader("🔗 Department Website")
st.markdown(f"[Visit Department Page]({data['link']})")
