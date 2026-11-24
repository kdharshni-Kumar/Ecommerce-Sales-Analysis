
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="E-Commerce Dashboard", layout="wide")

# Load dataset
df = pd.read_csv("analyzed_sales.csv")

df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Dashboard title
st.title("🛒 E-Commerce Sales Analysis Dashboard")
st.write("Sales Performance and Business Insights")

# Key metrics
total_revenue = df["Revenue"].sum()
total_orders = df["Order_ID"].nunique()
total_customers = df["Customer_ID"].nunique()

col1, col2, col3 = st.columns(3)

col1.metric("Total Revenue", f"₹{total_revenue:,.0f}")
col2.metric("Total Orders", total_orders)
col3.metric("Total Customers", total_customers)

st.divider()

# Best selling products
st.subheader("Top Selling Products")

product_sales = df.groupby("Product_Name")["Quantity"].sum().sort_values(ascending=False)
st.bar_chart(product_sales)

# Category revenue
st.subheader("Category-wise Revenue")

category_sales = df.groupby("Category")["Revenue"].sum()
st.bar_chart(category_sales)

# Monthly revenue
st.subheader("Monthly Revenue")

monthly_sales = (
    df.assign(Month=df["Order_Date"].dt.to_period("M").dt.to_timestamp())
      .groupby("Month")["Revenue"]
      .sum()
      .sort_index()
)
st.write(monthly_sales)
st.bar_chart(monthly_sales)

st.success("E-Commerce Dashboard Loaded Successfully!")
