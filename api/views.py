# from django.shortcuts import render
# import requests
from django.http import JsonResponse

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
