from django.db import models


class Furniture(models.Model):
    name = models.CharField(max_length=100, verbose_name='furniture type')
    description = models.CharField(max_length=350, verbose_name='type description')
    image = models.ImageField(upload_to='furniture/', verbose_name='image', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Мебель'
        verbose_name_plural = 'Мебель'
