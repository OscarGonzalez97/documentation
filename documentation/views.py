from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Max, Q
from django.template.loader import render_to_string
from .models import Version, VersionConfiguration, ConfigurationFileName, DatabaseFileName, Document, DocumentType, \
    DocumentFileName, PostmanFunctionality, Postman, VideoType, Video, DatabaseScript, StoredProcedureHTTP, MenuFilters
from django.http import HttpResponse
import re
import logging

logger = logging.getLogger(__name__)

@login_required(login_url='/auth/login')
def versions(request):
    menu_filters_instance = MenuFilters.objects.first()  # Assuming you have only one instance
    versions = Version.objects.all().order_by('-date')
    details = {}
    for version in versions:
        details[version.id] = version.details.all()
    context = {
        'versions': versions,
        'details': details,
        'menu_filters_instance': menu_filters_instance,
    }
    return render(request, 'documentation/versions.html', context)


def get_doc(request):
    version_id = request.GET.get("version_id")
    version = Version.objects.filter(id=int(version_id)).first()
    configurations = version.configurations.all().order_by('version__date')
    configuration_context = []
    menu_filters_instance = MenuFilters.objects.first()  # Assuming you have only one instance

    for conf in configurations:
        conf_modified = {
            'file_name': conf.file_name,
            'configuration': conf.configuration
        }
        configuration_context.append(conf_modified)

    database_files = DatabaseScript.objects.filter(version=version).order_by('file_name__database_file_name')

    context = {
        'version': version,
        'details': version.details.all(),
        'components': version.components.all(),
        'files': version.files.all(),
        'configurations': configuration_context,
        'images': version.images.all(),
        'database_files': database_files,
        'menu_filters_instance': menu_filters_instance,
    }
    data = render_to_string('documentation/get_doc.html', context)
    return HttpResponse(data, status=200, content_type='text/html')


@login_required(login_url='/auth/login')
def files(request):
    configurations_files = ConfigurationFileName.objects.all().order_by('configuration_file')
    configuration_context = []
    menu_filters_instance = MenuFilters.objects.first()  # Assuming you have only one instance

    for file in configurations_files:
        conf_modified = {
            'file_name': file.configuration_file,
            'configuration': ''
        }
        old_configurations = file.versions.all()
        old_config = ''
        for old_conf in old_configurations:
            if old_config:
                old_config += "\n"
            old_config += f"<strong># Desde version {old_conf.version.version_number}</strong>"
            old_config += "\n"
            old_config += old_conf.configuration
        conf_modified['old_configuration'] = old_config
        configuration_context.append(conf_modified)

    context = {
        'configurations': configuration_context,
        'menu_filters_instance': menu_filters_instance,
    }
    return render(request, 'documentation/files.html', context)


@login_required(login_url='/auth/login')
def scripts_db(request):
    files = DatabaseFileName.objects.all().order_by('database_file_name')
    scripts_files_context = []
    menu_filters_instance = MenuFilters.objects.first()  # Assuming you have only one instance

    for file in files:
        conf_modified = {
            'file_name': file.database_file_name,
            'configuration': ''
        }
        old_configurations = file.versions.all().order_by('date')
        old_config = ''
        for old_conf in old_configurations:
            if old_config:
                old_config += "\n"
            if old_conf.version:
                old_config += f"<strong>-- Desde version {old_conf.version.version_number}</strong>"
                old_config += "\n"
            elif old_config.find("<strong>--Sin version</strong>") == -1:
                old_config += f"<strong>--{old_conf.date.strftime('%d/%m/%Y')}</strong>"
                old_config += "\n"
            old_config += old_conf.change
        conf_modified['old_configuration'] = old_config
        scripts_files_context.append(conf_modified)

    context = {
        'configurations': scripts_files_context,
        'menu_filters_instance': menu_filters_instance,
    }
    return render(request, 'documentation/database.html', context)


@login_required(login_url='/auth/login')
def documents(request):
    types = DocumentType.objects.all().order_by('document_type_name')
    file_names = DocumentFileName.objects.all().annotate(
        last_document_date=Max('documents__date')
    ).order_by('last_document_date')
    documentos = []
    documentos_id = []
    menu_filters_instance = MenuFilters.objects.first()  # Assuming you have only one instance
    for file_name in file_names:
        last_document = file_name.documents.order_by('-date').first()
        if last_document:
            documentos.append(last_document)
            documentos_id.append(last_document.id)

    outdate_docs = Document.objects.filter(visible=True).exclude(id__in=documentos_id).order_by('-date')

    context = {
        'types': types,
        'file_names': file_names,
        'documents': documentos,
        'outdated_docs': outdate_docs,
        'menu_filters_instance': menu_filters_instance,
    }
    return render(request, 'documentation/documents.html', context)


@login_required(login_url='/auth/login')
def postman(request):
    functionalities = PostmanFunctionality.objects.all().order_by('postman_functionality_name')
    files = Postman.objects.filter(visible=True)
    menu_filters_instance = MenuFilters.objects.first()  # Assuming you have only one instance
    context = {
        'functionalities': functionalities,
        'files': files,
        'menu_filters_instance': menu_filters_instance,
    }
    return render(request, 'documentation/postman.html', context)


@login_required(login_url='/auth/login')
def videos(request):
    types = VideoType.objects.all().order_by('video_type_name')
    videos = Video.objects.all().order_by('-date')
    vids = []
    menu_filters_instance = MenuFilters.objects.first()  # Assuming you have only one instance
    for video in videos:
        video_code = re.search(r"youtu\.be/(.*)", video.link).group(1)
        vids.append({
            'type': video.type,
            'title': video.title,
            'description': video.description,
            'link': video.link,
            'video_code': video_code
        })

    context = {
        'types': types,
        'videos': vids,
        'menu_filters_instance': menu_filters_instance,
    }
    return render(request, 'documentation/videos.html', context)


@login_required(login_url='/auth/login')
def sp_http(request, type):
    if type:
        versions = StoredProcedureHTTP.objects.filter(Q(type__type_name__icontains=type)).order_by('date')
    else:
        versions = StoredProcedureHTTP.objects.all().order_by('-date')
    menu_filters_instance = MenuFilters.objects.first()  # Assuming you have only one instance
    context = {
        'versions': versions,
        'type': type,
        'menu_filters_instance': menu_filters_instance,
    }
    return render(request, 'documentation/versions_sps.html', context)


def get_doc_sps(request):
    version_id = request.GET.get("version_id")
    version = StoredProcedureHTTP.objects.filter(id=int(version_id)).first()
    menu_filters_instance = MenuFilters.objects.first()  # Assuming you have only one instance
    context = {
        'version': version,
        'menu_filters_instance': menu_filters_instance,
    }
    data = render_to_string('documentation/get_doc_sps.html', context)
    return HttpResponse(data, status=200, content_type='text/html')
@login_required(login_url='/auth/login')
def your_view_function(request):
    menu_filters_instance = MenuFilters.objects.first()  # Assuming you have only one instance
    return render(request, 'common/base-secured.html', {'menu_filters_instance': menu_filters_instance})