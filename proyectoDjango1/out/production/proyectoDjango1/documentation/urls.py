from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('versions/', views.versions, name="versions"),
    path('get_doc/', views.get_doc, name="get_doc"),
    path('files/', views.files, name="files"),
    path('scripts/', views.scripts_db, name="scripts"),
    path('documents/', views.documents, name="documents"),
    path('postman/', views.postman, name="postman"),
    path('videos/', views.videos, name="videos"),
    path('sps/<str:type>/', views.sp_http, name="sp_http"),
    path('get_doc_sps/', views.get_doc_sps, name="get_doc_sps"),
]