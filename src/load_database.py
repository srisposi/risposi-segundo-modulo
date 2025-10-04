import pandas as pd
from sqlalchemy import create_engine, text

# Configuración de conexión
DB_USER = "postgres"
DB_PASS = "tu_password"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "supply_chain_db"

# URL de conexión
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Conectar al motor de PostgreSQL
engine = create_engine(DATABASE_URL)

# Cargar el CSV
data_path = "data/supply_chain_data.csv"
df = pd.read_csv(data_path)

# Renombrar columnas para usar nombres válidos en SQL
df.columns = (
    df.columns.str.lower()
    .str.replace(" ", "_")
    .str.replace("-", "_")
)

# Crear la tabla en PostgreSQL
schema_sql = """
CREATE TABLE IF NOT EXISTS supply_chain (
    id SERIAL PRIMARY KEY,
    sku VARCHAR(20),
    product_type VARCHAR(50),
    price DECIMAL,
    availability INT,
    number_of_products_sold INT,
    revenue_generated DECIMAL,
    customer_demographics VARCHAR(50),
    stock_levels INT,
    lead_times INT,
    order_quantities INT,
    shipping_times INT,
    shipping_carriers VARCHAR(50),
    shipping_costs DECIMAL,
    supplier_name VARCHAR(100),
    location VARCHAR(100),
    lead_time INT,
    production_volumes INT,
    manufacturing_lead_time INT,
    manufacturing_costs DECIMAL,
    inspection_results VARCHAR(50),
    defect_rates FLOAT,
    transportation_modes VARCHAR(50),
    routes VARCHAR(50),
    costs DECIMAL
);
"""

with engine.begin() as conn:
    # Limpiar datos existentes
    conn.execute(text("DROP TABLE IF EXISTS supply_chain"))
    print("Datos anteriores eliminados.")
    
    # Crear tabla nueva
    conn.execute(text(schema_sql))
    print("Tabla 'supply_chain' creada correctamente.")

# Cargar datos desde pandas
df.to_sql("supply_chain", engine, if_exists="append", index=False)
print(f"{len(df)} registros insertados correctamente.")
