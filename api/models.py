from django.db import models

# Create your models here.
class UserDetails(models.Model):
    user_name = models.CharField(max_length=100)
    user_phone = models.CharField(max_length=20)
    user_email = models.EmailField()
    password = models.CharField(max_length=128)
    location = models.CharField(max_length=100)

    class Meta:
        db_table = 'userdetails' # table name

    def __str__(self):
        return self.user_name