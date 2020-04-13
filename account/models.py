from django.db import models


# Create your models here.
class User(models.Model):
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربر'

    user_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=11)
    email_address = models.CharField(max_length=60)
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    city = models.CharField(default='تهران', max_length=30)
    MAN = 1
    WOMEN = 2
    kind_gender(
    (MAN , 'مرد' ),
    (WOMEN ,'زن')
    )
    gender = models.IntegerField(choices=kind_gender)
