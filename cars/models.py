from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


# Create your models here.
class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=20)
    year = models.IntegerField()
    speed = models.IntegerField()
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='cars')
