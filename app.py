import streamlit as st
import pandas as pd
import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

# =========================================
# SUPABASE CONFIG
# =========================================
SUPABASE_URL = st.secrets.get("SUPABASE_URL") or os.getenv("SUPABASE_URL")
SUPABASE_KEY = st.secrets.get("SUPABASE_KEY") or os.getenv("SUPABASE_KEY")
SUPABASE_SERVICE_KEY = st.secrets.get("SUPABASE_SERVICE_KEY") or os.getenv("SUPABASE_SERVICE_KEY")

# Auth client (anon key) — used for login/signup
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Service client — used for DB operations, bypasses RLS safely on server
supabase_service = create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)

# =========================================
# TRANSLATIONS
# =========================================
TRANSLATIONS = {
    "en": {
        "app_title": "💰 Personal Finance Tracker",
        "login": "Sign In",
        "signup": "Create Account",
        "email": "Email",
        "password": "Password",
        "fill_fields": "Please fill in email and password.",
        "login_error": "Login error: ",
        "account_created": "Account created successfully!",
        "account_created_info": "Now select 'Sign In' and log in with your email and password.",
        "signup_error": "Error creating account: ",
        "logout": "Sign Out",
        "logged_as": "Logged in as: ",
        "add_transaction": "➕ Add Transaction",
        "type": "Type",
        "income": "Income",
        "fixed_expense": "Fixed Expense",
        "variable_expense": "Variable Expense",
        "category": "Category",
        "currency": "Currency",
        "description": "Description (optional)",
        "amount": "Amount",
        "save": "Save",
        "amount_warning": "Amount must be greater than zero.",
        "saved": "Saved!",
        "no_transactions": "No transactions yet. Add one using the sidebar.",
        "dashboard": "📊 Dashboard",
        "summary_by_currency": "Summary by Currency",
        "summary_by_type": "Summary by Type",
        "expenses_by_category": "Expenses by Category",
        "income_by_category": "Income by Category",
        "no_expenses": "No expenses recorded.",
        "no_income": "No income recorded.",
        "transactions": "📋 Transactions",
        "filter_by_type": "Filter by type",
        "filter_by_currency": "Filter by currency",
        "delete_transaction": "🗑️ Delete Transaction",
        "select_transaction": "Select transaction",
        "delete": "Delete",
        "deleted": "Deleted!",
        "total_income": "💚 Income",
        "fixed_expenses": "🔴 Fixed Expenses",
        "variable_expenses": "🟠 Variable Expenses",
        "total_expenses": "🔴 Total Expenses",
        "balance": "🔵 Balance",
        "balances_by_currency": "💱 Balances by Currency",
        "all_currencies": "All",
        "income_categories": [
            "Salary", "Freelance", "Investments", "Rental Income",
            "Dividends", "Other Income"
        ],
        "fixed_categories": [
            "Rent", "Mortgage", "Health Insurance", "Internet",
            "Phone", "Streaming (Netflix, etc)", "Insurance",
            "School Tuition", "Other Fixed"
        ],
        "variable_categories": [
            "Food", "Transportation", "Entertainment", "Clothing",
            "Health / Pharmacy", "Groceries", "Restaurant",
            "Travel", "Gifts", "Other Variable"
        ],
    },
    "pt": {
        "app_title": "💰 Rastreador Financeiro Pessoal",
        "login": "Entrar",
        "signup": "Criar Conta",
        "email": "Email",
        "password": "Senha",
        "fill_fields": "Preencha email e senha.",
        "login_error": "Erro ao entrar: ",
        "account_created": "Conta criada com sucesso!",
        "account_created_info": "Agora selecione 'Entrar' e faça login com seu email e senha.",
        "signup_error": "Erro ao criar conta: ",
        "logout": "Sair",
        "logged_as": "Usuário: ",
        "add_transaction": "➕ Adicionar Transação",
        "type": "Tipo",
        "income": "Receita",
        "fixed_expense": "Despesa Fixa",
        "variable_expense": "Despesa Variável",
        "category": "Categoria",
        "currency": "Moeda",
        "description": "Descrição (opcional)",
        "amount": "Valor",
        "save": "Salvar",
        "amount_warning": "O valor deve ser maior que zero.",
        "saved": "Salvo!",
        "no_transactions": "Nenhuma transação ainda. Adicione uma pelo menu lateral.",
        "dashboard": "📊 Dashboard",
        "summary_by_currency": "Resumo por Moeda",
        "summary_by_type": "Resumo por Tipo",
        "expenses_by_category": "Despesas por Categoria",
        "income_by_category": "Receitas por Categoria",
        "no_expenses": "Sem despesas registradas.",
        "no_income": "Sem receitas registradas.",
        "transactions": "📋 Transações",
        "filter_by_type": "Filtrar por tipo",
        "filter_by_currency": "Filtrar por moeda",
        "delete_transaction": "🗑️ Deletar Transação",
        "select_transaction": "Selecione a transação",
        "delete": "Deletar",
        "deleted": "Deletado!",
        "total_income": "💚 Receitas",
        "fixed_expenses": "🔴 Despesas Fixas",
        "variable_expenses": "🟠 Despesas Variáveis",
        "total_expenses": "🔴 Total Despesas",
        "balance": "🔵 Saldo",
        "balances_by_currency": "💱 Saldos por Moeda",
        "all_currencies": "Todas",
        "income_categories": [
            "Salário", "Freelance", "Investimentos", "Aluguel recebido",
            "Dividendos", "Outros rendimentos"
        ],
        "fixed_categories": [
            "Aluguel", "Financiamento", "Plano de saúde", "Internet",
            "Telefone", "Streaming (Netflix, etc)", "Seguro",
            "Mensalidade escolar", "Outros fixos"
        ],
        "variable_categories": [
            "Alimentação", "Transporte", "Lazer", "Vestuário",
            "Saúde / Farmácia", "Supermercado", "Restaurante",
            "Viagem", "Presentes", "Outros variáveis"
        ],
    },
    "es": {
        "app_title": "💰 Rastreador Financiero Personal",
        "login": "Iniciar sesión",
        "signup": "Crear cuenta",
        "email": "Correo electrónico",
        "password": "Contraseña",
        "fill_fields": "Por favor ingrese correo y contraseña.",
        "login_error": "Error al iniciar sesión: ",
        "account_created": "¡Cuenta creada con éxito!",
        "account_created_info": "Ahora seleccione 'Iniciar sesión' e ingrese con su correo y contraseña.",
        "signup_error": "Error al crear cuenta: ",
        "logout": "Cerrar sesión",
        "logged_as": "Usuario: ",
        "add_transaction": "➕ Agregar Transacción",
        "type": "Tipo",
        "income": "Ingreso",
        "fixed_expense": "Gasto Fijo",
        "variable_expense": "Gasto Variable",
        "category": "Categoría",
        "currency": "Moneda",
        "description": "Descripción (opcional)",
        "amount": "Monto",
        "save": "Guardar",
        "amount_warning": "El monto debe ser mayor que cero.",
        "saved": "¡Guardado!",
        "no_transactions": "Sin transacciones aún. Agregue una desde el menú lateral.",
        "dashboard": "📊 Panel",
        "summary_by_currency": "Resumen por Moneda",
        "summary_by_type": "Resumen por Tipo",
        "expenses_by_category": "Gastos por Categoría",
        "income_by_category": "Ingresos por Categoría",
        "no_expenses": "Sin gastos registrados.",
        "no_income": "Sin ingresos registrados.",
        "transactions": "📋 Transacciones",
        "filter_by_type": "Filtrar por tipo",
        "filter_by_currency": "Filtrar por moneda",
        "delete_transaction": "🗑️ Eliminar Transacción",
        "select_transaction": "Seleccione la transacción",
        "delete": "Eliminar",
        "deleted": "¡Eliminado!",
        "total_income": "💚 Ingresos",
        "fixed_expenses": "🔴 Gastos Fijos",
        "variable_expenses": "🟠 Gastos Variables",
        "total_expenses": "🔴 Total Gastos",
        "balance": "🔵 Saldo",
        "balances_by_currency": "💱 Saldos por Moneda",
        "all_currencies": "Todas",
        "income_categories": [
            "Salario", "Freelance", "Inversiones", "Alquiler recibido",
            "Dividendos", "Otros ingresos"
        ],
        "fixed_categories": [
            "Alquiler", "Hipoteca", "Seguro médico", "Internet",
            "Teléfono", "Streaming (Netflix, etc)", "Seguro",
            "Colegiatura", "Otros fijos"
        ],
        "variable_categories": [
            "Alimentación", "Transporte", "Entretenimiento", "Ropa",
            "Salud / Farmacia", "Supermercado", "Restaurante",
            "Viaje", "Regalos", "Otros variables"
        ],
    },
}

