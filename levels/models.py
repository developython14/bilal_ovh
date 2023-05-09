from django.db import models

# Create your models here.




class levels(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    order = models.IntegerField(default=0)
    title = models.CharField(max_length=100,unique=True )
    abre = models.CharField(max_length=5, blank=True, default='')

    def __str__(self) -> str:
        return self.title


    class Meta:
        ordering = ['order']




class Filieres(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    order = models.IntegerField(default=0)
    title = models.CharField(max_length=100,unique=True )
    abre = models.CharField(max_length=5, blank=True, default='')
    level = models.ForeignKey(levels , blank=True , on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title +'ha'+ str(self.level.id)

    class Meta:
        ordering = ['order']



class Modules(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100,unique=True )
    icon_title = models.ImageField(upload_to='modules_icon')
    filiere = models.ForeignKey(Filieres , blank=True , on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title +'ha'+ str(self.title)
    

class Tutorial(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100,unique=True )
    old_prix = models.CharField(max_length=100,unique=True )
    new_prix = models.CharField(max_length=100,unique=True )
    Module = models.ForeignKey(Modules , blank=True , on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.title +'ha'+ str(self.title)
    

class Cours(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100,unique=True )
    pdf_url = models.CharField(max_length=100,unique=True )
    video_url = models.CharField(max_length=100,unique=True )
    is_free = models.BooleanField(null=True)
    tutorial = models.ForeignKey(Tutorial , blank=True , on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title +'ha'+ str(self.title)

