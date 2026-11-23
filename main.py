import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
print("All Libraries Imported Successfully!")

products = pd.read_csv("products.csv")
customers = pd.read_csv("customers.csv")
orders = pd.read_csv("orders.csv")

print("\nPRODUCTS DATA")
print(products.head())

print("\nCUSTOMERS DATA")
print(customers.head())

print("\nORDERS DATA")
print(orders.head())

print("MISSING VALUES")

print("Products:")
print(products.isnull().sum())

print("Customers:")
print(customers.isnull().sum())

print("Orders:")
print(orders.isnull().sum())

print("DUPLICATE VALUES")

print("Products:", products.duplicated().sum())

print("Customers:", customers.duplicated().sum())

print("Orders:", orders.duplicated().sum())

print("PRODUCTS DATA TYPES")
print(products.dtypes)

print("CUSTOMERS DATA TYPES")
print(customers.dtypes)

print("ORDERS DATA TYPES")
print(orders.dtypes)

orders['Order_Date'] = pd.to_datetime(orders['Order_Date'])

print("UPDATED ORDER DATE TYPE")
print(orders['Order_Date'].dtype)

print("UPDATED DATA TYPES")
print(products.dtypes)
print(customers.dtypes)
print(orders.dtypes)


sales = pd.merge(orders, products, on="Product_ID", how="left")
print("MERGED SALES DATA")
print(sales.head())

#calculate revenue

sales["Revenue"] = sales["Quantity"] * sales["Price"]
print("SALES WITH REVENUE")
print(sales[["Order_ID", "Product_Name", "Quantity", "Price", "Revenue"]].head())

#Total Revenue

total_revenue = sales["Revenue"].sum()
print("TOTAL REVENUE:", total_revenue)

# Best-Selling Products

best_selling = sales.groupby("Product_Name")["Quantity"].sum()
best_selling = best_selling.sort_values(ascending=False)
print("BEST-SELLING PRODUCTS")
print(best_selling.head(5))

# Category-wise Sales Analysis

category_sales = sales.groupby("Category")["Revenue"].sum()
category_sales = category_sales.sort_values(ascending=False)
print("CATEGORY-WISE SALES")
print(category_sales)

# Monthly Sales Analysis

sales["Month"] = sales["Order_Date"].dt.month_name()
monthly_sales = sales.groupby("Month")["Revenue"].sum()
print("MONTHLY SALES")
print(monthly_sales)