LANGUAGE_OPTIONS = {"English": "en", "Português": "pt", "Español": "es"}
CURRENCIES = ["USD ($)", "EUR (€)", "BRL (R$)"]
CURRENCY_SYMBOLS = {"USD ($)": "$", "EUR (€)": "€", "BRL (R$)": "R$"}

# =========================================
# PAGE CONFIG
# =========================================
st.set_page_config(page_title="Personal Finance Tracker", layout="wide", page_icon="💰")

# =========================================
# SESSION STATE INIT
# =========================================
if "user" not in st.session_state:
    st.session_state.user = None
if "language" not in st.session_state:
    st.session_state.language = "en"

# =========================================
# LANGUAGE SELECTOR (always visible)
# =========================================
lang_col, spacer = st.columns([1, 7])
with lang_col:
    selected_lang_label = st.selectbox(
        "🌐",
        list(LANGUAGE_OPTIONS.keys()),
        index=list(LANGUAGE_OPTIONS.values()).index(st.session_state.language),
        label_visibility="collapsed"
    )
    st.session_state.language = LANGUAGE_OPTIONS[selected_lang_label]

T = TRANSLATIONS[st.session_state.language]

# =========================================
# AUTH FUNCTIONS
# =========================================
def login(email, password):
    try:
        response = supabase.auth.sign_in_with_password({"email": email, "password": password})
        st.session_state.user = response.user
        return True, None
    except Exception as e:
        return False, str(e)

