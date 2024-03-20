# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Install npm dependencies and build Tailwind CSS
npm install
npm run build

# Clear existing build artifacts if needed
rm -rf public

# Reflex build process
reflex init
reflex export --frontend-only

# Unzip frontend build artifacts
unzip frontend.zip -d public
rm -f frontend.zip