# Mi Página Web Personal

## Descripción

Portfolio personal desarrollado con un **stack moderno basado en Python**, pensado para mostrar no solo el resultado visual, sino también **criterio técnico, arquitectura y decisiones reales de despliegue**.

El proyecto combina frontend y backend desacoplados, integraciones externas y automatización, manteniendo un enfoque **simple, claro y profesional**.

---

## Tecnologías y herramientas

* **Python 3.13**
* **Reflex** (frontend)
* **FastAPI** (backend / API)
* **Supabase** (backend-as-a-service)
* **Docker** (containerización del backend)
* **GitHub Actions** (static build)

---

## Arquitectura (visión general)

* **Frontend**: aplicación web desplegada de forma independiente
* **Backend**: API desarrollada con FastAPI, containerizada con Docker
* **Integraciones externas**: servicios como Twitch
* **Servicios gestionados**: Supabase para persistencia y servicios backend

El frontend y el backend se encuentran **desacoplados**, permitiendo despliegue y evolución independientes.

---

## Despliegue

* **Frontend**: Vercel
* **Backend**: Railway (ejecutando la imagen definida en el `Dockerfile`)

---

## Autor

**Alejo Agasi**