def signup(email, password):
    try:
        supabase.auth.sign_up({"email": email, "password": password})
        return True, None
    except Exception as e:
        return False, str(e)

def logout():
    supabase.auth.sign_out()
    st.session_state.user = None
    st.rerun()

# =========================================
# AUTH SCREEN
# =========================================
if st.session_state.user is None:
    st.title(T["app_title"])
    st.divider()

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        mode = st.radio(
            "",
            [T["login"], T["signup"]],
            horizontal=True,
            label_visibility="collapsed"
        )
        email = st.text_input(T["email"])
        password = st.text_input(T["password"], type="password")

        if mode == T["login"]:
            if st.button(T["login"], use_container_width=True):
                if email and password:
                    ok, err = login(email, password)
                    if ok:
                        st.rerun()
                    else:
                        st.error(T["login_error"] + str(err))
                else:
                    st.warning(T["fill_fields"])
        else:
            if st.button(T["signup"], use_container_width=True):
                if email and password:
                    ok, err = signup(email, password)
                    if ok:
                        st.success(T["account_created"])
                        st.info(T["account_created_info"])
                    else:
                        st.error(T["signup_error"] + str(err))
                else:
                    st.warning(T["fill_fields"])

    st.stop()

# =========================================
# LOGGED IN
# =========================================
user_id = st.session_state.user.id

