import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="AI-Powered Threat Hunting Dashboard", layout="wide")

st.title("🛡️ AI + ML Log-based Threat Hunting Dashboard")

# Load processed data
@st.cache_data
def load_data():
    return pd.read_csv("Detected_Anomalies_combined.csv")

df = load_data()

st.sidebar.header("🔍 Filters")
category = st.sidebar.multiselect("Filter by Category", options=df['category'].unique(), default=None)
anomaly_only = st.sidebar.checkbox("Show only anomalies", value=True)

filtered_df = df.copy()
if category:
    filtered_df = filtered_df[filtered_df['category'].isin(category)]
if anomaly_only:
    filtered_df = filtered_df[filtered_df['anomaly_any'] == 1]

st.markdown(f"### Showing {len(filtered_df)} log entries")

# Pie chart: anomaly categories
fig1 = px.pie(filtered_df, names='category', title='Anomaly Type Distribution', hole=0.4)
st.plotly_chart(fig1, use_container_width=True)

# Time trend
if 'timestamp' in df.columns:
    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
    daily = df.groupby(df['timestamp'].dt.date)['anomaly_any'].sum().reset_index()
    fig2 = px.line(daily, x='timestamp', y='anomaly_any', title='Daily Anomaly Count Trend', markers=True)
    st.plotly_chart(fig2, use_container_width=True)

# Table view
st.markdown("### 📄 Anomalous Log Entries")
st.dataframe(filtered_df[['timestamp', 'raw_log', 'category']].head(100))

# Download option
csv = filtered_df.to_csv(index=False).encode('utf-8')
st.download_button(
    "Download Filtered Logs",
    data=csv,
    file_name="Filtered_Threat_Logs.csv",
    mime="text/csv"
)
