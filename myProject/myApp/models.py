from django.db import models

# Create your models here.
class UserInformation(models.Model):
    name = models.CharField(max_length=150)
    dob = models.DateField()
    email = models.EmailField()
    phone = models.IntegerField()

    def __str__(self):
        return str(self.name)