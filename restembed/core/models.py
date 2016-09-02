from django.db import models

class SavedEmbeds(models.Model):
    type = models.CharField(max_length=15)
    provider_url = models.URLField()
    provider_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    html = models.TextField(null=True, blank=True)
    width = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    thumbnail_url = models.URLField(null=True, blank=True)
    thumbnail_width = models.IntegerField(null=True, blank=True)
    thumbnail_height = models.IntegerField(null=True, blank=True)
    author_url = models.URLField(null=True, blank=True)
    author_name = models.CharField(max_length=100, null=True, blank=True)
    version = models.DecimalField(max_digits=4, decimal_places=2)
