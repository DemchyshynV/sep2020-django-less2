from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator


# Create your models here.
class UserModel(models.Model):
    class Meta:
        db_table = 'users'
        verbose_name = 'user'

    name = models.CharField(max_length=20, validators=[RegexValidator('^[a-zA-Z]{2,20}$', 'name must be only a-z A-Z and min 2 max 20 characters')])
    age = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(150)])
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=20, default='male', blank=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
