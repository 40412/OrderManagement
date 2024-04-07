# File name: order.py
# Author: Eetu Salminen
# Description: This file contains functionality for managing orders

from user import UserManager


class Order:
    def __init__(self, order_items):
        self.order_items = order_items

    def save_order(self):
        with open("order.txt", "a") as file: # The file is opened in append mode, so the previous orders are not overwritten
            file.write("\n\nOrder details:\n")
            file.write(f"Customer: {UserManager.current_user['username']}\n")
            for index, item in enumerate(self.order_items, start=1):
                file.write(f"Product {index}: {item.get_product_name()} - Price: {item.get_unit_price()}$\n")
            file.write(f"Total sum: ${self.calculate_total_sum()}")

    def calculate_total_sum(self):
        return round(sum(float(item.get_unit_price()) for item in self.order_items), 2)

# class to handle vip discounts
class SpecialOrder(Order):
    # constructor
    def __init__(self, order_items):
        super().__init__(order_items)
        
    # overrides the parent function and adds calculate the VIP discount functionality
    def save_order(self):
        super().save_order()
        with open("order.txt", "a") as file:
            file.write(f"\nAfter VIP discount: ${self.calculate_vip_discount()}")
            
    def calculate_vip_discount(self):
        return round(self.calculate_total_sum() * 0.9, 2)
