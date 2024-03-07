from django.http import JsonResponse
import json
from django.views import View
from rest_framework import generics
from .models import UserDetails
from .serializers import UserDetailsSerializer
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from django.contrib.auth.hashers import make_password, check_password
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token

# Create your views here.

# Signup user
class UserSignUpView(View):
    def post(self, request):
        try:
            data = request.POST.dict()
            hashed_password = make_password(data.get('password'))
            user = UserDetails.objects.create(
                user_name=data.get('user_name'),
                user_phone=data.get('user_phone'),
                user_email=data.get('user_email'),
                password=hashed_password,
                location=data.get('location')
            )
            return JsonResponse({'message': 'User signed up successfully', 'user_id': user.id}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

# Login user
class UserSigninView(View):
    def post(self, request):
        try:
            data = request.POST.dict()
            user_email = data.get('user_email')
            password = data.get('password')
            user = UserDetails.objects.get(user_email=user_email)
            print(user.password)
            if check_password(password, user.password):
                refresh = RefreshToken.for_user(user)
                return JsonResponse({'refresh': str(refresh), 'access': str(refresh.access_token)}, status=status.HTTP_200_OK)
            else:
                return JsonResponse({'error': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)
        except UserDetails.DoesNotExist:
            return JsonResponse({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

# Profile view for single user
class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        try:
            print("Authenticated bitch!")
            user = UserDetails.objects.get(id=user_id)
            user_data = {
                'id': user.id,
                'user_name': user.user_name,
                'user_phone': user.user_phone,
                'user_email': user.user_email,
                'location': user.location
            }
            return JsonResponse({'user_details': user_data}, status=status.HTTP_200_OK)
        except UserDetails.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

# Edit user profile
class UserEditProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, user_id):
        try:
            data = request.POST.dict()
            user = UserDetails.objects.get(id=user_id)
            user.user_name = data.get('user_name')
            user.user_phone = data.get('user_phone')
            user.user_email = data.get('user_email')
            if 'password' in data:
                user.password = make_password(data['password'])
            user.location = data.get('location')
            user.save()
            return JsonResponse({'message': 'User profile updated successfully'}, status=status.HTTP_200_OK)
        except UserDetails.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

# User details view
class UserDetailsView(View):
    def get(self, request, pk):
        user_details = get_object_or_404(UserDetails, pk=pk)
        data = {
            'user_name': user_details.user_name,
            'user_phone': user_details.user_phone,
            'user_email': user_details.user_email,
            'location': user_details.location,
        }
        return JsonResponse(data)


# List all users from UserDetails
class UserDetailsListCreate(generics.ListCreateAPIView):
    queryset = UserDetails.objects.all()
    serializer_class = UserDetailsSerializer

# Set CSRF token cookie
class SetCSRFTokenView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        return Response({'message': 'CSRF token cookie set successfully'}, status=status.HTTP_200_OK)

# [To be depricated] Create a new user
class UserCreateView(View):
    def post(self, request, format=None):
        # Get data from form fields
        user_name = request.POST.get('user_name')
        user_phone = request.POST.get('user_phone')
        user_email = request.POST.get('user_email')
        password = request.POST.get('password')
        location = request.POST.get('location')

        # Create a new UserDetails object with the received data
        user_details = UserDetails.objects.create(
            user_name=user_name,
            user_phone=user_phone,
            user_email=user_email,
            password=password,
            location=location,
        )

        # Return success response
        response_data = {'message': 'User details created successfully'}
        return JsonResponse(response_data, status=201)


# dummy api for testing
def get_dummy_json_view(request):
    # get parameters from the URL
    name_param = request.GET.get('name', '')
    email_param = request.GET.get('email', '')

    # static json payload
    dummy_data = {
        "name": name_param,
        "email": email_param,
        "other_data": "value",
    }
    # return payload
    return JsonResponse(dummy_data)