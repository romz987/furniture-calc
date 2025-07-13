from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, Http404
from reference.models import (
    MaterialType,
    MaterialThickness,
    MaterialColor,
    DoorType,
    BoxSummary,
    DoorSummary,
    DoorHandle,
)
from .services import CalculateWardrobe
from .forms import WardrobeForm, SaveOrderForm, UpdateOrderForm
from .models import Orders


class WardrobeView(LoginRequiredMixin, View):
    template_name = 'wardrobe_calculator.html'
    template_result = 'wardrobe_result.html'
    model_mtypes = MaterialType
    model_thicknesses = MaterialThickness
    model_colors = MaterialColor
    model_dtypes = DoorType
    model_box_summary = BoxSummary
    model_door_summary = DoorSummary
    model_door_handle = DoorHandle
    form_class = WardrobeForm

    def get(self, request):
        form = self.form_class(**self.get_form_kwargs())
        context = {
            'form': form,
        }
        return render(request, self.template_name, context=context)

    def post(self, request):
        form = self.form_class(request.POST, **self.get_form_kwargs())
        if form.is_valid():
            # Упаковываем данные из запроса в два словаря
            info, size = self.extract_data(form)
            # Получаем стоимости за квадратный метр
            info["box_price_per_sqm"] = self.get_box_material_price(info)
            if not info["box_price_per_sqm"]:
                request.session['combination_error'] = 'box'
                return redirect('wardrobe:combination_not_found')
            info["door_price_per_sqm"] = self.get_door_material_price(info)
            if not info["door_price_per_sqm"]:
                request.session['combination_error'] = 'door'
                return redirect('wardrobe:combination_not_found')
            # Получаем данные выбранной ручки
            info.update(self.get_handle_data(info))
            # Считаем
            calculator = CalculateWardrobe()
            size, info = calculator.calculate_price(size, info)
            # Нормализация
            info = self.normalize_info(info)
            # Сохраняем результат в сессии
            request.session['wardrobe_size'] = size
            request.session['wardrobe_info'] = info
            # На страницу результатов
            return render(
                request,
                self.template_result,
                {'form': form, 'size': size, 'info': info}
            )
        return render(request, self.template_name, {'form': form})

    def get_form_kwargs(self):
        kwargs = {}
        # результат
        # uq_box_materials
        kwargs["materials"] = self.get_form_data(
            self.model_mtypes, self.model_box_summary, "material_type")
        # uq_box_thicknesses
        kwargs["box_thicknesses"] = self.get_form_data(
            self.model_thicknesses, self.model_box_summary, "material_thickness")
        # uq_box_colors
        kwargs["box_colors"] = self.get_form_data(
            self.model_colors, self.model_box_summary, "material_color")
        # uq_door_thicknesses
        kwargs["door_thicknesses"] = self.get_form_data(
            self.model_thicknesses, self.model_door_summary, "material_thickness")
        # uq_door_colors
        kwargs["door_colors"] = self.get_form_data(
            self.model_colors, self.model_door_summary, "material_color")
        # uq_door_types
        kwargs["door_types"] = self.get_form_data(
            self.model_dtypes, self.model_door_summary, "door_type")
        return kwargs

    def get_form_data(self, model_one, model_two, field_name):
        """
        Get distinct used data
        :param model_one: main model
        :param_model_two: summary model
        :param field_name: field name
        """
        result = model_one.objects.filter(
            id__in=model_two.objects.values_list(
                field_name, flat=True
            )
        ).distinct()
        return result

    def extract_data(self, form):
        info = {
            # короб
            "material_type": form.cleaned_data["materials"],
            "box_material_thickness": form.cleaned_data["box_thicknesses"],
            "box_material_color": form.cleaned_data["box_colors"],
            # двери
            "door_type": form.cleaned_data["door_types"],
            "door_material_thickness": form.cleaned_data["door_thicknesses"],
            "door_material_color": form.cleaned_data["door_colors"],
            # фурнитура
            "handle_name": form.cleaned_data["handle_name"],
            "handle_ammount": 2
        }
        size = {
            "height": int(form.cleaned_data["height"]),
            "width": int(form.cleaned_data["width"]),
            "depth": int(form.cleaned_data["depth"])
        }
        return info, size

    def get_box_material_price(self, info):
        box = self.model_box_summary.objects.filter(
            material_type=info["material_type"],
            material_thickness=info["box_material_thickness"],
            material_color=info["box_material_color"]
        ).first()
        return box.price_per_sqm if box else None

    def get_door_material_price(self, info):
        door = self.model_door_summary.objects.filter(
            material_type=info["material_type"],
            material_thickness=info["door_material_thickness"],
            material_color=info["door_material_color"],
            door_type=info["door_type"]
        ).first()
        return door.price_per_sqm if door else None

    def get_handle_data(self, info):
        handle = self.model_door_handle.objects.filter(
            name=info["handle_name"]
        ).first()
        return {
            "handle_price_per_one": handle.price_per_one,
            "handle_length": handle.length,
            "handle_color": handle.color,
            "handle_material": handle.material
        }

    def normalize_info(self, info):
        # короб
        info["material_type"] = info["material_type"].name
        info["box_material_thickness"] = info["box_material_thickness"].thickness
        info["box_material_color"] = info["box_material_color"].name
        # двери
        info["door_type"] = info["door_type"].name
        info["door_material_thickness"] = info["door_material_thickness"].thickness
        info["door_material_color"] = info["door_material_color"].name
        # фурнитура
        info["handle_name"] = info["handle_name"].name
        # остальные
        info["box_price_per_sqm"] = int(info["box_price_per_sqm"])
        info["door_price_per_sqm"] = int(info["door_price_per_sqm"])
        info["handle_price_per_one"] = int(info["handle_price_per_one"])
        info["handle_price"] = int(info["handle_price"])
        info["box_price"] = int(info["box_price"])
        info["door_price"] = int(info["door_price"])
        return info


