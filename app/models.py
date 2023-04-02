from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='teachers/', blank=True, null=True)

    class Meta:
        verbose_name = "Учитель"
        verbose_name_plural = "Учителя"

    def __str__(self):
        return self.name


class Bastaush(models.Model):
    name = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='elementary/', blank=True, null=True)

    class Meta:
        verbose_name = "Учитель начальной школы"
        verbose_name_plural = "Учителя начальной школы"

    def __str__(self):
        return self.name

