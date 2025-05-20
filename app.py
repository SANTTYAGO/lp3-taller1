"""
Archivo principal de la aplicación Flask
"""
import os
from flask import Flask
from flask_restful import Api
from models import db
from resources.video import Video
from config import config
from flask_swagger_ui import get_swaggerui_blueprint
from flask import jsonify

def create_app(config_name='default'):

    app = Flask(__name__)
    
    # Cargar configuración
    app.config.from_object(config[config_name])
    
    # Inicializar extensiones
    db.init_app(app)
    api = Api(app)
    
    # Registrar rutas
    api.add_resource(Video, "/api/videos/<int:video_id>")

    # Swagger UI
    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.json'
    swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL)
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
    
    return app

if __name__ == "__main__":
    # Obtener configuración del entorno o usar 'development' por defecto
    config_name = os.getenv('FLASK_CONFIG', 'development')
    
    # Crear aplicación
    app = create_app(config_name)
    
    # Crear todas las tablas en la base de datos
    with app.app_context():
        db.create_all()
    
    # Ejecutar servidor
    app.run(host='0.0.0.0', port=5000)

