# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 10:46:40 2026

@author: Mogale
"""

import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Zacharia Mogale - Data Scientist & Meteorological Researcher",
    layout="wide"
)

# Sidebar Menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    [
        "Researcher Profile",
        "Experience & Achievements",
        "Projects",
        "Skills & Leadership",
        "Contact",
    ],
)

# -------------------- Researcher Profile --------------------
if menu == "Researcher Profile":
    st.title("Zacharia Mogale")
    st.subheader("Data Scientist | Data Quality & Analytics Practitioner | Meteorological Analyst")
    st.write("**Contact: mogalezach@gmail.com")

    st.markdown("---")
    st.header("Professional Summary")
    st.write("""
    Data Professional with over five years’ experience delivering high-integrity analytical datasets,
    reports, and decision-support insights in regulated, high-accountability environments — including
    remote stations.

    Proven capability across the full data analytics lifecycle: sourcing, validation, modelling,
    analysis, visualisation, and reporting. Strong background in statistical analysis, machine learning,
    and data quality management. Advanced proficiency in R, Python, SQL, SAS, and Power BI.

    .
    """)

    st.subheader("Cloud Timelapse")
    st.video("CloudTimeLapse.mp4")

# -------------------- Experience & Achievements --------------------
elif menu == "Experience & Achievements":
    st.title("Professional Experience & Achievements")

    with st.expander("Senior Meteorological Analyst (Oct 2019 – Mar 2021)", expanded=True):
        st.write("**SAWS**")
        st.write("""
        - Led full-lifecycle management of high-frequency operational datasets.
        - Time-series analysis for trends, anomalies, and quality issues.
        - Delivered analytical reports for national and international stakeholders.
        """)
        st.success("""
        **Key Achievements**
        - 98.86% data availability & 99.99% data integrity  
      
        """)

    with st.expander("Assistant Meteorological Analyst (Jun 2017 – Oct 2018)"):
        st.write("**SAWS**")
        st.write("""
        - Operated and maintained automated atmospheric and marine systems.
        - Conducted validation, quality checks, and preliminary analysis.
        - Compiled reports and supported remote field deployments.
        """)

# -------------------- Projects --------------------
elif menu == "Projects":
    st.title("Selected Data Analytics & Machine Learning Projects")

    st.write("- **FrontScore**: Continuous scoring model using engineered features and regression.")
    st.write("- Predictive resale value models using machine learning in R.")
    st.write("- Binary classification with ensemble models on self-cleaned datasets.")
    st.write("- **Power BI Report**: Interactive geospatial tsunami damage analysis.")

    st.image(
        "cloudy.jpg",
        caption="Atmospheric Conditions & Cloud Dynamics",
        use_column_width=True
    )

# -------------------- Skills & Leadership --------------------
elif menu == "Skills & Leadership":
    st.title("Skills & Leadership")

    st.subheader("Core Technical Skills")
    st.write("- R, Python, SQL, SAS, Power BI, STATA, ArcGIS")
    st.write("- Machine Learning, Statistical Analysis, Time Series & Forecasting")
    st.write("- Data Quality Assurance & Visualisation")

    st.subheader("Core Professional Skills")
    st.write("- Project Management (Agile), Process Optimisation")
    st.write("- Leadership in multicultural and high-risk environments")
    st.write("- Critical Thinking & Decision-Making")

    st.subheader("Leadership Roles")
    st.write("""
    - **Deputy Expedition Leader, SAWS (2020–2021)**  
      Led a team of 9; coordinated logistics, compliance, and risk management.

    - **Technical Team Leader, University of Pretoria Community Project (2012)**  
      Led a 14-member team delivering climate education to 900+ participants.
    """)

# -------------------- Contact --------------------
elif menu == "Contact":
    st.title("Contact")

    st.image(
        "contact researcher.jpg",
        caption="Research Collaboration & Contact",
        use_column_width=True
    )

    st.header("Get in Touch")
    st.write("**Zacharia Mogale**")

    st.write("✉️ mogalezach@gmail.com")
    st.write(
        "Open to collaborations in data science, analytics, machine learning, "
        "and meteorological research."
    )

# -------------------- Footer --------------------
st.markdown("---")
st.caption("Profile based on Professional Academic CV | Deployed with Streamlit | Updated January 2026")
