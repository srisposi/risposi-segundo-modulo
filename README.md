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

## Desarrollo

### Agregar Nuevas Visualizaciones
1. Editar `dashboard.py`
2. Agregar nueva sección con `st.subheader()`
3. Crear gráfico con Plotly
4. Usar `st.plotly_chart()` para mostrar

### Modificar Filtros
1. Editar sección de sidebar en `dashboard.py`
2. Agregar nuevos filtros con `st.multiselect()`
3. Aplicar filtros al DataFrame

### Agregar Métricas
1. Calcular nueva métrica
2. Mostrar con `st.metric()`
3. Agregar en sección de KPIs

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

## Próximas Mejoras

- [ ] Agregar análisis de tendencias temporales
- [ ] Implementar alertas automáticas
- [ ] Exportar reportes en PDF
- [ ] Integración con APIs externas
- [ ] Dashboard móvil responsive

## Contribución

1. Fork el proyecto
2. Crear rama para nueva feature (`git checkout -b feature/nueva-feature`)
3. Commit cambios (`git commit -am 'Agregar nueva feature'`)
4. Push a la rama (`git push origin feature/nueva-feature`)
5. Crear Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver `LICENSE` para más detalles.

## Contacto

Para preguntas o soporte, contactar a: [tu-email@ejemplo.com]

---

**Nota**: Este proyecto fue desarrollado como parte del segundo módulo de Programación Avanzada.