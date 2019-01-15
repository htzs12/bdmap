from django.db import models
from rest_framework import serializers


#  废弃
class address_info(models.Model):
    longitude = models.FloatField(verbose_name='经度')
    latitude = models.FloatField(verbose_name='纬度')
    address = models.CharField(max_length=100,null=True,blank=True,verbose_name='地址')
    phone = models.CharField(max_length=100,null=True,blank=True,verbose_name='电话')
    desc = models.CharField(max_length=1000,null=True,blank=True,verbose_name='介绍')
    video = models.URLField(null=True,blank=True,verbose_name='视频地址')

    class Meta:
        verbose_name = '地图模型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.address


class MapModel(models.Model):
    # 地图资源模型
    longitude = models.FloatField(verbose_name='经度')
    latitude = models.FloatField(verbose_name='纬度')
    number = models.IntegerField(verbose_name='站点编号')
    address = models.CharField(max_length=100, null=True, blank=True, verbose_name='地址')
    phone = models.CharField(max_length=100, null=True, blank=True, verbose_name='电话')
    desc = models.CharField(max_length=1000, null=True, blank=True, verbose_name='介绍')
    video = models.URLField(null=True, blank=True, verbose_name='视频地址')

    class Meta:
        verbose_name = '地图模型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.address
