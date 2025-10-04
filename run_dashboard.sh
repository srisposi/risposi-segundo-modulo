#!/bin/bash

# Script para ejecutar el dashboard
echo "Iniciando Supply Chain Dashboard..."

# Verificar si el entorno virtual existe
if [ ! -d "venv" ]; then
    echo "Entorno virtual no encontrado. Ejecuta primero: ./setup.sh"
    exit 1
fi

# Activar entorno virtual
source venv/bin/activate

# Verificar si la base de datos existe
if [ ! -f "data/supply_chain.db" ]; then
    echo "Base de datos no encontrada. Cargando datos..."
    python src/load_database_sqlite.py
fi

# Ejecutar dashboard
echo "Iniciando dashboard..."
streamlit run dashboard.py
