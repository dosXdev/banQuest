from django.urls import path
from api import views
from .views import UserDetailsListCreate, UserDetailsView

urlpatterns = [
    path('getdummyjson/', views.get_dummy_json_view, name='get_dummy_json'),
    path('users/getall/', UserDetailsListCreate.as_view(), name='user-list-create'),
    path('users/get/<int:pk>/', UserDetailsView.as_view(), name='user-detail'),
]