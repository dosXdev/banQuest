from django.urls import path
from api import views
from .views import UserDetailsListCreate, UserDetailsView, UserCreateView


urlpatterns = [
    # test apis
    path('getdummyjson/', views.get_dummy_json_view, name='get_dummy_json'),
    path('users/getall/', UserDetailsListCreate.as_view(), name='user-list-create'),
    path('users/get/<int:pk>/', UserDetailsView.as_view(), name='user-detail'),
    path('users/create/', UserCreateView.as_view(), name='user-create'),

    # app apis
    path('forms/users/signup/', UserCreateView.as_view(), name='user-create'),
]