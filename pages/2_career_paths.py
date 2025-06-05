import streamlit as st

st.set_page_config(page_title="Career Explorer for JEE Students", layout="wide")
st.title("🧭 Explore Career Paths After Engineering")

st.markdown("""
Welcome, JEE Aspirant! 👋
This tool helps you explore various exciting career paths you can pursue after your engineering studies.
Select a path from the dropdown in the sidebar to learn more.
""")

career_paths = {
    "Software Development": {
        "What People Do": "Software Developers design, code, test, and maintain software applications (websites, mobile apps, enterprise systems). Key tasks include problem-solving, writing efficient code, team collaboration (often Agile), debugging, and continuous learning. Requires strong analytical and logical skills.",
        "Typical Roles": ["Backend Developer", "Frontend Developer", "Full Stack Engineer", "DevOps Engineer", "Software Development Engineer (SDE)", "Mobile App Developer"],
        "Recommended Backgrounds": ["Computer Science (CSE)", "Mathematics and Computing (M&C)", "Electrical Engineering (EE)", "Electronics and Communication (ECE)", "Information Technology (IT)"],
        "Skills": ["Data Structures & Algorithms (DSA)", "System Design", "Programming Languages (e.g., Python, Java, C++, JavaScript)", "Web Development frameworks", "Databases (SQL/NoSQL)", "Cloud Computing (AWS/Azure/GCP)", "Version Control (Git)"],
        "Long-Term Prospects": "Growth to Senior Engineer, Tech Lead, Manager, Architect, or Principal/Distinguished Engineer. Options include Product Management, entrepreneurship, or specialization (e.g., Cybersecurity, AI/ML, SRE). Consistently high global demand.",
        "Top Companies": ["Google", "Microsoft", "Amazon", "Meta", "Apple", "Salesforce", "Netflix", "Flipkart", "Uber", "Various startups"],
        "Resources": [
            "https://roadmap.sh",
            "https://github.com/ossu/computer-science",
            "https://leetcode.com/",
            "https://www.geeksforgeeks.org/data-structures/",
            "freeCodeCamp.org"
        ]
    },
    "Data Science / Machine Learning": {
        "What People Do": "Extract insights and build predictive models from complex datasets. Involves collecting, cleaning, and analyzing data; developing & deploying ML algorithms (e.g., for recommendations, NLP). Combines statistics, programming (Python/R), and domain knowledge to drive data-informed decisions.",
        "Typical Roles": ["Data Scientist", "Machine Learning Engineer", "AI Researcher", "Data Analyst", "Business Intelligence Developer", "Data Engineer"],
        "Recommended Backgrounds": ["Computer Science (CSE)", "Mathematics and Computing (M&C)", "Electrical Engineering (EE)", "Electronics and Communication (ECE)", "Statistics"],
        "Skills": ["Python/R", "Statistics & Probability", "Machine Learning Algorithms", "Deep Learning Frameworks (TensorFlow/PyTorch)", "Data Wrangling", "SQL", "Data Visualization", "Big Data Technologies (Spark)"],
        "Long-Term Prospects": "Advance to Senior/Lead Data Scientist, AI Architect, or Head of Data Science/AI. Specializations include Computer Vision, NLP, Reinforcement Learning. Abundant opportunities across industries or in AI-focused startups; PhD for deeper research.",
        "Top Companies": ["Google AI", "Meta AI", "Microsoft AI", "NVIDIA", "OpenAI", "Amazon ML", "Netflix", "Consulting firms (e.g., Fractal Analytics)", "Various startups"],
        "Resources": [
            "https://www.kaggle.com/learn",
            "https://fast.ai/",
            "Andrew Ng's Machine Learning Course (Coursera)",
            "https://www.deeplearning.ai/",
            "Stanford CS229 & CS231n course materials"
        ]
    },
    "Quantitative Finance (Quant)": {
        "What People Do": "Apply mathematical and statistical models to financial markets: pricing instruments, developing trading algorithms, managing risk, and optimizing portfolios. Highly analytical, data-intensive, using Python/C++/R. Work in investment banks, hedge funds, FinTech.",
        "Typical Roles": ["Quantitative Analyst", "Algorithmic Trader", "Financial Engineer", "Risk Analyst", "Quant Developer"],
        "Recommended Backgrounds": ["Mathematics and Computing (M&C)", "Computer Science (CSE)", "Physics", "Electrical Engineering (EE)", "Statistics", "Financial Engineering"],
        "Skills": ["Advanced Probability & Statistics", "Stochastic Calculus", "Time Series Analysis", "Financial Modeling", "Python (NumPy, Pandas)", "C++", "Machine Learning", "Knowledge of financial markets"],
        "Long-Term Prospects": "High earning potential. Progress to Senior Quant, Portfolio Manager, Head of Strategy, or Chief Risk Officer. Options to start own hedge funds/FinTech. Intellectually demanding, high-pressure field.",
        "Special Note": "Quant roles are renowned for offering some of the highest initial compensation packages for graduates from premier engineering and mathematics programs.",
        "Top Companies": ["Jane Street", "Tower Research Capital", "DE Shaw", "Citadel Securities", "Hudson River Trading", "Two Sigma", "Goldman Sachs", "Morgan Stanley"],
        "Resources": [
            "https://www.quantstart.com/",
            "https://www.investopedia.com/terms/q/quantitativeanalysis.asp",
            "Book: 'Heard on the Street' by Timothy Falcon Crack",
            "Book: 'Paul Wilmott Introduces Quantitative Finance'"
        ]
    },
    "Management Consulting": {
        "What People Do": "Help organizations solve business problems, improve performance, and implement strategies. Involves data analysis, market research, strategy development, and client presentations across industries. Requires travel, teamwork, strong analytical and communication skills; fast-paced environment.",
        "Typical Roles": ["Management Consultant", "Strategy Analyst", "Business Analyst", "Technology Consultant"],
        "Recommended Backgrounds": ["Any engineering branch (strong analytical & problem-solving skills needed)", "Excellent communication, leadership skills. MBA common for advancement."],
        "Skills": ["Problem Solving (Case Interviews)", "Data Analysis", "Business Acumen", "Financial Modeling basics", "Presentation Skills (PowerPoint)", "Communication"],
        "Long-Term Prospects": "Steep learning curve, broad industry exposure. Advance to Senior Consultant, Manager, Principal/Partner. Options for industry leadership roles, entrepreneurship, or top MBA programs. Work-life balance can be a challenge.",
        "Top Companies": ["McKinsey & Company", "Boston Consulting Group (BCG)", "Bain & Company", "Accenture Strategy", "Deloitte Consulting", "EY", "KPMG"],
        "Resources": [
            "https://www.caseinterview.com/ (Victor Cheng)",
            "Book: 'Case in Point' by Marc Cosentino",
            "Management Consulted (website)",
            "Firms' official websites for case studies"
        ]
    },
    "Core Engineering (Mechanical/Electrical/Civil etc.)": {
        "What People Do": "Apply scientific/math principles to design, develop, build, and test physical systems and structures (e.g., engines, power systems, bridges). Use CAD/CAM, simulation tools; manage projects, ensure safety/efficiency. Mix of office design and on-site fieldwork.",
        "Typical Roles": ["Design Engineer", "Manufacturing Engineer", "Project Engineer", "R&D Engineer (Core)", "Process Engineer", "Site Engineer", "Automation Engineer"],
        "Recommended Backgrounds": ["Mechanical", "Electrical", "Civil", "Chemical", "Aerospace", "Automobile", "Instrumentation Engineering"],
        "Skills": ["CAD/CAM Software (AutoCAD, SolidWorks)", "Simulation Tools (ANSYS, MATLAB)", "Fundamental engineering principles", "Project Management", "Technical Drawing"],
        "Long-Term Prospects": "Advance to Senior/Lead Engineer, Project/Plant Manager, Head of Engineering, or technical expert. Opportunities in manufacturing, infrastructure, energy, PSUs, R&D. Options for M.Tech/PhD (specialization) or MBA (management). Stable career with tangible impact.",
        "Top Companies": ["Larsen & Toubro (L&T)", "Tata Group (Motors, Steel, Power)", "Mahindra & Mahindra", "Siemens", "General Electric (GE)", "Bosch", "PSUs (NTPC, BHEL, ISRO, DRDO)"],
        "Resources": [
            "https://nptel.ac.in/",
            "Professional Engineering Societies (ASME, IEEE, ASCE)",
            "Coursera/edX for specialized courses"
        ]
    },
    "Product Management": {
        "What People Do": "Define product strategy, roadmap, and features; act as 'CEO of the product.' Understand user needs (research, data), define vision, and work with engineering, marketing, and sales to build, launch, and iterate. Cross-functional role needing tech, business, and user empathy.",
        "Typical Roles": ["Product Manager (PM)", "Associate Product Manager (APM)", "Technical Product Manager (TPM)"],
        "Recommended Backgrounds": ["Engineering (CSE, ECE often) with tech & business understanding. MBA can help but not always required for APM.", "Strong communication & leadership."],
        "Skills": ["User Research & Empathy", "Market & Data Analysis", "Product Roadmapping & Prioritization", "Agile Methodologies", "Communication & Presentation", "Business Acumen"],
        "Long-Term Prospects": "Advance to Senior PM, Group PM, Director, VP, or Chief Product Officer (CPO). Broad skillset leads to options in entrepreneurship, venture capital, or general management. Highly influential role shaping products.",
        "Top Companies": ["Google", "Microsoft", "Amazon", "Meta", "Flipkart", "Atlassian", "Salesforce", "Cred", "Many startups"],
        "Resources": [
            "Book: 'Cracking the PM Interview' by Gayle Laakmann McDowell",
            "Book: 'Inspired' by Marty Cagan",
            "Product School (Resources & Courses)",
            "Exponent (PM Interview Prep)"
        ]
    },
    "Research (Academia & Industry R&D)": {
        "What People Do": "Discover new knowledge or develop/improve technologies. Academia: experiments, analysis, publishing papers, grant applications. Industry R&D: applied focus on innovative products/solutions. Requires deep expertise, critical thinking, perseverance.",
        "Typical Roles": ["Research Scientist/Engineer", "Postdoctoral Researcher", "Research Associate", "R&D Specialist", "Principal Investigator", "Professor"],
        "Recommended Backgrounds": ["Master's (M.Tech/MS) for entry, PhD for independent research roles. Strong foundation in a specific engineering/science field. Passion for inquiry and strong academic record vital."],
        "Skills": ["Deep Domain Knowledge", "Scientific Method & Experiment Design", "Data Analysis (Python, R, MATLAB)", "Critical Thinking", "Scientific Writing & Communication", "Literature Review"],
        "Long-Term Prospects": "Academia: Postdoc to Professor, leading research groups. Industry: Scientist to Research Manager/Director. Options in government labs, think tanks, or roles like data science, specialized consulting, deep-tech startups. PhD often key for leadership.",
        "Top Institutions/Companies": [
            "**Academia (India):** IITs, IISc Bangalore, TIFR, CSIR Labs, IISERs, DRDO, ISRO",
            "**Academia (International):** Top global universities (MIT, Stanford, etc.)",
            "**Industry R&D:** Google Research, Microsoft Research, IBM Research, Intel Labs, R&D wings of pharma, auto, tech companies."
        ],
        "Resources": [
            "Google Scholar, ResearchGate",
            "Websites of university departments & research labs",
            "Journals (IEEE, ACM, Nature, Science)",
            "arXiv.org (pre-prints)",
            "NPTEL"
        ]
    }
}

