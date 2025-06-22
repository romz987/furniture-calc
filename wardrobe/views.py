from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import WardrobeForm, SaveOrderForm
from django.views import View
from reference.models import BoxSummary, DoorSummary, DoorHandle
from .services import CalculateWardrobe


class WardrobeView(View):
    template = 'wardrobe.html'
    template_result = 'wardrobe_result.html'


    def get(self, request):
        form = WardrobeForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = WardrobeForm(request.POST)
        if form.is_valid():
            # Упаковываем данные из запроса в два словаря
            info, size = self.extract_data(form)
            # Получаем стоимости за квадратный метр
            info["box_price_per_sqm"] = self.get_box_material_price(info)
            if not info["box_price_per_sqm"]:
                messages.error(request, "Комбинация для корпуса не найдена")
                return redirect('wardrobe:combination_not_found')
            info["door_price_per_sqm"] = self.get_door_material_price(info)
            if not info["door_price_per_sqm"]:
                messages.error(request, "Комбинация для двери не найдена")
                return redirect('wardrobe:combination_not_found')
            # Получаем стоимость выбранной ручки 
            info["handle_price"] = self.get_handle_price(info)
            # Считаем
            calculator = CalculateWardrobe()
            size, info = calculator.calculate_price(size, info)
            # На страницу результатов
            return render(
                request, 
                self.template_result, 
                {'form': form, 'size': size, 'info': info}
            )
        return render(request, self.template, {'form': form})

    def extract_data(self, form):
        info = {
            "material_type": form.cleaned_data["material"],
            "material_thickness": form.cleaned_data["thickness"],
            "material_color": form.cleaned_data["color"],
            "door_type": form.cleaned_data["door_type"],
            # id толщины двери
            "door_thickness": 1,
            "handle_type": form.cleaned_data["handle_type"]
        }
        size = {
            "height": int(form.cleaned_data["height"]),
            "width": int(form.cleaned_data["width"]),
            "depth": int(form.cleaned_data["depth"])
        }
        return info, size

    def get_box_material_price(self, info):
        box = BoxSummary.objects.filter(
            material_type=info["material_type"],
            material_thickness=info["material_thickness"],
            material_color=info["material_color"]
        ).first()
        return box.price_per_sqm if box else None

    def get_door_material_price(self, info):
        door = DoorSummary.objects.filter(
            material_type=info["material_type"],
            material_thickness=info["door_thickness"],
            material_color=info["material_color"],
            door_type=info["door_type"]
        ).first()
        return door.price_per_sqm if door else None

    def get_handle_price(self, info):
        handle = DoorHandle.objects.filter(
            name=info["handle_type"]
        ).first()
        return handle.price_per_one 


class WardrobeSaveOrderView(View):
    template = 'wardrobe_save_order.html'

    def get(self, request):
        form = SaveOrderForm()
        return render(request, self.template, {'form': form})


def combination_not_found(request):
    return render(request, 'combination_not_found.html', {'title': 'Ошибка'})
