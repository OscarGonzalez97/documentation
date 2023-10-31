from django.contrib import admin
from .models import Version, VersionDetail, VersionComponent, VersionFile, VersionConfiguration, VersionImage, \
    ConfigurationFileName, DatabaseFileName, DatabaseScript, DocumentType, Document, DatabaseType, DocumentFileName, \
    PostmanFunctionality, Postman, VideoType, Video, StoredProcedureHTTPType, StoredProcedureHTTP
from .forms import VersionForm
from ckeditor.widgets import CKEditorWidget
from ckeditor.fields import RichTextField


class VersionDetailInline(admin.TabularInline):
    model = VersionDetail
    extra = 1
    fields = ('detail_text', 'bold')
    verbose_name_plural = 'Detalles de versión'


class VersionComponentInline(admin.TabularInline):
    verbose_name_plural = 'Componentes actualizados de versión'
    model = VersionComponent
    extra = 1
    fields = ('component',)


class VersionFileInline(admin.TabularInline):
    verbose_name_plural = 'Archivos de versión'
    model = VersionFile
    extra = 1


class VersionConfigurationInline(admin.TabularInline):
    verbose_name_plural = 'Configuraciones de versión'
    model = VersionConfiguration
    extra = 1


class VersionImageInline(admin.TabularInline):
    verbose_name_plural = 'Imagenes de versión'
    model = VersionImage
    extra = 1


class VersionAdmin(admin.ModelAdmin):
    formfield_overrides = {
        RichTextField: {'widget': CKEditorWidget},
    }
    form = VersionForm
    inlines = [
        VersionDetailInline,
        VersionComponentInline,
        VersionFileInline,
        VersionConfigurationInline,
        VersionImageInline,
    ]


admin.site.register(Version, VersionAdmin)
admin.site.register(ConfigurationFileName)

# DB
admin.site.register(DatabaseFileName)
admin.site.register(DatabaseType)
admin.site.register(DatabaseScript)

# Documents
admin.site.register(DocumentFileName)
admin.site.register(DocumentType)
admin.site.register(Document)

# Postman
admin.site.register(PostmanFunctionality)
admin.site.register(Postman)

# Videos
admin.site.register(VideoType)
admin.site.register(Video)


# SP_HTTP
admin.site.register(StoredProcedureHTTPType)
admin.site.register(StoredProcedureHTTP)

