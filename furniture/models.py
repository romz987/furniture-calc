from django.db import models


class Furniture(models.Model):
    name = models.CharField(max_length=100, verbose_name='furniture type')
    description = models.CharField(max_length=350, verbose_name='type description')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'furniture'
        verbose_name_plural = 'furniture'
