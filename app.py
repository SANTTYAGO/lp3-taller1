"""
Archivo principal de la aplicación Flask
"""
import os
from flask import Flask
from flask_restful import Api
from models import db
from resources.video import Video
from config import config

def create_app(config_name='default'):

    app = Flask(__name__)
    
    # Cargar configuración
    app.config.from_object(config[config_name])
    
    # Inicializar extensiones
    db.init_app(app)
    api = Api(app)
    
    # Registrar rutas
    api.add_resource(Video, "/api/videos/<int:video_id>")
    
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

