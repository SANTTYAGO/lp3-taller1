# CREADO POR: SANTIAGO VALENCIA AGUDELO

# API de Videos

Esta es una API RESTful para gestión de videos, desarrollada con Flask, Flask-RESTful y SQLAlchemy.

## Descripción

El proyecto implementa una API simple para gestionar información sobre videos, permitiendo:

- Crear nuevos videos
- Consultar videos existentes
- Actualizar información de videos
- Eliminar videos

Cada video tiene los siguientes atributos:
- ID: Identificador único del video
- Nombre: Título del video
- Vistas: Número de reproducciones
- Likes: Número de "me gusta"

## Estructura del Proyecto

```
lp3-taller1
├── app.py                  # Archivo principal para ejecutar la aplicación
├── config.py               # Configuración de la aplicación
├── models/
│   ├── __init__.py         # Inicializa el módulo models
│   └── video.py            # Modelo de datos para Video
├── resources/
│   ├── __init__.py         # Inicializa el módulo resources
│   └── video.py            # Recursos y rutas para Video
├── database.db             # Base de datos SQLite (generada automáticamente)
├── requirements.txt        # Dependencias del proyecto
└── README.md               # Documentación del proyecto
```

## Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## Ejecución

1. Iniciar el servidor de desarrollo:
   ```
   python app.py
   ```

2. El servidor estará disponible en `http://localhost:5000`

## Uso de la API

### Obtener un video

```
GET /api/videos/{id}
```

Respuesta:
```json
{
  "id": 1,
  "name": "Tutorial de Python",
  "views": 1500,
  "likes": 120
}
```

### Crear un nuevo video

```
PUT /api/videos/{id}
```

Cuerpo de la solicitud:
```json
{
  "name": "Tutorial de Flask",
  "views": 0,
  "likes": 0
}
```

### Actualizar un video

```
PATCH /api/videos/{id}
```

Cuerpo de la solicitud (campos opcionales):
```json
{
  "views": 2500,
  "likes": 200
}
```

### Eliminar un video

```
DELETE /api/videos/{id}
```

## Documentación de la API

### Integración de Swagger/OpenAPI

La API está documentada utilizando Swagger/OpenAPI. Esto permite visualizar y probar los endpoints de manera interactiva.

#### Configuración de Swagger

Se ha integrado Swagger utilizando el paquete `flask-swagger-ui`. La documentación se encuentra disponible en el endpoint `/swagger`.

1. **Ruta de la documentación**:  
   Accede a la documentación interactiva en:  
   [http://localhost:5000/swagger](http://localhost:5000/swagger)

2. **Archivo de configuración**:  
   La especificación de la API está definida en el archivo `static/swagger.json`. Este archivo contiene la descripción de los endpoints, parámetros, y ejemplos de respuestas.

#### Ejemplo de Configuración en `app.py`:

```python
# Swagger UI
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
```

### Ejemplos de Uso

#### Obtener un video

```
GET /api/videos/{id}
```

**Parámetros**:
- `id` (path): ID del video que se desea obtener.

**Respuesta Exitosa (200)**:
```json
{
  "id": 1,
  "name": "Tutorial de Python",
  "views": 1500,
  "likes": 120
}
```

**Error (404)**:
```json
{
  "message": "Video no encontrado"
}
```

#### Crear un nuevo video

```
PUT /api/videos/{id}
```

**Parámetros**:
- `id` (path): ID del video que se desea crear.

**Cuerpo de la Solicitud**:
```json
{
  "name": "Tutorial de Flask",
  "views": 0,
  "likes": 0
}
```

**Respuesta Exitosa (201)**:
```json
{
  "id": 1,
  "name": "Tutorial de Flask",
  "views": 0,
  "likes": 0
}
```

**Error (409)**:
```json
{
  "message": "El video ya existe"
}
```

#### Actualizar un video

```
PATCH /api/videos/{id}
```

**Parámetros**:
- `id` (path): ID del video que se desea actualizar.

**Cuerpo de la Solicitud** (campos opcionales):
```json
{
  "views": 2500,
  "likes": 200
}
```

**Respuesta Exitosa (200)**:
```json
{
  "id": 1,
  "name": "Tutorial de Flask",
  "views": 2500,
  "likes": 200
}
```

**Error (404)**:
```json
{
  "message": "Video no encontrado"
}
```

#### Eliminar un video

```
DELETE /api/videos/{id}
```

**Parámetros**:
- `id` (path): ID del video que se desea eliminar.

**Respuesta Exitosa (204)**:
Sin contenido.

**Error (404)**:
```json
{
  "message": "Video no encontrado"
}
```

### Cómo Probar la Documentación

1. Ejecuta la aplicación:
   ```bash
   python app.py
   ```

2. Abre un navegador y accede a:  
   [http://localhost:5000/swagger](http://localhost:5000/swagger)

Desde esta interfaz, puedes probar los endpoints directamente y visualizar las respuestas de la API.
