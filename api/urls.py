from django.urls import path
from api import views

urlpatterns = [
    path('getdummyjson/', views.get_dummy_json_view, name='get_dummy_json'),
]