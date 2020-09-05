from django.db import models


class SearchModel(models.Model):
    search = models.CharField(max_length=255)


class JsonModel(models.Model):
    Currency = models.CharField(max_length=255)
