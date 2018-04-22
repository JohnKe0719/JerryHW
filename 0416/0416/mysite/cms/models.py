from django.db import models
import django.utils.timezone as timezone
# Create your models here.
class Information(models.Model):
    GENDER_CHOICES = (
        (u'男', u'男'),
        (u'女', u'女'),
    )
    name=models.CharField('姓名',max_length=10)
    birthday=models.DateTimeField('出生日期',default = timezone.now)
    gender=models.CharField('性別',max_length=2,choices=GENDER_CHOICES)

    def __str__(self):
        return self.name