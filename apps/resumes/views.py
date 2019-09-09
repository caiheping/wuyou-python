from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse


# Create your views here.


class Test(View):
    def get(self, request):
        return JsonResponse({'code': '0', 'date': 'successs'})


class Login(View):
    pass