# Monthly Sales Bar Chart
monthly_sales.plot(kind="bar", figsize=(10, 5))
plt.title("Monthly Sales Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Top 5 Customers Analysis

customer_sales = sales.groupby("Customer_ID")["Revenue"].sum()
customer_sales = customer_sales.sort_values(ascending=False)
print("TOP 5 CUSTOMERS")
print(customer_sales.head(5))

# Customer Name and Sales Analysis

customer_data = pd.merge(
    sales,
    customers,
    on="Customer_ID",
    how="left"
)

customer_names = customer_data.groupby("Customer_Name")["Revenue"].sum()
customer_names = customer_names.sort_values(ascending=False)
print("CUSTOMER NAME-WISE SALES")
print(customer_names.head(5))

# Customer Order Count

order_count = sales.groupby("Customer_ID")["Order_ID"].count()
order_count = order_count.sort_values(ascending=False)
print("CUSTOMER ORDER COUNT")
print(order_count.head(5))

# Sales Summary

print("SALES SUMMARY")
print("Total Orders:", sales["Order_ID"].nunique())
print("Total Products Sold:", sales["Quantity"].sum())
print("Total Revenue:", sales["Revenue"].sum())
print("Average Order Revenue:", sales["Revenue"].mean())


# Product-wise Revenue Analysis

product_revenue = sales.groupby("Product_Name")["Revenue"].sum()
product_revenue = product_revenue.sort_values(ascending=False)
print("PRODUCT-WISE REVENUE")
print(product_revenue.head(10))

# Category-wise Product Count

category_count = products.groupby("Category")["Product_ID"].count()
print("CATEGORY-WISE PRODUCT COUNT")
print(category_count)

# Average Price by Category

average_price = products.groupby("Category")["Price"].mean()
print("AVERAGE PRICE BY CATEGORY")
print(average_price)

# City-wise Sales Analysis

city_sales = customer_data.groupby("City")["Revenue"].sum()
city_sales = city_sales.sort_values(ascending=False)
print("CITY-WISE SALES")
print(city_sales)

# City-wise Sales Bar Chart

city_sales.plot(kind="bar", figsize=(8, 5))
plt.title("City-wise Sales Revenue")
plt.xlabel("City")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Category-wise Revenue Pie Chart

category_sales.plot(
    kind="pie",
    autopct="%1.1f%%",
    figsize=(7, 7)
)
plt.title("Category-wise Revenue Distribution")
plt.ylabel("")
plt.show()

# Correlation Analysis

correlation = sales[["Quantity", "Price", "Revenue"]].corr()
print("CORRELATION MATRIX")
print(correlation)

# Correlation Heatmap

sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Sales Correlation Heatmap")
plt.tight_layout()
plt.show()

# Highest Revenue Orders

top_orders = sales.nlargest(5, "Revenue")
print("TOP 5 HIGHEST REVENUE ORDERS")
print(top_orders[["Order_ID", "Product_Name", "Quantity", "Revenue"]])

# Save Analyzed Sales Data

sales.to_csv("analyzed_sales.csv", index=False)
print("Sales data saved successfully!")

# Final steps

print("\n===== E-COMMERCE SALES ANALYSIS =====")

print("Total Orders:", sales["Order_ID"].nunique())
print("Total Products Sold:", sales["Quantity"].sum())
print("Total Revenue:", sales["Revenue"].sum())

print("\nTop 5 Selling Products:")
print(best_selling.head(5))

print("\nTop 5 Customers:")
print(customer_sales.head(5))

print("\nCategory-wise Revenue:")
print(category_sales)

# Business Insights

print("\n===== BUSINESS INSIGHTS =====")

print("Best Selling Product:", best_selling.idxmax())
print("Highest Selling Quantity:", best_selling.max())

print("Top Revenue Category:", category_sales.idxmax())
print("Category Revenue:", category_sales.max())

print("Top Customer ID:", customer_sales.idxmax())
print("Customer Purchase:", customer_sales.max())

print("Best Sales Month:", monthly_sales.idxmax())
print("Monthly Revenue:", monthly_sales.max())

# Top 5 Best-Selling Products Chart

top_products = best_selling.head(5)
top_products.plot(kind="bar", figsize=(8, 5))
plt.title("Top 5 Best-Selling Products")
plt.xlabel("Product Name")
plt.ylabel("Quantity Sold")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Monthly Revenue Trend

monthly_revenue = sales.groupby(
    sales["Order_Date"].dt.to_period("M")
)["Revenue"].sum()
monthly_revenue.plot(
    kind="line",
    marker="o",
    figsize=(10, 5)
)
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Top 5 Customers Sales Chart

top_customers = customer_sales.head(5)
top_customers.plot(kind="bar", figsize=(8, 5))
plt.title("Top 5 Customers by Revenue")
plt.xlabel("Customer ID")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Create Business Insights Report

with open("business_insights.txt", "w", encoding="utf-8") as file:

    file.write("E-COMMERCE SALES ANALYSIS REPORT\n\n")

    file.write(f"Total Revenue: {sales['Revenue'].sum()}\n")

    file.write(f"Best Selling Product: {best_selling.idxmax()}\n")

    file.write(f"Top Revenue Category: {category_sales.idxmax()}\n")

    file.write(f"Top Customer ID: {customer_sales.idxmax()}\n")

    file.write("\nTop 5 Selling Products:\n")
    file.write(best_selling.head(5).to_string())

    file.write("\n\nTop 5 Customers:\n")
    file.write(customer_sales.head(5).to_string())

print("Business Insights Report Created Successfully!")

max_quantity = best_selling.max()
top_selling_products = best_selling[
    best_selling == max_quantity
]
print("\nBEST SELLING PRODUCTS")
print(top_selling_products)

max_quantity = best_selling.max()

top_selling_products = best_selling[
    best_selling == max_quantity
]

with open("business_insights.txt", "w", encoding="utf-8") as file:
    file.write("E-COMMERCE SALES ANALYSIS REPORT\n\n")
    file.write(f"Total Revenue: {sales['Revenue'].sum()}\n")

    file.write("Best Selling Products:\n")
    file.write(top_selling_products.to_string() + "\n")

    file.write(f"Top Revenue Category: {category_sales.idxmax()}\n")
    file.write(f"Top Customer ID: {customer_sales.idxmax()}\n")

    file.write("\nTop 5 Selling Products:\n")
    file.write(best_selling.head(5).to_string())

    file.write("\n\nTop 5 Customers:\n")
    file.write(customer_sales.head(5).to_string())

print("Business Insights Report Created Successfully!")