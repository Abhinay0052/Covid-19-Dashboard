import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Page Configuration
st.set_page_config(page_title="COVID-19 Analysis Dashboard", layout="wide")
sns.set_theme(style="whitegrid")

st.title("🦠 COVID-19 Country-Wise Data Analysis")

# -----------------------------
# Data Loading & Preprocessing
# -----------------------------
@st.cache_data
def load_and_clean_data():
    file_path = "country_wise_latest.csv"
    df = pd.read_csv(file_path)
    
    # 1. Clean data
    df = df.drop_duplicates()
    numeric_columns = df.select_dtypes(include=np.number).columns
    df[numeric_columns] = df[numeric_columns].fillna(0)
    
    # 2. Add derived columns
    df["Recovery Rate"] = (df["Recovered"] / df["Confirmed"] * 100).replace([np.inf, -np.inf], 0).fillna(0)
    df["Death Rate"] = (df["Deaths"] / df["Confirmed"] * 100).replace([np.inf, -np.inf], 0).fillna(0)
    df["Death to Recovery Ratio"] = (df["Deaths"] / df["Recovered"]).replace([np.inf, -np.inf], 0).fillna(0)
    
    return df

df = load_and_clean_data()

# -----------------------------
# Sidebar: Interactive Filtering
# -----------------------------
st.sidebar.header("🔍 Custom Data Filter")

selected_region = st.sidebar.multiselect(
    "Select WHO Region:", 
    options=df["WHO Region"].unique(), 
    default=df["WHO Region"].unique()
)

min_confirmed = st.sidebar.number_input("Min Confirmed Cases:", min_value=0, value=100000)
min_deaths = st.sidebar.number_input("Min Deaths:", min_value=0, value=1000)
min_recovery = st.sidebar.slider("Min Recovery Rate (%):", 0, 100, 70)

# Filter Data
filtered_df = df[
    (df["WHO Region"].isin(selected_region)) &
    (df["Confirmed"] >= min_confirmed) &
    (df["Deaths"] >= min_deaths) &
    (df["Recovery Rate"] >= min_recovery)
]

# -----------------------------
# Global Key Metrics
# -----------------------------
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Confirmed", f"{df['Confirmed'].sum():,}")
col2.metric("Total Deaths", f"{df['Deaths'].sum():,}")
col3.metric("Total Recovered", f"{df['Recovered'].sum():,}")
col4.metric("Total Active", f"{df['Active'].sum():,}")

st.markdown("---")

# -----------------------------
# Visualizations & Sections
# -----------------------------
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Top Rankings", 
    "🌍 WHO Region Analysis", 
    "📈 Scatter Plots", 
    "🔥 Heatmap", 
    "📋 Filtered Data"
])

with tab1:
    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("Top 10 Countries by Confirmed Cases")
        top_10_confirmed = df.sort_values(by="Confirmed", ascending=False).head(10)
        fig1, ax1 = plt.subplots(figsize=(8, 5))
        sns.barplot(data=top_10_confirmed, x="Confirmed", y="Country/Region", ax=ax1)
        st.pyplot(fig1)

    with col_b:
        st.subheader("Top 10 Countries by Deaths")
        top_10_deaths = df.sort_values(by="Deaths", ascending=False).head(10)
        fig2, ax2 = plt.subplots(figsize=(8, 5))
        sns.barplot(data=top_10_deaths, x="Deaths", y="Country/Region", ax=ax2)
        st.pyplot(fig2)

with tab2:
    st.subheader("COVID-19 Statistics by WHO Region")
    region_data = df.groupby("WHO Region")[["Confirmed", "Deaths", "Recovered", "Active"]].sum()
    fig3, ax3 = plt.subplots(figsize=(10, 5))
    region_data.plot(kind="bar", ax=ax3)
    plt.xticks(rotation=45)
    st.pyplot(fig3)

with tab3:
    st.subheader("Confirmed Cases vs Deaths by Region")
    fig4, ax4 = plt.subplots(figsize=(10, 6))
    sns.scatterplot(
        data=df,
        x="Confirmed",
        y="Deaths",
        hue="WHO Region",
        size="Active",
        sizes=(40, 400),
        alpha=0.8,
        ax=ax4
    )
    st.pyplot(fig4)

with tab4:
    st.subheader("Correlation Heatmap")
    corr_cols = [
        "Confirmed", "Deaths", "Recovered", "Active", 
        "New cases", "New deaths", "New recovered", 
        "Deaths / 100 Cases", "Recovered / 100 Cases", 
        "1 week change", "1 week % increase"
        ]
    import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Page Configuration
st.set_page_config(page_title="COVID-19 Analysis Dashboard", layout="wide")
sns.set_theme(style="whitegrid")

st.title("🦠 COVID-19 Country-Wise Data Analysis")

