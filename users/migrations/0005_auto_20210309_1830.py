# Generated by Django 3.1.7 on 2021-03-09 18:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210309_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='age',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(150)]),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='name',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^[a-zA-Z]{2,20}$', 'name must be only a-z A-Z and min 2 max 20 characters')]),
        ),
    ]