"""
Recursos y rutas para la API de videos
"""
from flask_restful import Resource, reqparse, abort, fields, marshal_with
from models.video import VideoModel
from models import db

# Campos para serializar respuestas
resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer
}

# Parser para los argumentos en solicitudes PUT (crear video)
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Nombre del video es requerido", required=True)
video_put_args.add_argument("views", type=int, help="Número de vistas del video", required=True)
video_put_args.add_argument("likes", type=int, help="Número de likes del video", required=True)

# Parser para los argumentos en solicitudes PATCH (actualizar video)
video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="Nombre del video")
video_update_args.add_argument("views", type=int, help="Número de vistas del video")
video_update_args.add_argument("likes", type=int, help="Número de likes del video")

def abort_if_video_doesnt_exist(video_id):
    """
    Verifica si un video existe, y si no, aborta la solicitud
    
    Args:
        video_id (int): ID del video a verificar
    """
    video = VideoModel.query.filter_by(id=video_id).first()
    if not video:
        abort(404, message=f"No se encontró un video con el ID {video_id}")
    return video

class Video(Resource):
    """
    Recurso para gestionar videos individuales
    
    Métodos:
        get: Obtener un video por ID
        put: Crear un nuevo video
        patch: Actualizar un video existente
        delete: Eliminar un video
    """
    
    @marshal_with(resource_fields)
    def get(self, video_id):
        """
        Obtiene un video por su ID
        """
        video = abort_if_video_doesnt_exist(video_id)
        return video, 200
    
    @marshal_with(resource_fields)
    def put(self, video_id):
        """
        Crea un nuevo video con un ID específico
        """
        args = video_put_args.parse_args()
        video = VideoModel.query.filter_by(id=video_id).first()
        if video:
            abort(409, message=f"El video con ID {video_id} ya existe")
        
        new_video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
        db.session.add(new_video)
        db.session.commit()
        return new_video, 201
    
    @marshal_with(resource_fields)
    def patch(self, video_id):
        """
        Actualiza un video existente
        
        Args:
            video_id (int): ID del video a actualizar
            
        Returns:
            VideoModel: El video actualizado
        """
        # TODO
        pass
    
    def delete(self, video_id):
        """
        Elimina un video existente
        
        Args:
            video_id (int): ID del video a eliminar
            
        Returns:
            str: Mensaje vacío con código 204
        """
        # TODO
        pass