# -----------------------------
# Data Loading & Preprocessing
# -----------------------------
@st.cache_data
def load_and_clean_data():
    file_path = "country_wise_latest.csv"
    df = pd.read_csv(file_path)
    
    # 1. Clean data
    df = df.drop_duplicates()
    numeric_columns = df.select_dtypes(include=np.number).columns
    df[numeric_columns] = df[numeric_columns].fillna(0)
    
    # 2. Add derived columns
    df["Recovery Rate"] = (df["Recovered"] / df["Confirmed"] * 100).replace([np.inf, -np.inf], 0).fillna(0)
    df["Death Rate"] = (df["Deaths"] / df["Confirmed"] * 100).replace([np.inf, -np.inf], 0).fillna(0)
    df["Death to Recovery Ratio"] = (df["Deaths"] / df["Recovered"]).replace([np.inf, -np.inf], 0).fillna(0)
    
    return df

df = load_and_clean_data()

# -----------------------------
# Sidebar: Interactive Filtering
# -----------------------------
st.sidebar.header("🔍 Custom Data Filter")

selected_region = st.sidebar.multiselect(
    "Select WHO Region:", 
    options=df["WHO Region"].unique(), 
    default=df["WHO Region"].unique()
)

min_confirmed = st.sidebar.number_input("Min Confirmed Cases:", min_value=0, value=100000)
min_deaths = st.sidebar.number_input("Min Deaths:", min_value=0, value=1000)
min_recovery = st.sidebar.slider("Min Recovery Rate (%):", 0, 100, 70)

# Filter Data
filtered_df = df[
    (df["WHO Region"].isin(selected_region)) &
    (df["Confirmed"] >= min_confirmed) &
    (df["Deaths"] >= min_deaths) &
    (df["Recovery Rate"] >= min_recovery)
]

# -----------------------------
# Global Key Metrics
# -----------------------------
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Confirmed", f"{df['Confirmed'].sum():,}")
col2.metric("Total Deaths", f"{df['Deaths'].sum():,}")
col3.metric("Total Recovered", f"{df['Recovered'].sum():,}")
col4.metric("Total Active", f"{df['Active'].sum():,}")

st.markdown("---")

# -----------------------------
# Visualizations & Sections
# -----------------------------
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Top Rankings", 
    "🌍 WHO Region Analysis", 
    "📈 Scatter Plots", 
    "🔥 Heatmap", 
    "📋 Filtered Data"
])

with tab1:
    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("Top 10 Countries by Confirmed Cases")
        top_10_confirmed = df.sort_values(by="Confirmed", ascending=False).head(10)
        fig1, ax1 = plt.subplots(figsize=(8, 5))
        sns.barplot(data=top_10_confirmed, x="Confirmed", y="Country/Region", ax=ax1)
        st.pyplot(fig1)

    with col_b:
        st.subheader("Top 10 Countries by Deaths")
        top_10_deaths = df.sort_values(by="Deaths", ascending=False).head(10)
        fig2, ax2 = plt.subplots(figsize=(8, 5))
        sns.barplot(data=top_10_deaths, x="Deaths", y="Country/Region", ax=ax2)
        st.pyplot(fig2)

with tab2:
    st.subheader("COVID-19 Statistics by WHO Region")
    region_data = df.groupby("WHO Region")[["Confirmed", "Deaths", "Recovered", "Active"]].sum()
    fig3, ax3 = plt.subplots(figsize=(10, 5))
    region_data.plot(kind="bar", ax=ax3)
    plt.xticks(rotation=45)
    st.pyplot(fig3)

with tab3:
    st.subheader("Confirmed Cases vs Deaths by Region")
    fig4, ax4 = plt.subplots(figsize=(10, 6))
    sns.scatterplot(
        data=df,
        x="Confirmed",
        y="Deaths",
        hue="WHO Region",
        size="Active",
        sizes=(40, 400),
        alpha=0.8,
        ax=ax4
    )
    st.pyplot(fig4)

with tab4:
    st.subheader("Correlation Heatmap")
    corr_cols = [
        "Confirmed", "Deaths", "Recovered", "Active", 
        "New cases", "New deaths", "New recovered", 
        "Deaths / 100 Cases", "Recovered / 100 Cases", 
        "1 week change", "1 week % increase"
    ]
    fig5, ax5 = plt.subplots(figsize=(10, 7))
    sns.heatmap(df[corr_cols].corr(), annot=True, cmap="coolwarm", fmt=".2f", ax=ax5)
    st.pyplot(fig5)

with tab5:
    st.subheader("Filtered Data Preview")
    st.dataframe(filtered_df)
    
    # CSV Download Button
    csv_data = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Filtered Data CSV",
        data=csv_data,
        file_name="filtered_covid_data.csv",
        mime="text/csv"
    )
    
    fig5, ax5 = plt.subplots(figsize=(10, 7))
    sns.heatmap(df[corr_cols].corr(), annot=True, cmap="coolwarm", fmt=".2f", ax=ax5)
    st.pyplot(fig5)

with tab5:
    st.subheader("Filtered Data Preview")
    st.dataframe(filtered_df)
    
    # CSV Download Button
    csv_data = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Filtered Data CSV",
        data=csv_data,
        file_name="filtered_covid_data.csv",
        mime="text/csv"
    )
