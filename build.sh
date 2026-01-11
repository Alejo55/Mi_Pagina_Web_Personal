pip install --upgrade pip
pip install -r requirements.txt
rm -rf public
reflex init
export REFLEX_API_URL=https://289c1fc7-fb0e-4c12-8471-4106c46a6d05.fly.dev
reflex export --frontend-only
unzip frontend.zip -d public
rm -f frontend.zip