class WardrobeSaveOrderView(LoginRequiredMixin, View):
    template_name = 'wardrobe_save_order.html'
    model = Orders
    form_class = SaveOrderForm

    def get(self, request):
        # Проверим, существует ли заказ
        if ('wardrobe_info' not in request.session
                and 'wardrobe_size' not in request.session):
            return redirect('wardrobe:calculator')
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = self.get_data_from_session(request)
            if isinstance(data, HttpResponseRedirect):
                return data
            size, info = data
            self.save_order(request, form, size, info)
            request.session["save_order"] = True
        return redirect('wardrobe:save_order_success')

    def get_data_from_session(self, request):
        size = request.session.get('wardrobe_size')
        info = request.session.get('wardrobe_info')
        if not size or not info:
            return redirect('wardrobe:calculator')
        return size, info

    def save_order(self, request, form, size, info):
        self.model.objects.create(
            # заказчик
            customer_name=form.cleaned_data['customer_name'],
            customer_surname=form.cleaned_data['customer_surname'],
            phone=form.cleaned_data['phone'],
            email=form.cleaned_data['email'],
            # размеры
            height=size['height'],
            width=size['width'],
            depth=size['depth'],
            # короб
            material_type=info['material_type'],
            box_material_thickness=info['box_material_thickness'],
            box_material_color=info['box_material_color'],
            box_square=size['box_square'],
            box_price_per_sqm=info['box_price_per_sqm'],
            box_price=info['box_price'],
            # двери
            door_type=info['door_type'],
            door_material_thickness=info['door_material_thickness'],
            door_material_color=info['door_material_color'],
            door_square=size['door_square'],
            door_price_per_sqm=info['door_price_per_sqm'],
            door_price=info['door_price'],
            # фурнитура
            handle_name=info["handle_name"],
            handle_material=info["handle_material"],
            handle_color=info["handle_color"],
            handle_length=info["handle_length"],
            handle_price_per_one=info["handle_price_per_one"],
            handle_ammount=info["handle_ammount"],
            handle_price=info["handle_price"],
            # итоговая цена
            total_price=info['total_price'],
            # владелец
            owner=request.user,
            # дата
            order_date=timezone.now()
        )


