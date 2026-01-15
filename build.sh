python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
rm -rf public
export REFLEX_LOGLEVEL=default
# Configurar la URL del backend ANTES de inicializar Reflex
export API_URL=https://alejoagasiweb.up.railway.app
reflex init
# Exportar frontend con la URL del backend (sin puerto, Railway lo maneja automáticamente)
reflex export --frontend-only
unzip frontend.zip -d public
rm -f frontend.zip

# Corregir las URLs en el archivo reflex-env generado
# Reflex no está usando backend_url del rxconfig.py, así que lo corregimos manualmente
BACKEND_URL="alejoagasiweb.up.railway.app"
for file in public/assets/reflex-env-*.js; do
    if [ -f "$file" ]; then
        # Reemplazar localhost:8000 con la URL de Railway
        # Reemplazar http://localhost:8000 con https://alejoagasiweb.up.railway.app
        sed -i "s|http://localhost:8000|https://${BACKEND_URL}|g" "$file"
        # Reemplazar ws://localhost:8000 con wss://alejoagasiweb.up.railway.app
        sed -i "s|ws://localhost:8000|wss://${BACKEND_URL}|g" "$file"
        echo "✓ Corregido: $file"
    fi
done

deactivate
