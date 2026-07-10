# Task API

API REST para gestión de tareas, construida con **FastAPI** y **SQLAlchemy**.
Proyecto de mi portafolio como desarrollador backend Python.

## Stack

- Python 3.11+
- FastAPI
- SQLAlchemy (ORM)
- SQLite (desarrollo) → PostgreSQL (siguiente iteración)
- Pydantic (validación de datos)

## Cómo correrlo

\`\`\`bash
# 1. Crear entorno virtual
python -m venv venv
source venv/Scripts/activate      # En Mac/Linux: source venv/bin/activate

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Levantar el servidor
uvicorn app.main:app --reload
\`\`\`

La API queda disponible en `http://127.0.0.1:8000` y la documentación
interactiva (Swagger) en `http://127.0.0.1:8000/docs`.

## Endpoints

| Método | Ruta            | Descripción              |
|--------|-----------------|---------------------------|
| POST   | /tasks          | Crear una tarea           |
| GET    | /tasks          | Listar tareas              |
| GET    | /tasks/{id}     | Obtener una tarea          |
| PUT    | /tasks/{id}     | Actualizar una tarea       |
| DELETE | /tasks/{id}     | Eliminar una tarea         |

## Roadmap (próximas mejoras)

- [ ] Migrar de SQLite a PostgreSQL
- [ ] Dockerizar la app y la base de datos (docker-compose)
- [ ] Autenticación con JWT (usuarios propietarios de sus tareas)
- [ ] Tests automáticos con pytest
- [ ] Deploy en Railway/Render
- [ ] CI/CD con GitHub Actions

## Autor

Gabriel Figueroa — Ingeniero de Sistemas