class WardrobeOrderDetailView(LoginRequiredMixin, View):
    template_name = 'wardrobe_order_details.html'
    model = Orders

    def get(self, request, pk):
        order_record = get_object_or_404(self.model, pk=pk)
        # Проверка владельца
        if (order_record.owner != request.user and
                not request.user.is_superuser):
            raise Http404
        customer_data = self.prepare_customer_data(order_record)
        order_size = self.prepare_order_size(order_record)
        order_info = self.prepare_order_info(order_record)
        context = {
            'customer_data': customer_data,
            'order_size': order_size,
            'order_info': order_info,
        }
        return render(request, self.template_name, context=context)

    def prepare_customer_data(self, order_record):
        return {
            'order_id': order_record.id,
            'customer_name': order_record.customer_name,
            'customer_surname': order_record.customer_surname,
            'phone': order_record.phone,
            'email': order_record.email,
            'order_date': order_record.order_date,
            'owner': order_record.owner,
        }

    def prepare_order_size(self, order_record):
        return {
            'height': order_record.height,
            'width': order_record.width,
            'depth': order_record.depth,
            'box_square': order_record.box_square,
            'door_square': order_record.door_square,
        }

    def prepare_order_info(self, order_record):
        return {
            'material_type': order_record.material_type,
            'box_material_thickness': order_record.box_material_thickness,
            'box_material_color': order_record.box_material_color,
            'box_price_per_sqm': order_record.box_price_per_sqm,
            'box_square': order_record.box_square,
            'box_price': order_record.box_price,
            # двери
            'door_type': order_record.door_type,
            'door_material_thickness': order_record.door_material_thickness,
            'door_material_color': order_record.door_material_color,
            'door_price_per_sqm': order_record.door_price_per_sqm,
            'door_square': order_record.door_square,
            'door_price': order_record.door_price,
            # фурнитура
            'handle_name': order_record.handle_name,
            'handle_material': order_record.handle_material,
            'handle_color': order_record.handle_color,
            'handle_length': order_record.handle_length,
            'handle_price_per_one': order_record.handle_price_per_one,
            'handle_ammount': order_record.handle_ammount,
            'handle_price': order_record.handle_price,
            # итоговая цена
            'total_price': order_record.total_price,
        }

    def normalize_info(self, info):
        info["material_type"] = info["material_type"].name
        info["material_thickness"] = info["material_thickness"].thickness
        info["material_color"] = info["material_color"].name
        info["door_type"] = info["door_type"].name
        info["handle_type"] = info["handle_type"].name
        info["box_price_per_sqm"] = int(info["box_price_per_sqm"])
        info["door_price_per_sqm"] = int(info["door_price_per_sqm"])
        info["handle_price"] = int(info["handle_price"])
        info["box_price"] = int(info["box_price"])
        info["door_price"] = int(info["door_price"])
        return info


class WardrobeOrderUpdateView(LoginRequiredMixin, UpdateView):
    model = Orders
    form_class = UpdateOrderForm
    template_name = 'wardrobe_order_update.html'
    success_url = reverse_lazy('wardrobe:show_wardrobe_orders')

    def get_object(self):
        order_record = super().get_object()
        # Проверка пользователя
        if (order_record.owner != self.request.user and
                not self.request.user.is_superuser):
            raise Http404
        return order_record


@login_required
def wardrobe_orders_list_view(request):
    if request.user.is_superuser:
        objects_list = Orders.objects.filter(is_active=True).order_by('id')
    else:
        objects_list = Orders.objects.filter(
            owner=request.user, is_active=True).order_by('id')
    template_name = 'wardrobe_orders_list.html'
    context = {
        'title': 'Заказы шкафов',
        'objects_list': objects_list
    }
    return render(request, template_name, context=context)


@login_required
def wardrobe_order_delete_view(request, pk):
    order_record = get_object_or_404(Orders, pk=pk)
    order_number = order_record.id
    # Проверка пользователя
    if order_record.owner != request.user and not request.user.is_superuser:
        raise Http404
    if request.method == 'POST':
        order_record.delete()
        return redirect('wardrobe:show_wardrobe_orders')
    # Страница подтверждения удаления
    template_name = 'common/confirm_delete.html'
    context = {
        'title': 'Вы уверены, что хотите удалить заказ?',
        'message': f'Удалить заказ номер {order_number}'
    }
    return render(request, template_name, context=context)


