# File name: main.py
# Author: Jasmin Fränti
# Description: Main file that defines and starts the graphical user interface

import tkinter as tk
import productListFunctions as pf
import addToCartFunctions as add_cart
import showCartFunctions as showcart
import modifyProductList as mp
from tkinter import ttk
from tkinter import messagebox
from product import Product

class MyWindow(ttk.Frame):
    """Defines the buttons and text inside the graphical user interface window"""
    def __init__(self, win):
        ttk.Frame.__init__(self)
        self.list_items = pf.create_all_products_list()
        self.observable_list_objects = tk.StringVar(value=self.list_items)
        self.list_of_products = tk.Listbox(win, listvariable=self.observable_list_objects,
                                            width=50, height=window.winfo_screenheight(), 
                                            selectmode=tk.MULTIPLE, background='#D1E8E2')
        self.list_of_products.place(x=50, y=50)
        self.search_bar = tk.Entry(win, background='#E2E2E2')
        self.search_bar.place(x=50, y=20)
        self.search_button = ttk.Button(win, text="Search", 
                                       command=lambda: pf.search_button_clicked(self))
        self.search_button.place(x=220, y=18)
        self.add_button = ttk.Button(win, text="Add to Shopping Cart", 
                                    command=lambda: add_cart.add_button_clicked(self))
        self.add_button.place(x=440, y=18)
        self.shopping_cart = []
        self.sort_button = ttk.Button(win, text="Sort",
                                     command=lambda: pf.sort_product_list(self))
        self.sort_button.place(x=330, y=18)
        self.show_cart_button = ttk.Button(win, text="Show Shopping Cart", 
                                          command=lambda: showcart.show_shopping_cart(self))
        self.show_cart_button.place(x=455, y=500)
        self.continue_button = ttk.Button(win, text="Continue Shopping", 
                                         command=lambda: showcart.continue_shopping(self))
        self.total_sum = 0
        self.total_sum_label = tk.Label(win, text="Total sum: " + str(self.total_sum))
        self.remove_from_cart_button = ttk.Button(win, text="Remove from Shopping Cart", 
                                                 command=lambda: add_cart.remove_from_cart(self))
        self.login_button = ttk.Button(win, text="Log in as Admin", 
                                      command=lambda: mp.admin_log_in(self))
        self.login_button.place(x=800, y=0)
        self.add_label = tk.Label(win, text="Add new product")
        self.new_product_box = tk.Entry(win)
        self.price_box = tk.Entry(win)
        self.save_button = ttk.Button(win, text="Save", 
                                     command=lambda: mp.save_button_clicked(self))
        self.remove_products_button = ttk.Button(text="Remove", 
                                                command=lambda: mp.remove_products(self))

        self.save_order_button = ttk.Button(win, text="Send Order", 
                                    command=lambda: self.save_order_and_show_message())
        self.save_order_button.place(x=600, y=500)

    def set_total_sum(self, sum):
        self.total_sum = sum

    def get_total_sum(self):
        return self.total_sum
    
    def save_order(self, order_items):  
        with open("order.txt", "w") as file:
            for index, item in enumerate(order_items, start=1):
                file.write(f"Product {index}: {item.get_product_name()} - Price: {item.get_unit_price()}$\n")

    def save_order_and_show_message(self):
        order = self.generate_order()  
        self.save_order(order) 
        messagebox.showinfo("Order sent", "Your order has been sent successfully!")

    def generate_order(self):
        selected_products = Product.get_selected_products()
        return selected_products
    
window = tk.Tk()
ui = MyWindow(window)
window['background'] = '#A9D6E5'
style = ttk.Style()
style.configure("TButton", background="#D1E8E2", foreground="black")
style.map('TButton', foreground = [('active', '!disabled', 'black')],
                     background = [('active', 'white')])
window.title("Buy something! Anything!")
window.geometry("{}x{}".format(window.winfo_screenwidth(), window.winfo_screenheight()))
window.mainloop()
