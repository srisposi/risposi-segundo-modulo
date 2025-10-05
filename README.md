# Supply Chain Analytics Dashboard

Dashboard interactivo para análisis de datos de cadena de suministro desarrollado con Python, SQLite y Streamlit.

## Descripción del Proyecto

Este proyecto implementa un sistema completo de análisis de datos de supply chain que incluye:

- **Carga de datos** desde CSV a base de datos SQLite
- **Dashboard interactivo** con visualizaciones dinámicas
- **Análisis de KPIs** en tiempo real
- **Filtros interactivos** para exploración de datos

## Características

### Dashboard Features
- **Métricas KPI**: Revenue total, productos vendidos, precio promedio, tasa de defectos
- **Visualizaciones**: Gráficos de barras, dispersión, líneas, pie charts
- **Filtros interactivos**: Por tipo de producto, ubicación, proveedor
- **Análisis geográfico**: Tendencias por ubicación
- **Análisis de proveedores**: Ranking por revenue
- **Análisis logístico**: Costos por modo de transporte

### Base de Datos
- **SQLite** para desarrollo y pruebas
- **PostgreSQL** para producción (opcional)
- **Limpieza automática** de datos en cada ejecución
- **Esquema optimizado** para análisis

## Instalación y Configuración

### Prerrequisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### 1. Clonar el Repositorio
```bash
git clone <url-del-repositorio>
cd risposi-segundo-modulo
```

### 2. Crear Entorno Virtual
```bash
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 4. Cargar Datos en la Base de Datos
```bash
python src/load_database_sqlite.py
```

### 5. Ejecutar Dashboard
```bash
streamlit run dashboard.py
```

El dashboard se abrirá automáticamente en tu navegador en `http://localhost:8501`

## Estructura del Proyecto

```
risposi-segundo-modulo/
├── README.md                    # Documentación del proyecto
├── requirements.txt             # Dependencias de Python
├── .gitignore                  # Archivos a ignorar en Git
├── dashboard.py                # Dashboard principal
├── data/
│   ├── supply_chain_data.csv   # Datos originales
│   └── supply_chain.db         # Base de datos SQLite (generada)
├── src/
│   ├── load_database.py        # Script para PostgreSQL
│   └── load_database_sqlite.py # Script para SQLite
└── venv/                       # Entorno virtual (no versionado)
```

## Scripts Disponibles

### Carga de Datos
- **`src/load_database_sqlite.py`**: Carga datos en SQLite (recomendado)
- **`src/load_database.py`**: Carga datos en PostgreSQL (requiere instalación)

### Dashboard
- **`dashboard.py`**: Dashboard interactivo con Streamlit

## Análisis de Datos

### Métricas Principales
- **Revenue Total**: Suma de ingresos generados
- **Productos Vendidos**: Cantidad total de unidades vendidas
- **Precio Promedio**: Precio promedio de productos
- **Tasa de Defectos**: Porcentaje de productos defectuosos

### Visualizaciones
- **Revenue por Tipo de Producto**: Análisis de rentabilidad por categoría
- **Precio vs Defectos**: Correlación entre precio y calidad
- **Tendencias Geográficas**: Performance por ubicación
- **Top Proveedores**: Ranking por revenue generado
- **Análisis Logístico**: Costos por modo de transporte

### Filtros Interactivos
- **Tipo de Producto**: Haircare, Skincare, Cosmetics
- **Ubicación**: Mumbai, Kolkata, Delhi, Bangalore
- **Proveedor**: Supplier 1-5

## Solución de Problemas

### Error: "No module named 'streamlit'"
```bash
source venv/bin/activate
pip install streamlit
```

### Error: "Database not found"
```bash
python src/load_database_sqlite.py
```

### Error: "Port already in use"
```bash
streamlit run dashboard.py --server.port 8502
```