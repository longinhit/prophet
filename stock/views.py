from django.shortcuts import render
from django.http import HttpResponse
import json


def ping(request):
    resp = {
        "code": "ST0000",
        "msg": "success",
    }
    return HttpResponse(json.dumps(resp), content_type='application/json')


def index(request):
    return render(request, 'stock/index.html')
