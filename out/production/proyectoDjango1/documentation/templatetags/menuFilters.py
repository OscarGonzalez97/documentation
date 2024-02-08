from django.template import Library
from documentation.models import MenuFilters

register = Library()

@register.filter
def get_boolean_values():
    my_table = MenuFilters.objects.get(id=1)

    # Access each column value individually
    versiones = my_table.versiones
    configuraciones = my_table.configuraciones
    basededatos = my_table.basededatos
    documentos = my_table.documentos
    videos = my_table.videos
    spOracle = my_table.spOracle
    spSQL = my_table.spSQL
    postman = my_table.postman

    boolean_values = [
        versiones,
        configuraciones,
        basededatos,
        documentos,
        videos,
        spOracle,
        spSQL,
        postman,
    ]

    return boolean_values

@register.filter
def is_versiones_enabled(boolean_values):
    return boolean_values['versiones']

@register.filter
def is_configuraciones_enabled(boolean_values):
    return boolean_values['configuraciones']

@register.filter
def is_basededatos_enabled(boolean_values):
    return boolean_values['basededatos']

@register.filter
def is_documentos_enabled(boolean_values):
    return boolean_values['documentos']

@register.filter
def is_videos_enabled(boolean_values):
    return boolean_values['videos']

@register.filter
def is_spOracle_enabled(boolean_values):
    return boolean_values['spOracle']

@register.filter
def is_spSQL_enabled(boolean_values):
    return boolean_values['spSQL']

@register.filter
def is_postman_enabled(boolean_values):
    return boolean_values['postman']