from django.db import models


class WarnListModel(models.Model):
    # 预警清单模型
    name = models.CharField(max_length=300,verbose_name='地点名称')
    address = models.CharField(max_length=300,verbose_name='监控地址')
    news = models.CharField(max_length=300,verbose_name='预警内容')
    video= models.URLField(verbose_name='视频地址')
    image= models.URLField(verbose_name='图片地址')
    add_time = models.DateTimeField(auto_now_add=True,verbose_name='添加时间')

    class Meta:
        verbose_name = '预警清单'
        verbose_name_plural = verbose_name
