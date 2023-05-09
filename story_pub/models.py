from django.db import models

# Create your models here.


class story(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    order = models.IntegerField(default=0)
    title = models.CharField(max_length=100,default='' )
    page_de_garde = models.ImageField(null=True,upload_to='image_stories', default='')

    class Meta:
        ordering = ['order']




class story_files(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    file = models.ImageField(upload_to='files_stories', default='')
    story = models.ForeignKey(story ,on_delete=models.CASCADE)



class Pub(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=100,default='' )
    image_de_garde = models.ImageField(null=True,upload_to='pub_images', default='')

