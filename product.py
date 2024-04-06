# File name: product.py
# Author: Jasmin Fränti
# Description: This file contains the class "Product"


class Product:

    def __init__(self, name, unit_price):
        self.__name = name
        self.__unit_price = unit_price

    def __eq__(self, other):
        if isinstance(other, Product):
            return self.__name == other.__name and self.__unit_price == other.__unit_price
        return False


    def __str__(self):
        return self.__name + "  " + self.__unit_price + "$"

    """Getters and setters for all class attributes"""
    
    def get_product_name(self):
        return self.__name
    
    def get_unit_price(self):
        return self.__unit_price
    
    def set_name(self, name):
        self.__name = name

    def set_unit_price(self, price):
        self.__unit_price = price

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


