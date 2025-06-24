import math


class CalculateWardrobe:
    """ 
    Wardrode Price Calculation 

    size = {
        "height": высота мм,
        "width": ширина мм,
        "depth": глубина мм
    }

    info = {
        "box_price_per_sqm": стоимость материала короба за м.кв.,
        "door_price_per_sqm": стоимость материала двери за м.кв.,
        "handle_price": стоимость дверной ручки,
    }
    """


    def calculate_price(self, size, info):
        """ 
        Calculate calculate 
        :param info: dict with info
        :param size: dict with size
        :return: updated size, info
        """
        # Распаковываем необходимые данные
        box_price_per_sqm = info["box_price_per_sqm"]
        door_price_per_sqm = info["door_price_per_sqm"]
        handle_price = info["handle_price"]
        # Считаем площади
        box_square = self.calc_box_square(size)
        door_square = self.calc_door_square(size)
        # Считаем цену коробки и дверей
        box_price = box_price_per_sqm * box_square
        door_price = door_price_per_sqm * door_square
        total_price = math.ceil(box_price + door_price + handle_price * 2)
        # Сохраняем результат в словарь
        size["box_square"] = box_square
        size["door_square"] = door_square
        info["box_price"] = box_price
        info["door_price"] = door_price
        info["total_price"] = total_price
        return size, info       

    def calc_box_square(self, size):
        height = size["height"] / 1000
        width = size["width"] / 1000
        depth = size["depth"] / 1000
        return math.ceil((height * 2 + width * 2) * depth)

    def calc_door_square(self, size):
        height = size["height"] / 1000
        width = size["width"] / 1000
        return math.ceil(height * width)
