from django.urls import path
from servicios import views

urlpatterns = [
    path("servicios/", views.servicios_view,name="servicios"),
]