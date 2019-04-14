from django.db import models
import datetime
from django.utils import timezone


class Magic(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class OracleRecord(models.Model):
    computer_choice = models.CharField(max_length=200)
