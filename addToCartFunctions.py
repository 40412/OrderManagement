# File name: addTCartFunctions.py
# Author: Jasmin Fränti
# Description: This file contains functionality to add products to shopping cart

import productListFunctions as pf
from tkinter import messagebox

def add_button_clicked(win):
    listbox = win.list_of_products
    objects = win.list_items
    cart = win.shopping_cart
    selected_indices = listbox.curselection()
    cart_total = win.total_sum
    products_added = False

    for index in selected_indices:
        product_name = listbox.get(index).rsplit(" ", 1)[0].strip()

        for object in objects:
            if product_name in object.get_product_name() and object not in cart:
                cart.append(object)
                cart_total += float(object.get_unit_price())
                cart_total = round(cart_total, 2)
                products_added = True
    
    win.total_sum = cart_total
    update_cart_sum(win.total_sum_label, win)

    if products_added:
        messagebox.showinfo("Products added", "Products were added to cart")

def update_cart_sum(label, win):
    label.config(text="Total sum: $" + str(win.total_sum)) # Sets the text of the label in UI
    
def remove_from_cart(win):
    lbox = win.list_of_products
    selected_indices = lbox.curselection()

    for index in selected_indices:
        product_name = lbox.get(index).rsplit(" ", 1)[0].strip()

        for item in win.shopping_cart:
            if product_name in item.get_product_name():
                win.total_sum -= float(item.get_unit_price())
                win.total_sum = round(win.total_sum, 2)
                win.shopping_cart.remove(item)

    update_cart_sum(win.total_sum_label, win)
    pf.update_product_list(win.shopping_cart, win.observable_list_objects)
