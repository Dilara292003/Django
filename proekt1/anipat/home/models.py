from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    featured_images = models.ImageField(blank=True, upload_to='home/%Y/%m/%d/')


    def __str__(self):
        return self.title

