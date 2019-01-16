from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from shortuuidfield import ShortUUIDField


class UserManger(BaseUserManager):
    # 用户管理类
    def _create_user(self,telephone,username,password,**kwargs):
        if not telephone:
            raise ValueError('请传入手机号！')
        if not username:
            raise ValueError('请传入用户名！')
        if not password:
            raise ValueError('请传入密码！')

        user = self.model(telephone=telephone,username=username,**kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_user(self,telephone,username,password,**kwargs):
        kwargs['is_superuser'] = False
        user = self._create_user(telephone,username,password,**kwargs)
        return user

    def create_superuser(self,telephone,username,password,**kwargs):
        kwargs['is_superuser'] = True
        kwargs['is_staff'] = True
        user = self._create_user(telephone,username,password,**kwargs)
        return user


class User(AbstractBaseUser,PermissionsMixin):
    # 用户模型 / 不适用默认的主键
    id = ShortUUIDField(primary_key=True)
    telephone = models.CharField(max_length=11,unique=True,verbose_name='手机号')
    email= models.EmailField(unique=True,verbose_name='邮箱')
    username = models.CharField(max_length=100,verbose_name='用户名')
    # image = models.ImageField(upload_to='image/%Y/%m',verbose_name='用户头像')
    is_active = models.BooleanField(default=False,verbose_name='是否激活')
    is_staff = models.BooleanField(default=True,verbose_name='是否为员工')
    date_joined = models.DateTimeField(auto_now_add=True,verbose_name='添加时间')

    USERNAME_FIELD = 'telephone'  # authenticate 唯一验证字段
    REQUIRED_FIELDS = ['username'] # 创建超级用户提示输入字段
    EMAIL_FIELD = 'email'

    objects = UserManger()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
