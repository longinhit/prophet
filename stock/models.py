# coding: utf8
from django.db import models


class TradeStock(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=8)
    name = models.CharField(max_length=255)
    buy_time = models.DateTimeField()
    buy_price = models.IntegerField()
    sale_time = models.DateTimeField()
    sale_price = models.IntegerField()
    profit_percentage = models.IntegerField()

    class Meta:
        db_table = "trade_stocks"

