# from django.shortcuts import render
# import requests
from django.http import JsonResponse
from django.views import View
from rest_framework import generics
from .models import UserDetails
from .serializers import UserDetailsSerializer
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


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
    @csrf_exempt
    def post(self, request):
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
