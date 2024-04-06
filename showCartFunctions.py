# File name: showCartFunctions.py
# Author: Jasmin Fränti
# Description: Functions that are related to clicking the Show Shopping Cart-button


import addToCartFunctions as addcart
import productListFunctions as pf
import widgetsManagement as wm
from tkinter import messagebox

def show_shopping_cart(win):
    pf.update_product_list(win.shopping_cart, win.observable_list_objects)

    if not win.shopping_cart:
        messagebox.showinfo("Shopping cart is empty", "No products in cart")

    wm.toggle_total_sum_label(win.total_sum_label, "on", win)
    wm.show_widget(win.remove_from_cart_button, 250, 450)
    wm.hide_widget(win.sort_button)
    wm.hide_widget(win.search_button)
    wm.hide_widget(win.add_button)
    wm.hide_widget(win.show_cart_button)
    wm.show_widget(win.continue_button, 250, 20)
    wm.hide_widget(win.login_button)
    wm.show_widget(win.save_order_button, 250, 550)


def continue_shopping(win):
    wm.toggle_total_sum_label(win.total_sum_label, "off", win)
    wm.show_widget(win.sort_button, 350, 20)
    wm.show_widget(win.show_cart_button, 620, 20)
    wm.show_widget(win.search_button, 250, 20)
    wm.show_widget(win.add_button, 300, 600)
    wm.hide_widget(win.continue_button)
    wm.hide_widget(win.remove_from_cart_button)
    wm.show_widget(win.login_button, 920, 20)
    pf.update_product_list(win.list_items, win.observable_list_objects)
    wm.hide_widget(win.save_order_button)
