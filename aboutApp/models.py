from django.db import models


# Create your models here.

class Award(models.Model):
    # 荣誉
    description = models.TextField(max_length=500, blank=True, null=True)
    # 图片地址
    photo = models.ImageField(upload_to='Award/', blank=True)

    class Meta:
        verbose_name = verbose_name_plural = '荣誉资质'
        db_table = 'Award'



