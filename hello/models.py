from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=11)
    subject = models.CharField(max_length=400)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta :
        ordering =['-created']

    def __str__(self):
        return self.message[0:50]