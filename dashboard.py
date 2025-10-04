import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# Configuración de la página
st.set_page_config(
    page_title="Supply Chain Dashboard",
    page_icon="📊",
    layout="wide"
)

# Título principal
st.title("📊 Supply Chain Analytics Dashboard")
st.markdown("---")

# Conectar a la base de datos SQLite
@st.cache_data
def load_data():
    engine = create_engine("sqlite:///data/supply_chain.db")
    query = "SELECT * FROM supply_chain"
    df = pd.read_sql(query, engine)
    return df
