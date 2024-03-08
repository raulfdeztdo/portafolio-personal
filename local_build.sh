# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Build the frontend (assuming you have a separate build step)
# Example using npm:
npm install
npm run build

# Clear existing build artifacts if needed
rm -rf public

# Reflex build process
reflex init
reflex export --frontend-only

# Create the zip file
zip -r frontend.zip public