from django.db import models

# Create your models here.

class contact(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    order = models.IntegerField(default=0)
    title = models.CharField(max_length=100, blank=True, default='')
    icon_title = models.ImageField(upload_to='contact_icon')
    text_to_show = models.CharField(max_length=100, blank=True, default='')
    type_url = models.CharField(max_length=100, blank=True, default='')
    url = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ['order']
