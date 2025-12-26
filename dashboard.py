import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Setup Page
st.set_page_config(page_title="E-Commerce Dashboard", layout="wide")
sns.set(style='dark')

# 1. Load Data
df = pd.read_csv("all_data.zip")
df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])

# 2. Sidebar (Filter Waktu)
with st.sidebar:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png") # Opsional: Logo
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=df['order_purchase_timestamp'].min(),
        max_value=df['order_purchase_timestamp'].max(),
        value=[df['order_purchase_timestamp'].min(), df['order_purchase_timestamp'].max()]
    )

# Filter data berdasarkan tanggal dari sidebar
main_df = df[(df["order_purchase_timestamp"] >= str(start_date)) & 
                (df["order_purchase_timestamp"] <= str(end_date))]

# 3. Main Page
st.title('E-Commerce Analysis')

# Menampilkan Metric Sederhana
col1, col2 = st.columns(2)
with col1:
    total_orders = main_df.order_id.nunique()
    st.metric("Total Pesanan", value=total_orders)
with col2:
    total_revenue = main_df.payment_value.sum()
    st.metric("Total Pendapatan", value=f"Rp {total_revenue:,.2f}")

# 4. Visualisasi
st.subheader("10 Kategori Produk Terpopuler")
top_10 = main_df['product_category_name_english'].value_counts().head(10)
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x=top_10.values, y=top_10.index, palette="Blues_r", ax=ax)
st.pyplot(fig)

st.subheader("Tren Pesanan Bulanan")
monthly_orders = main_df.resample(rule='M', on='order_purchase_timestamp').agg({"order_id": "nunique"})
fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(monthly_orders.index, monthly_orders["order_id"], marker='o', color="#1f77b4")
st.pyplot(fig)
