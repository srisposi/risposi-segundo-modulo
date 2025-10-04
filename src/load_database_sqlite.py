import pandas as pd
from sqlalchemy import create_engine, text

# Configuración de conexión SQLite
DB_PATH = "data/supply_chain.db"
DATABASE_URL = f"sqlite:///{DB_PATH}"

# Conectar al motor de SQLite
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

# Crear la tabla en SQLite
schema_sql = """
CREATE TABLE IF NOT EXISTS supply_chain (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
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

# Verificar datos
with engine.begin() as conn:
    result = conn.execute(text("SELECT COUNT(*) as total FROM supply_chain"))
    count = result.fetchone()[0]
    print(f"Total de registros en la base de datos: {count}")
