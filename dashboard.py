import streamlit as st
import pandas as pd
from datetime import datetime
from src.agent import WaterIntakeAgent
from src.database import log_intake, get_intake_history


if "tracker_started" not in st.session_state:
    st.session_state.tracker_started = False

if not st.session_state.tracker_started:
    st.title("Welcome to AI Water Assistant")
    st.markdown(""""
                Track your daily hydration with the help of AI assistant.
                log your intake, get smart feedback and stay healthy effortlessly
             
                """)
    if st.button("Start Tracking"):
        st.session_state.tracker_started = True
        st.experimental_rerun()


else:
    st.title(" AI water Tracker Dashboard")

    st.sidebar.header("Log your water intake")
    UserId = st.sidebar.text_input("User Id", value="exampleuser")
    Intake = st.sidebar.number_input("intake in (ml)", min_value=0, step=100)

    if st.sidebar.button("Submit"):
        if UserId and Intake:
            log_intake(UserId, Intake)
            st.success(f"Logged {Intake} (ml) for {UserId}")

            agent = WaterIntakeAgent()
            feedback = agent.analyze_intake(Intake)
            st.info(f"AI feedback: {feedback}")
    
    st.markdown("---")

    st.header("Water Intake history")

    if UserId:
        history = get_intake_history(UserId)
        if history:
            dates = [datetime.strptime(row[1], "%Y-%m-%d") for row in history]
            values = [row[0] for row in history]

            df = pd.DataFrame({
                "Date": dates,
                "Water Intake (ml)": values
            })

            st.dataframe(df)
            st.line_chart(df, x="Date", y="Water Intake (ml)")

    else:
        st.warning("No Intake water data found. Please log your intake.")
