from django.db import models

class Flat(models.Model):
    name=models.CharField(max_length=128, verbose_name="Название")
    text=models.TextField(blank=False, verbose_name="Описание")
    img=models.ImageField(upload_to="%Y/%m/%d/", verbose_name="Изображение")
