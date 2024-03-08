# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Build the frontend (assuming you have a separate build step)
# Example using npm:
npm install
npm run build
pwd
ls -l
# Clear existing build artifacts if needed
rm -rf public

# Reflex build process
reflex init
reflex export --frontend-only
pwd
ls -l

# Create the zip file
zip -r frontend.zip public