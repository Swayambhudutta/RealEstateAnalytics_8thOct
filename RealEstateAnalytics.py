import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# -----------------------------
# Generate synthetic ESG data
# -----------------------------
years = list(range(2019, 2024))
subsidiaries = ['Subsidiary A', 'Subsidiary B', 'Subsidiary C']
assets = ['Asset 1', 'Asset 2', 'Asset 3']
phases = ['Building', 'Construction', 'Post-Construction']

def generate_data():
    data = []
    for year in years:
        for sub in subsidiaries:
            for asset in assets:
                for phase in phases:
                    data.append({
                        'Year': year,
                        'Subsidiary': sub,
                        'Asset': asset,
                        'Phase': phase,
                        'Energy Usage': np.random.randint(100, 500),
                        'Energy Use Intensity': np.random.uniform(80, 150),
                        'Waste Recycling %': np.random.uniform(30, 90),
                        'Water Usage': np.random.randint(1000, 5000),
                        'Embodied Carbon': np.random.randint(100, 1000),
                        'Certification Score': np.random.uniform(50, 100),
                        'Indoor Air Quality': np.random.uniform(70, 100),
                        'Tenant Satisfaction': np.random.uniform(60, 100),
                        'ROI': np.random.uniform(5, 15)
                    })
    return pd.DataFrame(data)

df = generate_data()

# -----------------------------
# Sidebar Filters
# -----------------------------
st.sidebar.title("Filters")
selected_subsidiary = st.sidebar.selectbox("Select Subsidiary", ['All'] + subsidiaries)
selected_asset = st.sidebar.selectbox("Select Asset", ['All'] + assets)
selected_year = st.sidebar.selectbox("Select Year", ['All'] + years)

filtered_df = df.copy()
if selected_subsidiary != 'All':
    filtered_df = filtered_df[filtered_df['Subsidiary'] == selected_subsidiary]
if selected_asset != 'All':
    filtered_df = filtered_df[filtered_df['Asset'] == selected_asset]
if selected_year != 'All':
    filtered_df = filtered_df[filtered_df['Year'] == selected_year]

# -----------------------------
# Tabs for Dashboards
# -----------------------------
tab1, tab2, tab3, tab4 = st.tabs(["Building Phase", "Construction Phase", "Post-Construction", "Financial Impact"])

# -----------------------------
# Function to Display Charts
# -----------------------------
def display_charts(data, simulation_value):
    col1, col2 = st.columns(2)
    with col1:
        fig1 = px.bar(data, x='Year', y='Energy Usage', color='Subsidiary', title='Energy Usage Over Years')
        st.plotly_chart(fig1, use_container_width=True)

        fig2 = px.pie(data, names='Asset', values='Waste Recycling %', hole=0.4, title='Waste Recycling % by Asset')
        st.plotly_chart(fig2, use_container_width=True)

    with col2:
        fig3 = px.line(data, x='Year', y='Water Usage', color='Asset', title='Water Usage Trend')
        fig3.update_traces(mode="lines+markers")
        st.plotly_chart(fig3, use_container_width=True)

        fig4 = px.area(data, x='Year', y='Embodied Carbon', color='Subsidiary', title='Embodied Carbon Over Time')
        st.plotly_chart(fig4, use_container_width=True)

    # Full-width charts
    fig5 = px.line(data, x='Year', y='Energy Use Intensity', color='Asset', title='Energy Use Intensity')
    fig5.update_traces(mode="lines+markers")
    st.plotly_chart(fig5, use_container_width=True)

    fig6 = px.scatter(data, x='ROI', y='Embodied Carbon', color='Subsidiary', size='Certification Score', title='ROI vs Carbon Impact')
    st.plotly_chart(fig6, use_container_width=True)

    # Simulation impact chart
    simulated_values = [simulation_value * 10 + np.random.randint(0, 10) for _ in data['Year']]
    fig7 = px.line(x=data['Year'], y=simulated_values, title='Simulated Carbon Reduction')
    fig7.update_traces(mode="lines+markers")
    st.plotly_chart(fig7, use_container_width=True)

# -----------------------------
# Building Phase Dashboard
# -----------------------------
with tab1:
    st.header("Building Phase ESG Analytics")
    investment_slider = st.slider("Investment in Sustainable Materials (%)", 0, 100, 50)
    display_charts(filtered_df[filtered_df['Phase'] == 'Building'], investment_slider)

# -----------------------------
# Construction Phase Dashboard
# -----------------------------
with tab2:
    st.header("Construction Phase ESG Analytics")
    energy_slider = st.slider("Renewable Energy Usage (%)", 0, 100, 50)
    display_charts(filtered_df[filtered_df['Phase'] == 'Construction'], energy_slider)

# -----------------------------
# Post-Construction Dashboard
# -----------------------------
with tab3:
    st.header("Post-Construction ESG Analytics")
    smart_slider = st.slider("Smart Energy System Investment (%)", 0, 100, 50)
    display_charts(filtered_df[filtered_df['Phase'] == 'Post-Construction'], smart_slider)

# -----------------------------
# Financial Impact Dashboard
# -----------------------------
with tab4:
    st.header("Financial & Certification Impact")
    capex_slider = st.slider("ESG CapEx Increase (%)", 0, 100, 50)
    display_charts(filtered_df, capex_slider)
