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
deactivate
