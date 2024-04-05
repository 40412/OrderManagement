# File name: main.py
# Author: Jasmin Fränti, Elina Maunula, Eetu Salminen
# Description: Main file that defines and starts the graphical user interface

import tkinter as tk
import productListFunctions as pf
import addToCartFunctions as add_cart
import showCartFunctions as showcart
import modifyProductList as mp
from tkinter import ttk
from tkinter import messagebox
from product import Product
from order import Order
from user import UserManager

class LoginWindow(ttk.Frame):
    """Defines the login window"""

    def __init__(self, win):
        ttk.Frame.__init__(self)
        
        self.username_label = ttk.Label(win, text="Username:")
        self.username_label.grid(row=0, column=0, pady=10)
        
        self.username_entry = ttk.Entry(win)
        self.username_entry.grid(row=0, column=1, pady=5)
        
        self.password_label = ttk.Label(win, text="Password:")
        self.password_label.grid(row=1, column=0, pady=10)
        
        self.password_entry = ttk.Entry(win, show="*")
        self.password_entry.grid(row=1, column=1, pady=5)
        
        self.login_button = ttk.Button(win, text="Login", command=self.login)
        self.login_button.grid(row=2, column=0, pady=20)
        
        self.register_button = ttk.Button(win, text="Register", command=self.register)
        self.register_button.grid(row=2, column=1, pady=10)
        
        self.login_successful = False  # Initialize login_successful attribute

        self.error_message = tk.StringVar()
        self.success_message = tk.StringVar()

        self.error_label = ttk.Label(win, textvariable=self.error_message)
        self.success_label = ttk.Label(win, textvariable=self.success_message)

    def login(self):
        self.error_label.grid_remove()  # Remove error label
        self.success_label.grid_remove()  # Remove success label

        username = self.username_entry.get()
        password = self.password_entry.get()
        
        authenticated = UserManager.authenticate_user(username, password)
        
        if authenticated:
            self.login_successful = True  # Set login_successful to True
            MyWindow(self.master)  # Show the main window
            
            # Hide the login widgets
            self.username_label.grid_forget()
            self.username_entry.grid_forget()
            self.password_label.grid_forget()
            self.password_entry.grid_forget()
            self.login_button.grid_forget()
            self.register_button.grid_forget()
            
        else:
            # Display an error message
            self.error_message.set("Invalid username or password")
            self.error_label.grid(row=3, columnspan=2, pady=10)

    def register(self):
        self.error_label.grid_remove()  # Remove error label
        self.success_label.grid_remove()  # Remove success label
    
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        UserManager.create_user(username=username, password=password)
        
        # Display a success message
        self.success_message.set("Registration successful")
        self.success_label.grid(row=3, columnspan=2, pady=10)


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
        self.search_button.place(x=250, y=20)
        self.add_button = ttk.Button(win, text="Add to Shopping Cart", 
                                    command=lambda: add_cart.add_button_clicked(self))
        self.add_button.place(x=300, y=600)
        self.shopping_cart = []
        self.sort_button = ttk.Button(win, text="Sort",
                                     command=lambda: pf.sort_product_list(self))
        self.sort_button.place(x=350, y=20)
        self.show_cart_button = ttk.Button(win, text="Show Shopping Cart", 
                                          command=lambda: showcart.show_shopping_cart(self))
        self.show_cart_button.place(x=620, y=20)
        self.continue_button = ttk.Button(win, text="Continue Shopping", 
                                         command=lambda: showcart.continue_shopping(self))
        self.total_sum = 0
        self.total_sum_label = tk.Label(win, text="Total sum: " + str(self.total_sum))
        self.remove_from_cart_button = ttk.Button(win, text="Remove from Shopping Cart", 
                                                 command=lambda: add_cart.remove_from_cart(self))
        self.login_button = ttk.Button(win, text="Log in as Admin", 
                                      command=lambda: mp.admin_log_in(self))
        self.login_button.place(x=800, y=20)
        self.add_label = tk.Label(win, text="Add new product")
        self.new_product_box = tk.Entry(win)
        self.price_box = tk.Entry(win)
        self.save_button = ttk.Button(win, text="Save", 
                                     command=lambda: mp.save_button_clicked(self))
        self.remove_products_button = ttk.Button(text="Remove", 
                                                command=lambda: mp.remove_products(self))

        self.save_order_button = ttk.Button(win, text="Send Order", 
                                    command=lambda: self.save_order_and_show_message())
    

        

    def set_total_sum(self, sum):
        self.total_sum = sum

    def get_total_sum(self):
        return self.total_sum

    def save_order(self):
        order = Order(self.shopping_cart)  # Luo tilauksen olio ja välitä sille ostoskori
        order.save_order()  # Tallenna tilaus
        messagebox.showinfo("Order Saved", "Your order has been saved successfully!")

    def save_order_and_show_message(self):
        self.save_order()

    def generate_order(self):
        selected_products = Product.get_selected_products()
        return selected_products
    
if __name__ == "__main__":
    window = tk.Tk()
    window['background'] = '#A9D6E5'
    style = ttk.Style()
    style.configure("TButton", background="#D1E8E2", foreground="black")
    style.map('TButton', foreground=[('active', '!disabled', 'black')],
              background=[('active', 'white')])
    window.title("Buy something! Anything!")
    window.geometry("{}x{}".format(window.winfo_screenwidth(), window.winfo_screenheight()))
    
    login_window = LoginWindow(window)
    
    window.mainloop()
