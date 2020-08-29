from django.db import models


class SearchModel(models.Model):
    search = models.CharField(max_length=255)
