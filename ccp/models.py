from django.db import models

# Create your models here.

class ccp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    class Meta:
        ordering = ['created']



class ccp_image(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    page_de_garde = models.ImageField(upload_to='ccp_images')
    class Meta:
        ordering = ['created']
