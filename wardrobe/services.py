import math
from decimal import Decimal


class CalculateWardrobe:
    """ Wardrode Price Calculation """


    def calculate_price(self, info, size):
        """ 
        Calculate calculate 
        :param info:
        :param size:
        :return:
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
        # Считаем все вместе
        return math.ceil(box_price + door_price + handle_price)
        
    def calc_box_square(self, size):
        height = size["height"] / 1000
        width = size["width"] / 1000
        depth = size["depth"] / 1000
        return Decimal((height * 2 + width * 2) * depth)

    def calc_door_square(self, size):
        height = size["height"] / 1000
        width = size["width"] / 1000
        return Decimal(height * width)
