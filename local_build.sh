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

# Proceso de construcción de Reflex
reflex init
reflex export --frontend-only

# Descomprime los artefactos de construcción del frontend
unzip frontend.zip -d public
rm -f frontend.zip