# --- Sidebar for Career Path Selection ---
st.sidebar.header("🧑‍💻 Choose a Career Path")
all_paths = ["Select a Path..."] + list(career_paths.keys())
selected_path_name = st.sidebar.selectbox("", all_paths, label_visibility="collapsed")


# --- Display Career Path Information ---
if selected_path_name and selected_path_name != "Select a Path...":
    data = career_paths[selected_path_name]

    st.header(f"✨ {selected_path_name}")

    if "What People Do" in data and data["What People Do"]:
        st.subheader("🤔 What People Actually Do") # Shortened subheader
        st.markdown(data["What People Do"])
        st.write("---")

    if "Typical Roles" in data and data["Typical Roles"]:
        st.subheader("🧑‍💼 Typical Roles")
        for role in data["Typical Roles"]:
            st.markdown(f"- {role}")
        st.write("---")

    if "Recommended Backgrounds" in data and data["Recommended Backgrounds"]:
        st.subheader("🎓 Recommended Engineering Backgrounds")
        for background in data["Recommended Backgrounds"]:
            st.markdown(f"- {background}")
        st.write("---")

    if "Skills" in data and data["Skills"]:
        st.subheader("🧠 Key Skills")
        for skill in data["Skills"]:
            st.markdown(f"- {skill}")
        st.write("---")

    if "Long-Term Prospects" in data and data["Long-Term Prospects"]:
        st.subheader("📈 Long-Term Prospects")
        st.markdown(data["Long-Term Prospects"])
        if "Special Note" in data and data["Special Note"]:
             st.markdown(f"🚀 **Note:** {data['Special Note']}")
        st.write("---")

    if "Top Companies" in data and data["Top Companies"]:
        st.subheader("🏢 Top Companies / Institutions")
        for company in data["Top Companies"]:
            st.markdown(f"- {company}")
        st.write("---")

    if "Resources" in data and data["Resources"]:
        st.subheader("📚 Learning Resources & Communities")
        for resource in data["Resources"]:
            if isinstance(resource, str) and (resource.startswith("http://") or resource.startswith("https://")):
                st.markdown(f"- [{resource}]({resource})")
            else:
                st.markdown(f"- {str(resource)}")
else:
    st.info("ℹ️ Please select a career path from the sidebar to see the details.")
