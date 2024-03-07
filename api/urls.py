from django.urls import path
from api import views
from .views import (
    UserDetailsListCreate, 
    UserDetailsView, 
    UserCreateView,
    UserSignUpView,
    UserProfileView,
    UserEditProfileView,
    UserSigninView,
    SetCSRFTokenView,
)

urlpatterns = [
    # Test apis
    # These apis are still in test mode and should not be used
    # directly with dev/prod UI component.
    path('getdummyjson/', views.get_dummy_json_view, name='get_dummy_json'),
    path('users/getall/', UserDetailsListCreate.as_view(), name='user-list-create'),
    path('users/get/<int:pk>/', UserDetailsView.as_view(), name='user-detail'),
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('test/signup/', UserSignUpView.as_view(), name='user_signup'),
    path('test/signin/', UserSigninView.as_view(), name='user_login'),
    path('test/profile/<int:user_id>/', UserProfileView.as_view(), name='user_profile'),
    path('test/profile/edit/<int:user_id>/', UserEditProfileView.as_view(), name='user_edit_profile'),

    # Debug apis
    # These apis are meant for dev/prod debug operations and
    # must be replaced with App apis before deployment.
    path('debug/users/signup/', views.create_user_view, name='create_user_view'),

    # App apis
    path('set_csrf_token/', SetCSRFTokenView.as_view(), name='set-csrf-token'),
    path('forms/users/signup/', UserCreateView.as_view(), name='user-create'),
]