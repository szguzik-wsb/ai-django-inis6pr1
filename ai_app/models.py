from django.db import models


class ImageElement(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=False, default='')
    image = models.ImageField(upload_to='media', blank=True, null=True)

    def __str__(self):
        return self.title
