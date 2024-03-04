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
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class UserSignUpView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
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

class UserLoginView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            user_email = data.get('user_email')
            password = data.get('password')
            user = UserDetails.objects.get(user_email=user_email)
            if check_password(password, user.password):
                refresh = RefreshToken.for_user(user)
                return JsonResponse({'refresh': str(refresh), 'access': str(refresh.access_token)}, status=200)
            else:
                return JsonResponse({'error': 'Invalid email or password'}, status=401)
        except UserDetails.DoesNotExist:
            return JsonResponse({'error': 'Invalid email or password'}, status=401)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserDetailsSerializer(user)
        return Response(serializer.data)

class UserEditProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        data = request.data
        serializer = UserDetailsSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User profile updated successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_csrf_token(request):
    # Get CSRF token
    csrf_token = get_token(request)
    return JsonResponse({'csrfToken': csrf_token})

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


class UserDetailsListCreate(generics.ListCreateAPIView):
    queryset = UserDetails.objects.all()
    serializer_class = UserDetailsSerializer


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


def create_user_view(request):  
    if request.method == 'POST':
        serializer = UserDetailsSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)