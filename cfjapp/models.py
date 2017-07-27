from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Recive_Adress(models.Model):
    name = models.CharField(max_length=63)
    phone = models.IntegerField(default=0)
    address = models.CharField(max_length=255)

    class Meta:
        verbose_name = '收货地址'

@python_2_unicode_compatible
class NewUser(AbstractUser):
    phonenum = models.IntegerField(default=0)
    address = models.CharField(max_length=255,default='')
    reviceInfo = models.ForeignKey(Recive_Adress,blank=True, null=True)
    def __str__(self):
        return self.username


class PgroupModel(models.Model):
    name = models.CharField(max_length=126)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "类别"
        verbose_name_plural = "类别"



class ProduceModel(models.Model):
    name =  models.CharField(max_length=126,default='长丰肉食')
    price = models.FloatField(default=0.0)
    imgURL = models.CharField(max_length=256)
    sortid = models.IntegerField(unique=True,db_index=True,blank=None)
    group = models.ForeignKey(PgroupModel)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "商品名"
        verbose_name_plural = "商品名"




