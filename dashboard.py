import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sqlalchemy import create_engine, text

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
    
    # Filtro por ubicación
    locations = df['location'].unique()
    selected_locations = st.sidebar.multiselect(
        "Ubicación",
        locations,
        default=locations
    )
    
    # Filtro por proveedor
    suppliers = df['supplier_name'].unique()
    selected_suppliers = st.sidebar.multiselect(
        "Proveedor",
        suppliers,
        default=suppliers
    )
    
    # Aplicar filtros
    filtered_df = df[
        (df['product_type'].isin(selected_products)) &
        (df['location'].isin(selected_locations)) &
        (df['supplier_name'].isin(selected_suppliers))
    ]
    
    # Métricas principales
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_revenue = filtered_df['revenue_generated'].sum()
        st.metric("Revenue Total", f"${total_revenue:,.2f}")
    
    with col2:
        total_products = filtered_df['number_of_products_sold'].sum()
        st.metric("Productos Vendidos", f"{total_products:,}")
    
    with col3:
        avg_price = filtered_df['price'].mean()
        st.metric("Precio Promedio", f"${avg_price:.2f}")
    
    with col4:
        defect_rate = filtered_df['defect_rates'].mean()
        st.metric("Tasa de Defectos", f"{defect_rate:.2%}")
    
    st.markdown("---")
    
    # Gráficos principales
    col1, col2 = st.columns(2)
    
    with col1:
        # Gráfico de barras: Revenue por tipo de producto
        revenue_by_type = filtered_df.groupby('product_type')['revenue_generated'].sum().reset_index()
        fig1 = px.bar(
            revenue_by_type, 
            x='product_type', 
            y='revenue_generated',
            title="Revenue por Tipo de Producto",
            color='product_type'
        )
        fig1.update_layout(showlegend=False)
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        # Gráfico de dispersión: Precio vs Defectos
        fig2 = px.scatter(
            filtered_df, 
            x='price', 
            y='defect_rates',
            color='product_type',
            title="Precio vs Tasa de Defectos",
            hover_data=['supplier_name', 'location']
        )
        st.plotly_chart(fig2, use_container_width=True)
    
    # Gráfico de líneas: Tendencias por ubicación
    st.subheader("Tendencias por Ubicación")
    trends_data = filtered_df.groupby(['location', 'product_type'])['revenue_generated'].sum().reset_index()
    fig3 = px.line(
        trends_data, 
        x='location', 
        y='revenue_generated',
        color='product_type',
        title="Revenue por Ubicación y Tipo de Producto"
    )
    st.plotly_chart(fig3, use_container_width=True)
    
    # Análisis de proveedores
    col1, col2 = st.columns(2)
    
    with col1:
        # Top proveedores por revenue
        top_suppliers = filtered_df.groupby('supplier_name')['revenue_generated'].sum().sort_values(ascending=False).head(10)
        fig4 = px.bar(
            x=top_suppliers.values,
            y=top_suppliers.index,
            orientation='h',
            title="Top 10 Proveedores por Revenue"
        )
        fig4.update_layout(yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig4, use_container_width=True)
    
    with col2:
        # Análisis de costos de transporte
        transport_costs = filtered_df.groupby('transportation_modes')['shipping_costs'].mean().reset_index()
        fig5 = px.pie(
            transport_costs,
            values='shipping_costs',
            names='transportation_modes',
            title="Distribución de Costos por Modo de Transporte"
        )
        st.plotly_chart(fig5, use_container_width=True)
    
    # Tabla de datos
    st.subheader("Datos Detallados")
    st.dataframe(
        filtered_df[['sku', 'product_type', 'price', 'revenue_generated', 'supplier_name', 'location', 'defect_rates']],
        use_container_width=True
    )
    
    # Información del dataset
    st.sidebar.markdown("---")
    st.sidebar.markdown("**Información del Dataset**")
    st.sidebar.write(f"Total registros: {len(df)}")
    st.sidebar.write(f"Registros filtrados: {len(filtered_df)}")
    st.sidebar.write(f"Tipos de producto: {len(product_types)}")
    st.sidebar.write(f"Ubicaciones: {len(locations)}")
    st.sidebar.write(f"Proveedores: {len(suppliers)}")

except Exception as e:
    st.error(f"Error al cargar los datos: {str(e)}")
    st.info("Asegúrate de que la base de datos existe y contiene datos. Ejecuta primero: python src/load_database_sqlite.py")

