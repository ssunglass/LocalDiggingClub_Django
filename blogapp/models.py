from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.models import (
  AbstractBaseUser, PermissionsMixin, UserManager
)
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    body = RichTextUploadingField()


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email', unique=True,default='')
    username = models.CharField(max_length=64, verbose_name='사용자명')
    password = models.CharField(max_length=50, verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')
    status = models.CharField(max_length=100, verbose_name="권한", default='')
    is_staff = models.BooleanField('스태프 권한', default=False)
    is_active = models.BooleanField('사용중', default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = '에디터'
        swappable = 'AUTH_USER_MODEL'


    def email_user(self, subject, message, from_email=None, **kwargs):  # 이메일 발송 메소드
         send_mail(subject, message, from_email, [self.email], **kwargs)


class Banner(models.Model):
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='bannerImages/', null=True)

    def __str__(self):
        return self.title