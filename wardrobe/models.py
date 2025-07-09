from django.db import models
from django.conf import settings


class Orders(models.Model):
    # клиент
    customer_name = models.CharField(max_length=50, verbose_name='имя заказчика')
    customer_surname = models.CharField(max_length=50, verbose_name='фамилия заказчика')
    phone = models.CharField(max_length=12, verbose_name='телефон заказчика')
    email = models.EmailField(verbose_name='email')
    # размеры
    height = models.IntegerField()
    width = models.IntegerField()
    depth = models.IntegerField()
    # короб
    material_type = models.CharField(max_length=35, verbose_name='материал')
    box_material_thickness = models.SmallIntegerField(verbose_name='толщина')
    box_material_color = models.CharField(max_length=35, verbose_name='цвет')   
    box_square = models.IntegerField()
    box_price_per_sqm = models.IntegerField(verbose_name='цена короба за м кв')
    box_price = models.IntegerField(verbose_name='цена короба')
    # двери
    door_type = models.CharField(max_length=35, verbose_name='тип дверей')
    door_material_thickness = models.SmallIntegerField(verbose_name='толщина')
    door_material_color = models.CharField(max_length=35, verbose_name='цвет')
    door_square = models.IntegerField()
    door_price_per_sqm = models.IntegerField(verbose_name='цена двери за м кв')
    door_price = models.IntegerField(verbose_name='цена двери')
    # фурнитура
    handle_name = models.CharField(max_length=35, verbose_name='тип дверной ручки')
    handle_material = models.CharField(max_length=35, verbose_name='материал дверной ручки')
    handle_color = models.CharField(max_length=35, verbose_name='цвет дверной ручки')
    handle_length = models.CharField(max_length=35, verbose_name='длинна дверной ручки', null=True, blank=True)
    handle_price_per_one = models.IntegerField(verbose_name='цена дверной ручки за единицу')
    handle_ammount = models.IntegerField(verbose_name='количество дверных ручек')
    handle_price = models.IntegerField(verbose_name='цена дверной ручки')
    # итоговая цена
    total_price = models.IntegerField(verbose_name='стоимость шкафа')
    # сотрудник
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='сотрудник')
    # дата 
    order_date = models.DateTimeField(verbose_name='дата заказа', null=True, blank=True)
    # активность
    is_active = models.BooleanField(default=True, verbose_name='active')
    
    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'
