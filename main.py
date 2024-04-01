# File name: main.py
# Author: Jasmin Fränti
# Description: Main file that defines and starts the graphical user interface

import tkinter as tk
import productListFunctions as pf
import addToCartFunctions as add_cart
import showCartFunctions as showcart
import modifyProductList as mp

class MyWindow():

    """Defines the buttons and text inside the graphical user interface window"""
    def __init__(self, win):
        self.list_items = pf.create_all_products_list()
        self.observable_list_objects = tk.StringVar(value=self.list_items)
        self.list_of_products = tk.Listbox(win, listvariable=self.observable_list_objects,
                                            width=50, height=window.winfo_screenheight(), 
                                            selectmode=tk.MULTIPLE)
        self.list_of_products.place(x=50, y=50)
        self.search_bar = tk.Entry(win)
        self.search_bar.place(x=50, y=20)
        self.search_button = tk.Button(win, height=1, text="Search", 
                                       command=lambda: pf.search_button_clicked(self))
        self.search_button.place(x=220, y=18)
        self.add_button = tk.Button(win, text="Add to Shopping Cart", 
                                    command=lambda: add_cart.add_button_clicked(self))
        self.add_button.place(x=455, y=100)
        self.shopping_cart = []
        self.sort_button = tk.Button(win, text="Sort", 
                                     command=lambda: pf.sort_product_list(self))
        self.sort_button.place(x=300, y=18)
        self.show_cart_button = tk.Button(win, text="Show Shopping Cart", 
                                          command=lambda: showcart.show_shopping_cart(self))
        self.show_cart_button.place(x=455, y=60)
        self.continue_button = tk.Button(win, text="Continue Shopping", 
                                         command=lambda: showcart.continue_shopping(self))
        self.total_sum = 0
        self.total_sum_label = tk.Label(win, text="Total sum: " + str(self.total_sum))
        self.remove_from_cart_button = tk.Button(win, text="Remove from Shopping Cart", 
                                                 command=lambda: add_cart.remove_from_cart(self))
        self.login_button = tk.Button(win, text="Log in as Admin", 
                                      command=lambda: mp.admin_log_in(self))
        self.login_button.place(x=650, y=0)
        self.add_label = tk.Label(win, text="Add new product")
        self.new_product_box = tk.Entry(win)
        self.price_box = tk.Entry(win)
        self.save_button = tk.Button(win, text="Save", 
                                     command=lambda: mp.save_button_clicked(self))
        self.remove_products_button = tk.Button(text="Remove", 
                                                command=lambda: mp.remove_products(self))

    def set_total_sum(self, sum):
        self.total_sum = sum

    def get_total_sum(self):
        return self.total_sum

window = tk.Tk()
ui = MyWindow(window)
window.title("Buy something! Anything!")
window.geometry("{}x{}".format(window.winfo_screenwidth(), window.winfo_screenheight()))
window.mainloop()