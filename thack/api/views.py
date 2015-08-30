import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from rest_framework.views import APIView
from django.conf import settings


class ApiSample(View):
    def get(self, request):
        return HttpResponse(json.dumps(request.GET), content_type='application/json')