@login_required
def save_order_success_view(request):
    # Проверим на переход по прямой ссылке
    if not request.session.get('save_order'):
        return redirect('wardrobe:calculator')
    # Создадим ссылку для кнопки
    url = 'wardrobe:show_wardrobe_orders'
    template_name = 'wardrobe_save_order_success.html'
    context = {
        'url': reverse(url),
    }
    return render(request, template_name, context=context)


@login_required
def combination_not_found_view(request):
    # Проверим на переход по прямой ссылке
    error = request.session.pop('combination_error', None)
    if not error:
        return redirect('wardrobe:calculator')
    # Страница комбинация не найдена
    template_name = 'common/combination_not_found.html'
    context = {
        'error': error
    }
    return render(request, template_name, context=context)


# Management
@login_required
def wardrobe_deactivated_list_view(request):
    # Проверка привилегий
    if not request.user.is_superuser:
        raise Http404
    objects_list = Orders.objects.filter(is_active=False).order_by('id')
    template_name = 'wardrobe_orders_list.html'
    context = {
        'title': 'Отмененные заказы шкафов',
        'status': 'inactive',
        'objects_list': objects_list
    }
    return render(request, template_name, context=context)


@login_required
def toggle_order_active_view(request, pk):
    order = get_object_or_404(Orders, pk=pk)
    # Проверка владельца
    if (order.owner != request.user and
            not request.user.is_superuser):
        raise Http404
    # Меняем активность
    order.is_active = not order.is_active
    order.save()
    return redirect('wardrobe:show_wardrobe_orders')


class WardrobeDeactivatedDetailView(LoginRequiredMixin, View):
    template_name = 'wardrobe_deactivated_order_details.html'
    model_orders = Orders

    def get(self, request, pk):
        # Проверка привилегий
        if not request.user.is_superuser:
            raise Http404
        order_record = get_object_or_404(
            self.model_orders, pk=pk, is_active=False)
        customer_data = self.prepare_customer_data(order_record)
        order_size = self.prepare_order_size(order_record)
        order_info = self.prepare_order_info(order_record)
        context = {
            'customer_data': customer_data,
            'order_size': order_size,
            'order_info': order_info,
        }
        return render(request, self.template_name, context=context)

    def prepare_customer_data(self, order_record):
        return {
            'order_id': order_record.id,
            'customer_name': order_record.customer_name,
            'customer_surname': order_record.customer_surname,
            'phone': order_record.phone,
            'email': order_record.email,
            'order_date': order_record.order_date,
            'owner': order_record.owner,
        }

    def prepare_order_size(self, order_record):
        return {
            'height': order_record.height,
            'width': order_record.width,
            'depth': order_record.depth,
            'box_square': order_record.box_square,
            'door_square': order_record.door_square,
        }

    def prepare_order_info(self, order_record):
        return {
            'material_type': order_record.material_type,
            'box_material_thickness': order_record.box_material_thickness,
            'box_material_color': order_record.box_material_color,
            'box_price_per_sqm': order_record.box_price_per_sqm,
            'box_square': order_record.box_square,
            'box_price': order_record.box_price,
            # двери
            'door_type': order_record.door_type,
            'door_material_thickness': order_record.door_material_thickness,
            'door_material_color': order_record.door_material_color,
            'door_price_per_sqm': order_record.door_price_per_sqm,
            'door_square': order_record.door_square,
            'door_price': order_record.door_price,
            # фурнитура
            'handle_name': order_record.handle_name,
            'handle_material': order_record.handle_material,
            'handle_color': order_record.handle_color,
            'handle_length': order_record.handle_length,
            'handle_price_per_one': order_record.handle_price_per_one,
            'handle_ammount': order_record.handle_ammount,
            'handle_price': order_record.handle_price,
            # итоговая цена
            'total_price': order_record.total_price,
        }
