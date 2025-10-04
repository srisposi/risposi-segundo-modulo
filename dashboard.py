import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# Configuración de Streamlit
st.set_page_config(
    page_title="Supply Chain Dashboard",
    page_icon="📊",
    layout="wide"
)

# Configuración de la página
st.set_page_config(
    page_title="Supply Chain Dashboard",
    page_icon="📊",
    layout="wide"
)

# Título principal
st.title("Supply Chain Analytics Dashboard")
st.markdown("---")

# Conectar a la base de datos SQLite
@st.cache_data
def load_data():
    engine = create_engine("sqlite:///data/supply_chain.db")
    query = "SELECT * FROM supply_chain"
    df = pd.read_sql(query, engine)
    return df

# Cargar datos
try:
    df = load_data()
    
    # Sidebar con filtros
    st.sidebar.header("Filtros")
    
    # Filtro por tipo de producto
    product_types = df['product_type'].unique()
    selected_products = st.sidebar.multiselect(
        "Tipo de Producto",
        product_types,
        default=product_types
    )

