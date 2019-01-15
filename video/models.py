from django.db import models
from warnlist.models import WarnListModel


class VideoModel(models.Model):
    list = models.ForeignKey(WarnListModel,on_delete=models.CASCADE,verbose_name='所属清单')
    video = models.FileField(upload_to='video/%Y/%m',verbose_name='违法视频')
    image = models.ImageField(upload_to='image/%Y/%m',verbose_name='违法图片')
    add_time = models.DateTimeField(auto_now_add=True,verbose_name='添加时间')
