from django.db import models

# Create your models here.
class UserDetails(models.Model):
    user_name = models.CharField(max_length=100)
    user_phone = models.CharField(max_length=20)
    user_email = models.EmailField()
    password = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.user_name