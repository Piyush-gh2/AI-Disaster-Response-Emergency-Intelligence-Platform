import streamlit as st

from src.agents import run_disaster_ai
from src.rag import load_knowledge, build_index, retrieve

st.title("🚨 AI Disaster Response & Emergency Intelligence Platform")

query = st.text_input("Ask Emergency Insight")

if st.button("Analyze Disaster Risk"):

    df, prediction, risk, explanation = run_disaster_ai()

    st.subheader("📊 Disaster Dataset")
    st.dataframe(df)

    st.subheader("📈 Disaster Forecast")
    st.write(f"Predicted Disaster Severity: {prediction:.2f}")

    st.subheader("⚠️ Emergency Risk Detection")
    st.write(risk)

    st.subheader("🧠 Explainable AI Insight")
    st.write(explanation)

    st.line_chart(df.set_index("region")["flood_level"])

    # RAG
    docs = load_knowledge()
    index = build_index(docs)

    if query:

        insights = retrieve(query, docs, index)

        st.subheader("🔎 Emergency Intelligence Insights")

        for i in insights:
            st.write(i)