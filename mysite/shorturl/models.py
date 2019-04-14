from django.db import models


class Web_Url(models.Model):
    code = models.CharField(max_length=100)
    original_url = models.CharField(max_length=500)

    def __str__(self):
        return self.original_url