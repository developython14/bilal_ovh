from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class Student(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    device_id = models.CharField(max_length=100,default='' )
    is_accepeted = models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile_picture = models.ImageField(null=True,upload_to='profile_student_image')

    def __str__(self) -> str:
        return self.user.username