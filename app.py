import streamlit as st
import pandas as pd
import plotly.express as px
import os

# =========================================
# PAGE CONFIG
# =========================================
st.set_page_config(
    page_title="Personal Finance Tracker",
    page_icon="💰",
    layout="wide"
)

# =========================================
# TITLE
# =========================================
st.title("💰 Personal Finance Tracker")
st.write("Track your personal finances professionally.")

# =========================================
# CURRENCY SELECTION
# =========================================
currency = st.selectbox(
    "Select Currency",
    ["USD ($)", "EUR (€)", "BRL (R$)"]
)

currency_symbol = {
    "USD ($)": "$",
    "EUR (€)": "€",
    "BRL (R$)": "R$"
}[currency]

# =========================================
# CSV CONFIGURATION
# =========================================
csv_file = "finances.csv"

required_columns = [
    "Type",
    "Expense Type",
    "Category",
    "Description",
    "Amount"
]

# Create file if it doesn't exist
if not os.path.exists(csv_file):
    df = pd.DataFrame(columns=required_columns)
    df.to_csv(csv_file, index=False)

# Read CSV
df = pd.read_csv(csv_file)

# Fix old column names automatically
df.columns = [col.replace("_", " ") for col in df.columns]

# Add missing columns if necessary
for col in required_columns:
    if col not in df.columns:
        df[col] = ""

# =========================================
# SIDEBAR FORM
# =========================================
st.sidebar.header("Add Transaction")

transaction_type = st.sidebar.selectbox(
    "Transaction Type",
    ["Income", "Expense"]
)

# =========================================
# INCOME CATEGORIES
# =========================================
income_categories = [
    "Salary",
    "Bonus",
    "Freelance",
    "Business Income",
    "Investments",
    "Dividends",
    "Rental Income",
    "Side Hustle",
    "Scholarship",
    "Cashback",
    "Other Income"
]

# =========================================
# FIXED EXPENSES
# =========================================
fixed_expenses = [
    "Rent / Mortgage",
    "Electricity",
    "Water",
    "Internet",
    "Phone Bill",
    "Health Insurance",
    "Car Insurance",
    "Life Insurance",
    "Loan Payment",
    "Tuition",
    "Gym Membership",
    "Streaming Services",
    "Subscriptions",
    "Transportation Pass",
    "Childcare",
    "Taxes",
    "Retirement Contribution",
    "Domestic Employee",
    "Security Service",
    "Pet Care",
    "Other Fixed Expense"
]

# =========================================
# VARIABLE EXPENSES
# =========================================
variable_expenses = [
    "Groceries",
    "Restaurants",
    "Coffee",
    "Fast Food",
    "Transportation",
    "Fuel",
    "Uber / Taxi",
    "Travel",
    "Shopping",
    "Clothing",
    "Beauty",
    "Healthcare",
    "Medicine",
    "Entertainment",
    "Movies",
    "Gaming",
    "Education",
    "Books",
    "Courses",
    "Gifts",
    "Emergency",
    "Home Maintenance",
    "Electronics",
    "Sports",
    "Hobbies",
    "Charity",
    "Other Variable Expense"
]

# =========================================
# FORM LOGIC
# =========================================
expense_type = ""

if transaction_type == "Income":

    category = st.sidebar.selectbox(
        "Income Category",
        income_categories
    )

else:

    expense_type = st.sidebar.selectbox(
        "Expense Type",
        ["Fixed Expense", "Variable Expense"]
    )

    if expense_type == "Fixed Expense":
        category = st.sidebar.selectbox(
            "Expense Category",
            fixed_expenses
        )
    else:
        category = st.sidebar.selectbox(
            "Expense Category",
            variable_expenses
        )

description = st.sidebar.text_input("Description")

amount = st.sidebar.number_input(
    "Amount",
    min_value=0.0,
    format="%.2f"
)

# =========================================
# SAVE BUTTON
# =========================================
if st.sidebar.button("Save Transaction"):

    new_data = pd.DataFrame({
        "Type": [transaction_type],
        "Expense Type": [expense_type],
        "Category": [category],
        "Description": [description],
        "Amount": [amount]
    })

    df = pd.concat([df, new_data], ignore_index=True)

    df.to_csv(csv_file, index=False)

    st.sidebar.success("Transaction saved successfully!")

# =========================================
# ENSURE NUMERIC
# =========================================
df["Amount"] = pd.to_numeric(
    df["Amount"],
    errors="coerce"
).fillna(0)

# =========================================
# FINANCIAL METRICS
# =========================================
income_total = df[df["Type"] == "Income"]["Amount"].sum()

fixed_total = df[
    df["Expense Type"] == "Fixed Expense"
]["Amount"].sum()

variable_total = df[
    df["Expense Type"] == "Variable Expense"
]["Amount"].sum()

expense_total = fixed_total + variable_total

balance = income_total - expense_total

# =========================================
# METRIC CARDS
# =========================================
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Income",
    f"{currency_symbol} {income_total:,.2f}"
)

col2.metric(
    "Fixed Expenses",
    f"{currency_symbol} {fixed_total:,.2f}"
)

col3.metric(
    "Variable Expenses",
    f"{currency_symbol} {variable_total:,.2f}"
)

col4.metric(
    "Balance",
    f"{currency_symbol} {balance:,.2f}"
)

st.divider()

# =========================================
# CHARTS
# =========================================
chart_col1, chart_col2 = st.columns(2)

# Expense Distribution
expense_df = df[df["Type"] == "Expense"]

if not expense_df.empty:

    pie_chart = px.pie(
        expense_df,
        names="Category",
        values="Amount",
        title="Expense Distribution"
    )

    chart_col1.plotly_chart(
        pie_chart,
        use_container_width=True
    )

# Income Distribution
income_df = df[df["Type"] == "Income"]

if not income_df.empty:

    income_chart = px.bar(
        income_df,
        x="Category",
        y="Amount",
        title="Income Sources"
    )

    chart_col2.plotly_chart(
        income_chart,
        use_container_width=True
    )

st.divider()

# =========================================
# SAVED TRANSACTIONS
# =========================================
st.subheader("Saved Transactions")

st.dataframe(
    df,
    use_container_width=True
)

# =========================================
# DOWNLOAD BUTTON
# =========================================
csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Financial Data",
    data=csv,
    file_name="financial_data.csv",
    mime="text/csv"
)