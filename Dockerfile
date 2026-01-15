# Imagen
FROM python:3.13

# Directorio de trabajo donde realizaremos las acciones
# Copy local context to `/app` inside container (see .dockerignore)
WORKDIR /app
COPY . .

# Create virtualenv which will be copied into final container
ENV VIRTUAL_ENV=/app/.venv_docker
# Debemos tener mapeados en el path el entorno virtual
ENV PATH="$VIRTUAL_ENV/bin:$PATH" 
# Crear entorno virtual
RUN python3.13 -m venv $VIRTUAL_ENV

# Install app requirements and reflex inside virtualenv
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Arrancar backend
CMD ["reflex", "run", "--env", "prod", "--backend-only"]