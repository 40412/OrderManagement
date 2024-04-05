# File name: product.py
# Author: Jasmin Fränti
# Description: This file contains the class "Product"


class Product:

    def __init__(self, name, unit_price):
        self.name = name
        self.unit_price = unit_price

    def __eq__(self, other):
        if isinstance(other, Product):
            return self.name == other.name and self.unit_price == other.unit_price
        return False


    def __str__(self):
        return self.name + "  " + self.unit_price + "$"

    """Getters and setters for all class attributes"""
    
    def get_product_name(self):
        return self.name
    
    def get_unit_price(self):
        return self.unit_price
    
    def set_name(self, name):
        self.name = name

    def set_unit_price(self, price):
        self.unit_price = price

    @staticmethod
    def get_selected_products():
        from addToCartFunctions import added_products
        
        selected_products = []
        with open("initialproducts", "r") as file:
            for line in file:
                name, price = line.strip().split(",")
                product = Product(name, price)
                if product in added_products:
                    selected_products.append(product)
        return selected_products


