# from django.shortcuts import render
# import requests
from django.http import JsonResponse
from django.views import View
from rest_framework import generics
from .models import UserDetails
from .serializers import UserDetailsSerializer
from django.shortcuts import get_object_or_404

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