from django.shortcuts import render
from django.http import HttpResponse
import json
from stock.models import TradeStock


def ping(request):
    resp = {
        "code": "ST0000",
        "msg": "success",
    }
    return HttpResponse(json.dumps(resp), content_type='application/json')


def index(request):
    return render(request, 'stock/index.html')


def get_stock(request):
    stock_list = TradeStock.objects.filter(code='600066')
    data = []
    for item in stock_list:
        data.append({"code": item.code})
    resp = {
        "code": "ST0000",
        "msg": "success",
        "data": data,
    }
    return HttpResponse(json.dumps(resp), content_type='application/json')
