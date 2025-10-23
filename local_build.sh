# Crea y activa un entorno virtual
python3 -m venv .venv
source .venv/bin/activate

# Instala las dependencias
pip install --upgrade pip
pip install -r requirements.txt

# Instala las dependencias de npm y construye Tailwind CSS
npm install
npm install -g postcss-cli
npm run build

# Elimina los artefactos de construcción existentes si es necesario
rm -rf public

# Proceso de construcción de Reflex con debugging
echo "=== Iniciando reflex init ==="
reflex init --loglevel debug
if [ $? -ne 0 ]; then
    echo "ERROR: reflex init falló"
    exit 1
fi

echo "=== Copiando devicon a .web/public ==="
cp -r node_modules/devicon .web/public/
if [ $? -ne 0 ]; then
    echo "ERROR: No se pudo copiar devicon"
    exit 1
fi

echo "=== Iniciando reflex export ==="
reflex export --frontend-only --loglevel debug
if [ $? -ne 0 ]; then
    echo "ERROR: reflex export falló"
    exit 1
fi

echo "=== Verificando si frontend.zip fue creado ==="
if [ ! -f "frontend.zip" ]; then
    echo "ERROR: frontend.zip no fue creado"
    echo "Archivos en el directorio actual:"
    ls -la
    exit 1
fi

# Descomprime los artefactos de construcción del frontend
echo "=== Descomprimiendo frontend.zip ==="
unzip frontend.zip -d public
if [ $? -ne 0 ]; then
    echo "ERROR: No se pudo descomprimir frontend.zip"
    exit 1
fi

rm -f frontend.zip
echo "=== Build completado exitosamente ==="