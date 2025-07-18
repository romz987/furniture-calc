from django.db import models


class MaterialType(models.Model):
    name = models.CharField(max_length=15, unique=True, verbose_name='материал') 

    class Meta:
        verbose_name = 'Тип материала'
        verbose_name_plural = 'Типы материалов'

    def __str__(self):
        return f'{self.name}'


class MaterialThickness(models.Model):
    thickness = models.SmallIntegerField(unique=True, verbose_name='толщина') 

    class Meta:
        verbose_name = 'Толщина'
        verbose_name_plural = 'Толщины'

    def __str__(self):
        return f'{self.thickness}'


class MaterialColor(models.Model):
    name = models.CharField(max_length=25, unique=True, verbose_name='цвет')

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

    def __str__(self):
        return f'{self.name}'


class DoorType(models.Model):
    name = models.CharField(max_length=25, unique=True, verbose_name='тип дверей')

    class Meta:
        verbose_name = 'Тип дверей'
        verbose_name_plural = 'Типы дверей'

    def __str__(self):
        return f'{self.name}'


# Summary
class BoxSummary(models.Model):
    material_type = models.ForeignKey(MaterialType, on_delete=models.CASCADE, verbose_name='материал')
    material_thickness = models.ForeignKey(MaterialThickness, on_delete=models.CASCADE, verbose_name='толщина')
    material_color = models.ForeignKey(MaterialColor, on_delete=models.CASCADE, verbose_name='цвет')
    price_per_sqm = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена за квадратный метр') 

    class Meta:
        verbose_name = 'Материал короба'
        verbose_name_plural = 'Материалы короба'
        unique_together = ('material_type', 'material_thickness', 'material_color')


class DoorSummary(models.Model):
    material_type = models.ForeignKey(MaterialType, on_delete=models.CASCADE, verbose_name='материал')
    material_thickness = models.ForeignKey(MaterialThickness, on_delete=models.CASCADE, verbose_name='толщина')
    material_color = models.ForeignKey(MaterialColor, on_delete=models.CASCADE, verbose_name='цвет')
    door_type = models.ForeignKey(DoorType, on_delete=models.CASCADE, verbose_name='тип дверей')
    price_per_sqm = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена за квадратный метр') 

    class Meta:
        verbose_name = 'Материал дверки'
        verbose_name_plural = 'Материалы дверок'
        unique_together = ('material_type', 'material_thickness', 'material_color', 'door_type')


class DoorHandle(models.Model):
    name = models.CharField(max_length=25, verbose_name='дверная ручка')
    length = models.SmallIntegerField(verbose_name='межцентровое расстояние', null=True, blank=True)
    material = models.CharField(max_length=25, verbose_name='материал ручки')
    color = models.CharField(max_length=25, verbose_name='цвет ручки')
    price_per_one = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена за единицу')

    class Meta:
        verbose_name = 'Дверная ручка'
        verbose_name_plural = 'Дверные ручки'
        unique_together = ('name', 'length', 'material', 'color')

    def __str__(self):
        return f'{self.name}'
