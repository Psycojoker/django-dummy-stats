from datetime import datetime, timedelta, date
from django.db import models

class Request(models.Model):
    datetime = models.DateTimeField(default=datetime.now)
    date = models.DateField(default=date.today)
    ip = models.CharField(max_length=255)
    meta = models.TextField()
    path = models.CharField(max_length=255)
    response_code = models.IntegerField()
    response_size = models.IntegerField()

    @classmethod
    def this_week(self):
        return [[x, Request.objects.filter(date=(date.today() - timedelta(days=7 - x))).count()] for x in range(1, 8)]

    @classmethod
    def this_week_unique(self):
        return [[x, len(set(y.ip for y in Request.objects.filter(date=(date.today() - timedelta(days=7 - x)))))] for x in range(1, 8)]
