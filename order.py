# File name: order.py
# Author: Eetu Salminen
# Description: This file contains functionality for managing orders

class Order:
    def __init__(self, order_items):
        self.order_items = order_items

    def save_order(self):
        with open("order.txt", "w") as file:
            file.write("Order details:\n")
            for index, item in enumerate(self.order_items, start=1):
                file.write(f"Product {index}: {item.get_product_name()} - Price: {item.get_unit_price()}$\n")
            file.write(f"Total sum: ${self.calculate_total_sum()}")

    def calculate_total_sum(self):
        return sum(float(item.get_unit_price()) for item in self.order_items)