# =========================================
# DATA FUNCTIONS
# =========================================
def load_data():
    response = (
        supabase_service.table("transactions")
        .select("*")
        .eq("user_id", user_id)
        .order("created_at", desc=True)
        .execute()
    )
    data = response.data
    return pd.DataFrame(data) if data else pd.DataFrame(columns=[
        "id", "user_id", "type", "expense_type",
        "category", "currency", "description", "amount", "created_at"
    ])

def add_transaction(row):
    supabase_service.table("transactions").insert(row).execute()

def delete_transaction(row_id):
    supabase_service.table("transactions").delete().eq("id", row_id).execute()

# =========================================
# HEADER
# =========================================
col_title, col_logout = st.columns([8, 1])
with col_title:
    st.title(T["app_title"])
with col_logout:
    st.write("")
    if st.button(T["logout"]):
        logout()

st.caption(T["logged_as"] + st.session_state.user.email)

# =========================================
# SIDEBAR INPUT
# =========================================
st.sidebar.header(T["add_transaction"])

type_options = [T["income"], T["fixed_expense"], T["variable_expense"]]
transaction_type = st.sidebar.selectbox(T["type"], type_options)

if transaction_type == T["income"]:
    category = st.sidebar.selectbox(T["category"], T["income_categories"])
elif transaction_type == T["fixed_expense"]:
    category = st.sidebar.selectbox(T["category"], T["fixed_categories"])
else:
    category = st.sidebar.selectbox(T["category"], T["variable_categories"])

selected_currency = st.sidebar.selectbox(T["currency"], CURRENCIES)
description = st.sidebar.text_input(T["description"])
amount = st.sidebar.number_input(T["amount"], min_value=0.0, format="%.2f")

if st.sidebar.button(T["save"], use_container_width=True):
    if amount <= 0:
        st.sidebar.warning(T["amount_warning"])
    else:
        expense_type = None
        if transaction_type == T["fixed_expense"]:
            expense_type = "Fixed"
        elif transaction_type == T["variable_expense"]:
            expense_type = "Variable"

        add_transaction({
            "user_id": user_id,
            "type": transaction_type,
            "expense_type": expense_type,
            "category": category,
            "currency": selected_currency,
            "description": description,
            "amount": amount
        })
        st.sidebar.success(T["saved"])
        st.rerun()

# =========================================
# LOAD DATA
# =========================================
df = load_data()

if df.empty:
    st.info(T["no_transactions"])
    st.stop()

df["amount"] = pd.to_numeric(df["amount"], errors="coerce").fillna(0)

if "currency" not in df.columns:
    df["currency"] = "USD ($)"

# =========================================
# BALANCES BY CURRENCY
# =========================================
st.subheader(T["balances_by_currency"])

all_currencies = df["currency"].unique().tolist()

currency_cols = st.columns(len(all_currencies))

for i, curr in enumerate(all_currencies):
    sym = CURRENCY_SYMBOLS.get(curr, curr)
    curr_df = df[df["currency"] == curr]
    inc = curr_df[curr_df["type"] == T["income"]]["amount"].sum()
    exp = curr_df[curr_df["type"].isin([T["fixed_expense"], T["variable_expense"]])]["amount"].sum()
    bal = inc - exp
    with currency_cols[i]:
        st.markdown(f"**{curr}**")
        st.metric(T["total_income"], f"{sym} {inc:,.2f}")
        st.metric(T["total_expenses"], f"{sym} {exp:,.2f}")
        st.metric(T["balance"], f"{sym} {bal:,.2f}", delta=f"{sym} {bal:,.2f}")

st.divider()

# =========================================
# DASHBOARD
# =========================================
st.subheader(T["dashboard"])

tab1, tab2, tab3, tab4 = st.tabs([
    T["summary_by_currency"],
    T["summary_by_type"],
    T["expenses_by_category"],
    T["income_by_category"]
])

