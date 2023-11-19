from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    age = models.CharField(max_length=3)
    phone_number = models.CharField(max_length=11)
    

    def __str__(self) -> str:
        return self.user.username