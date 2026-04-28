import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import os

# Set page config
st.set_page_config(page_title="E-Commerce Dashboard", layout="wide")

# Custom styling
st.markdown("""
    <style>
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .header-title {
        color: #1f77b4;
        font-size: 2.5em;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    # Get the path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, 'main_data.csv')
    df = pd.read_csv(data_path)
    df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
    df['order_delivered_customer_date'] = pd.to_datetime(df['order_delivered_customer_date'])
    return df

df = load_data()

# Header
st.markdown("<h1 class='header-title'>📊 E-Commerce Dashboard</h1>", unsafe_allow_html=True)
st.markdown("---")

# Sidebar filters
st.sidebar.header("🔍 Filters")
selected_state = st.sidebar.multiselect(
    "Select Customer State(s):",
    options=df['customer_state'].unique(),
    default=df['customer_state'].unique()[:5]
)

selected_category = st.sidebar.multiselect(
    "Select Product Category(ies):",
    options=df['product_category_name_english'].unique(),
    default=df['product_category_name_english'].unique()[:5]
)

selected_status = st.sidebar.multiselect(
    "Select Order Status:",
    options=df['order_status'].unique(),
    default=df['order_status'].unique()
)

# Validate filter selections
if not selected_state:
    st.sidebar.warning("⚠️ Please select at least one Customer State!")
    selected_state = df['customer_state'].unique()[:5]
    
if not selected_category:
    st.sidebar.warning("⚠️ Please select at least one Product Category!")
    selected_category = df['product_category_name_english'].unique()[:5]
    
if not selected_status:
    st.sidebar.warning("⚠️ Please select at least one Order Status!")
    selected_status = df['order_status'].unique()

# Apply filters
try:
    filtered_df = df[
        (df['customer_state'].isin(selected_state)) &
        (df['product_category_name_english'].isin(selected_category)) &
        (df['order_status'].isin(selected_status))
    ]
    
    # Check if filtered_df is empty
    if filtered_df.empty:
        st.error("❌ No data available with the selected filters. Please adjust your selections.")
        filtered_df = df  # Use unfiltered data as fallback
        
except Exception as e:
    st.error(f"❌ Error applying filters: {str(e)}")
    filtered_df = df

# Key Metrics
st.subheader("📈 Key Metrics")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("Total Orders", f"{len(filtered_df):,}")

with col2:
    total_revenue = filtered_df['price'].sum()
    st.metric("Total Revenue (R$)", f"{total_revenue:,.2f}")

with col3:
    avg_rating = filtered_df['avg_review_score'].mean()
    st.metric("Avg Rating", f"{avg_rating:.2f}/5.0")

with col4:
    avg_delay = filtered_df['delay_days'].mean()
    st.metric("Avg Delay (days)", f"{avg_delay:.2f}")

with col5:
    on_time_pct = (1 - filtered_df['is_late'].sum() / len(filtered_df)) * 100
    st.metric("On-Time Delivery %", f"{on_time_pct:.1f}%")

st.markdown("---")

# Row 1: Charts
col1, col2 = st.columns(2)

with col1:
    st.subheader("📦 Orders by Category")
    category_orders = filtered_df['product_category_name_english'].value_counts().head(10)
    fig, ax = plt.subplots(figsize=(10, 6))
    category_orders.plot(kind='barh', ax=ax, color='steelblue')
    ax.set_xlabel("Number of Orders")
    ax.set_ylabel("Category")
    st.pyplot(fig)

with col2:
    st.subheader("🗺️ Orders by State")
    state_orders = filtered_df['customer_state'].value_counts().head(10)
    fig, ax = plt.subplots(figsize=(10, 6))
    state_orders.plot(kind='barh', ax=ax, color='coral')
    ax.set_xlabel("Number of Orders")
    ax.set_ylabel("State")
    st.pyplot(fig)

st.markdown("---")

# Row 2: Charts
col1, col2 = st.columns(2)

with col1:
    st.subheader("💰 Revenue Distribution")
    fig, ax = plt.subplots(figsize=(8, 6))
    filtered_df['price'].hist(bins=50, ax=ax, color='green', edgecolor='black', alpha=0.7)
    ax.set_xlabel("Price (R$)")
    ax.set_ylabel("Frequency")
    ax.set_title("Price Distribution")
    st.pyplot(fig)

with col2:
    st.subheader("⭐ Rating Distribution")
    rating_dist = filtered_df['avg_review_score'].value_counts().sort_index()
    fig, ax = plt.subplots(figsize=(8, 6))
    rating_dist.plot(kind='bar', ax=ax, color='gold', edgecolor='black')
    ax.set_xlabel("Rating Score")
    ax.set_ylabel("Number of Orders")
    ax.set_title("Customer Ratings Distribution")
    plt.xticks(rotation=0)
    st.pyplot(fig)

st.markdown("---")

# Row 3: Charts
col1, col2 = st.columns(2)

with col1:
    st.subheader("✅ Order Status")
    status_dist = filtered_df['order_status'].value_counts()
    fig, ax = plt.subplots(figsize=(8, 6))
    colors = ['#2ecc71', '#e74c3c', '#f39c12', '#95a5a6']
    ax.pie(status_dist, labels=status_dist.index, autopct='%1.1f%%', colors=colors, startangle=90)
    ax.set_title("Order Status Distribution")
    st.pyplot(fig)

with col2:
    st.subheader("📅 Orders Over Time")
    monthly_orders = filtered_df.groupby(filtered_df['order_purchase_timestamp'].dt.to_period('M')).size()
    fig, ax = plt.subplots(figsize=(10, 6))
    monthly_orders.plot(ax=ax, marker='o', color='purple', linewidth=2)
    ax.set_xlabel("Month")
    ax.set_ylabel("Number of Orders")
    ax.set_title("Orders Trend Over Time")
    plt.xticks(rotation=45)
    st.pyplot(fig)

st.markdown("---")

# Row 4: Delivery Performance
col1, col2 = st.columns(2)

with col1:
    st.subheader("🚚 On-Time vs Late Delivery")
    delivery_status = filtered_df['is_late'].value_counts()
    delivery_labels = ['On-Time', 'Late']
    fig, ax = plt.subplots(figsize=(8, 6))
    colors_delivery = ['#2ecc71', '#e74c3c']
    ax.pie([delivery_status.get(False, 0), delivery_status.get(True, 0)], 
           labels=delivery_labels, autopct='%1.1f%%', colors=colors_delivery, startangle=90)
    ax.set_title("Delivery Performance")
    st.pyplot(fig)

with col2:
    st.subheader("⏱️ Delivery Delay Distribution")
    fig, ax = plt.subplots(figsize=(8, 6))
    filtered_df['delay_days'].hist(bins=50, ax=ax, color='orange', edgecolor='black', alpha=0.7)
    ax.set_xlabel("Delay (days)")
    ax.set_ylabel("Frequency")
    ax.set_title("Delivery Delay Distribution")
    st.pyplot(fig)

st.markdown("---")

# Data Table
st.subheader("📋 Detailed Data")
if st.checkbox("Show raw data"):
    st.dataframe(
        filtered_df[[
            'order_id', 'product_category_name_english', 'price', 
            'order_status', 'avg_review_score', 'delay_days', 'customer_state'
        ]].head(100),
        use_container_width=True
    )

# Footer
st.caption("© 2026 E-Commerce Dashboard. Muhammad Daffa Alghifari")