with tab1:
    rows = []
    for curr in all_currencies:
        sym = CURRENCY_SYMBOLS.get(curr, curr)
        curr_df = df[df["currency"] == curr]
        inc = curr_df[curr_df["type"] == T["income"]]["amount"].sum()
        fix = curr_df[curr_df["type"] == T["fixed_expense"]]["amount"].sum()
        var = curr_df[curr_df["type"] == T["variable_expense"]]["amount"].sum()
        rows.append({"Currency": curr, T["total_income"]: inc, T["fixed_expenses"]: fix, T["variable_expenses"]: var})
    summary_df = pd.DataFrame(rows).set_index("Currency")
    st.bar_chart(summary_df)

with tab2:
    curr_filter = st.selectbox(
        T["filter_by_currency"],
        [T["all_currencies"]] + all_currencies,
        key="tab2_curr"
    )
    tab2_df = df if curr_filter == T["all_currencies"] else df[df["currency"] == curr_filter]
    summary = pd.DataFrame({
        "Type": [T["income"], T["fixed_expense"], T["variable_expense"]],
        "Total": [
            tab2_df[tab2_df["type"] == T["income"]]["amount"].sum(),
            tab2_df[tab2_df["type"] == T["fixed_expense"]]["amount"].sum(),
            tab2_df[tab2_df["type"] == T["variable_expense"]]["amount"].sum(),
        ]
    })
    st.bar_chart(summary.set_index("Type"))

with tab3:
    curr_filter3 = st.selectbox(
        T["filter_by_currency"],
        [T["all_currencies"]] + all_currencies,
        key="tab3_curr"
    )
    tab3_df = df if curr_filter3 == T["all_currencies"] else df[df["currency"] == curr_filter3]
    expenses = tab3_df[tab3_df["type"].isin([T["fixed_expense"], T["variable_expense"]])]
    if not expenses.empty:
        by_cat = expenses.groupby("category")["amount"].sum().reset_index()
        by_cat.columns = [T["category"], "Total"]
        st.bar_chart(by_cat.set_index(T["category"]))
    else:
        st.info(T["no_expenses"])

with tab4:
    curr_filter4 = st.selectbox(
        T["filter_by_currency"],
        [T["all_currencies"]] + all_currencies,
        key="tab4_curr"
    )
    tab4_df = df if curr_filter4 == T["all_currencies"] else df[df["currency"] == curr_filter4]
    revenues = tab4_df[tab4_df["type"] == T["income"]]
    if not revenues.empty:
        by_cat = revenues.groupby("category")["amount"].sum().reset_index()
        by_cat.columns = [T["category"], "Total"]
        st.bar_chart(by_cat.set_index(T["category"]))
    else:
        st.info(T["no_income"])

st.divider()

# =========================================
# TRANSACTIONS TABLE
# =========================================
st.subheader(T["transactions"])

col_f1, col_f2 = st.columns(2)
with col_f1:
    filter_type = st.multiselect(T["filter_by_type"], type_options, default=type_options)
with col_f2:
    filter_currency = st.multiselect(T["filter_by_currency"], all_currencies, default=all_currencies)

filtered = df.copy()
if filter_type:
    filtered = filtered[filtered["type"].isin(filter_type)]
if filter_currency:
    filtered = filtered[filtered["currency"].isin(filter_currency)]

display_cols = [c for c in ["type", "expense_type", "category", "currency", "description", "amount", "created_at"] if c in filtered.columns]
st.dataframe(filtered[display_cols], use_container_width=True)

st.divider()

# =========================================
# DELETE
# =========================================
st.subheader(T["delete_transaction"])

if not df.empty:
    df["label"] = df.apply(
        lambda r: f"{r.get('category','?')} — {r.get('type','?')} — {CURRENCY_SYMBOLS.get(r.get('currency',''), '')} {float(r['amount']):,.2f} ({r.get('currency','')})",
        axis=1
    )
    options = dict(zip(df["label"], df["id"]))
    selected_label = st.selectbox(T["select_transaction"], list(options.keys()))
    selected_id = options[selected_label]

    if st.button(T["delete"], type="primary"):
        delete_transaction(selected_id)
        st.success(T["deleted"])
        st.rerun()