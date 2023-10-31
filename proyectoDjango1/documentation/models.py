from django.utils import timezone
from django.db import models
from ckeditor.fields import RichTextField


class Version(models.Model):
    version_number = models.CharField('Numero de version', max_length=50)
    date = models.DateField('Fecha')
    summary = RichTextField()

    def __str__(self):
        return self.version_number

    class Meta:
        verbose_name_plural = "Versiones"


class ConfigurationFileName(models.Model):
    configuration_file = models.CharField('Nombre de archivo de configuracion', max_length=250)

    def __str__(self):
        return self.configuration_file

    class Meta:
        verbose_name_plural = "Nombre de archivos de configuración"



class VersionDetail(models.Model):
    version = models.ForeignKey(Version, related_name='details', related_query_name='version', on_delete=models.CASCADE)
    detail_text = models.TextField('Texto de detalle')
    bold = models.BooleanField('Negrita', default=False)


class VersionComponent(models.Model):
    version = models.ForeignKey(Version, related_name='components', on_delete=models.CASCADE)
    component = models.CharField('Version de componente', max_length=200)


class VersionFile(models.Model):
    version = models.ForeignKey(Version, related_name='files', on_delete=models.CASCADE)
    file = models.FileField('Archivo')


class VersionConfiguration(models.Model):
    version = models.ForeignKey(Version, related_name='configurations', on_delete=models.CASCADE)
    file_name = models.ForeignKey(ConfigurationFileName, related_name='versions', on_delete=models.CASCADE)
    configuration = models.TextField('Cambio en configuracion')


class VersionImage(models.Model):
    version = models.ForeignKey(Version, related_name='images', on_delete=models.CASCADE)
    image_title = models.TextField('Titulo de imagen', null=True, blank=True)
    image_description = models.TextField('Texto de imagen', null=True, blank=True)
    image = models.ImageField('Image')


class DatabaseType(models.Model):
    database_type_name = models.CharField('Tipo de script', max_length=300)

    def __str__(self):
        return self.database_type_name

    class Meta:
        verbose_name_plural = "BD - Tipos de archivos"


class DatabaseFileName(models.Model):
    type = models.ForeignKey(DatabaseType, related_name='file_names', on_delete=models.CASCADE)
    database_file_name = models.TextField('Nombre de script BD')

    def __str__(self):
        return self.database_file_name

    class Meta:
        verbose_name_plural = "BD - Nombre de archivos"


class DatabaseScript(models.Model):
    version = models.ForeignKey(Version, related_name='scripts', on_delete=models.SET_NULL, null=True, blank=True)
    file_name = models.ForeignKey(DatabaseFileName, related_name='versions', on_delete=models.CASCADE)
    date = models.DateField('Fecha')
    change = models.TextField('Cambio en Script')
    description = models.TextField('Descripción cambio', null=True, blank=True)

    def __str__(self):
        if self.description:
            if self.version:
                return str(self.description) + ' - ' + str(self.file_name) + ' - Fecha: ' + str(self.date) +\
                       ' - Version: ' + str(self.version)
            return str(self.description) + ' - ' + str(self.file_name) + ' - Fecha: ' + str(self.date)
        else:
            return str(self.pk) + ' - ' + str(self.file_name) + ' - Fecha: ' + str(self.date)

    class Meta:
        verbose_name_plural = "BD - Archivos"


class DocumentType(models.Model):
    document_type_name = models.CharField('Tipo de documento', max_length=300)

    def __str__(self):
        return self.document_type_name

    class Meta:
        verbose_name_plural = "Documentos - Tipos de documentos"


class DocumentFileName(models.Model):
    type = models.ForeignKey(DocumentType, related_name='file_names', on_delete=models.SET_NULL, null=True, blank=True)
    file_name = models.CharField('Nombre de documento', max_length=400)

    def __str__(self):
        return self.file_name

    class Meta:
        verbose_name_plural = "Documentos - Nombres de documentos"


class Document(models.Model):
    file_name = models.ForeignKey(DocumentFileName, related_name='documents', on_delete=models.CASCADE)
    version_number = models.CharField('Numero de version', max_length=50, null=True, blank=True)
    date = models.DateField('Fecha')
    visible = models.BooleanField(default=True)
    file = models.FileField('Archivo')

    class Meta:
        verbose_name_plural = "Documentos - Documentos"

    def __str__(self):
        return str(self.file_name) + ' - ' + str(self.date)


class PostmanFunctionality(models.Model):
    postman_functionality_name = models.CharField('Nombre de funcionalidad', max_length=400)

    def __str__(self):
        return self.postman_functionality_name

    class Meta:
        verbose_name_plural = "Postman - Funcionalidad"


class Postman(models.Model):
    functionality = models.ForeignKey(PostmanFunctionality, related_name='files', on_delete=models.CASCADE)
    collection_name = models.CharField('Nombre de colección', max_length=300)
    date = models.DateField('Fecha')
    version_number = models.CharField('Numero de version', max_length=50, null=True, blank=True)
    visible = models.BooleanField(default=True)
    postman_file = models.FileField('Colección Postman')

    class Meta:
        verbose_name_plural = "Postman - Archivos"

    def __str__(self):
        if self.version_number:
            return str(self.functionality) + ' - ' + self.collection_name + ' - Version: ' + str(self.version_number)
        return str(self.functionality) + ' - ' + self.collection_name


class VideoType(models.Model):
    video_type_name = models.CharField('Tipo de video', max_length=300)

    def __str__(self):
        return self.video_type_name

    class Meta:
        verbose_name_plural = "Videos - Tipos de videos"


class Video(models.Model):
    type = models.ForeignKey(VideoType, related_name='videos', on_delete=models.CASCADE)
    title = models.CharField('Título', max_length=400)
    description = models.TextField('Descripción', null=True, blank=True)
    link = models.URLField('Youtube Link', help_text='Se debe ir al video de Youtube y hacer click derecho sobre el video, y copiar el link \'Copiar URL del vídeo\'')
    date = models.DateField('Fecha', default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Videos - Videos"


class StoredProcedureHTTPType(models.Model):
    type_name = models.CharField('Tipo de SP HTTP', max_length=300)

    def __str__(self):
        return self.type_name

    class Meta:
        verbose_name_plural = "SP HTTP - Tipos de SP"


class StoredProcedureHTTP(models.Model):
    type = models.ForeignKey(StoredProcedureHTTPType, related_name='sps', on_delete=models.CASCADE)
    version_number = models.CharField('Numero de version', max_length=50, null=True, blank=True)
    date = models.DateField('Fecha', default=timezone.now)
    file = models.FileField('Archivo')
    readme = models.TextField('Readme')

    def __str__(self):
        return str(self.type) + ' - ' + str(self.date)

    class Meta:
        verbose_name_plural = "SP HTTP - SP HTTP"
