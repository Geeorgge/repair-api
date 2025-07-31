from django.urls import path
from . import views

urlpatterns = [
    path('status', views.status_view),
    path('repair-bay', views.repair_bay_view),
    path('teapot', views.teapot_view),
]
