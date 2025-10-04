#!/bin/bash

# Script de configuración automática del proyecto
echo "Configurando proyecto Supply Chain Analytics..."

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo "Python3 no está instalado. Por favor instala Python 3.8 o superior."
    exit 1
fi

# Crear entorno virtual
echo "Creando entorno virtual..."
python3 -m venv venv

# Activar entorno virtual
echo "Activando entorno virtual..."
source venv/bin/activate

# Instalar dependencias
echo "Instalando dependencias..."
pip install -r requirements.txt

# Cargar datos en la base de datos
echo "Cargando datos en la base de datos..."
python src/load_database_sqlite.py

echo "Configuración completada!"
echo ""
echo "Para ejecutar el dashboard:"
echo "1. source venv/bin/activate"
echo "2. streamlit run dashboard.py"
echo ""
echo "El dashboard se abrirá en: http://localhost:8501"
