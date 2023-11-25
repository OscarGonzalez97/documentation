from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    # /auth/login
    path('login/', views.login_view, name="login"),
    # /auth/logout
    path('logout/', views.logout_view, name="logout"),
]