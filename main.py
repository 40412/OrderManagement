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
from order import Order, SpecialOrder
from user import UserManager

class LoginWindow(ttk.Frame):
    """Defines the login window"""

    def __init__(self, win):
        ttk.Frame.__init__(self)
        
        self.username_label = ttk.Label(win, text="Username:")
        self.username_label.place(x=50, y=50)
        
        self.username_entry = ttk.Entry(win)
        self.username_entry.place(x=150, y=50)
        
        self.password_label = ttk.Label(win, text="Password:")
        self.password_label.place(x=50, y=80)
        
        self.password_entry = ttk.Entry(win, show="*")
        self.password_entry.place(x=150, y=80)
        
        self.login_button = ttk.Button(win, text="Login", command=self.login)
        self.login_button.place(x=100, y=120)
        
        self.register_button = ttk.Button(win, text="Register", command=self.register)
        self.register_button.place(x=200, y=120)
        
        self.login_successful = False  # Initialize login_successful attribute

        self.error_message = tk.StringVar()
        self.success_message = tk.StringVar()

        self.error_label = ttk.Label(win, textvariable=self.error_message)
        
        self.success_label = ttk.Label(win, textvariable=self.success_message)

    def login(self):
        self.error_label.place_forget()  # Remove error label
        self.success_label.place_forget()  # Remove success label

        username = self.username_entry.get()
        password = self.password_entry.get()
    
        authenticated = UserManager.authenticate_user(username, password)
    
        if authenticated:
            self.login_successful = True  # Set login_successful to True
            MyWindow(self.master)  # Show the main window
        
            # Hide the login widgets
            self.username_label.place_forget()
            self.username_entry.place_forget()
            self.password_label.place_forget()
            self.password_entry.place_forget()
            self.login_button.place_forget()
            self.register_button.place_forget()
        
        else:
            # Display an error message
            self.error_message.set("Invalid username or password")
            self.error_label.place(x=100, y=170)


    def register(self):
        self.error_label.place_forget()  # Remove error label
        self.success_label.place_forget()  # Remove success label
    
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        UserManager.create_user(username=username, password=password)
        
        # Display a success message
        self.success_message.set("Registration successful")
        self.success_label.place(x=100, y=170)


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
        self.add_button.place(x=200, y=600)
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
        self.login_button.place(x=920, y=20)
        self.add_label = tk.Label(win, text="Add new product")
        self.new_product_box = tk.Entry(win)
        self.price_box = tk.Entry(win)
        self.save_button = ttk.Button(win, text="Save", 
                                     command=lambda: mp.save_button_clicked(self))
        self.remove_products_button = ttk.Button(text="Remove", 
                                                command=lambda: mp.remove_products(self))

        self.save_order_button = ttk.Button(win, text="Send Order", 
                                    command=lambda: self.save_order_and_show_message())
    
        self.become_vip_button = ttk.Button(win, text="Become VIP", 
                                            command=lambda: self.become_vip())
        self.become_vip_button.place(x=790, y=20)
        

    def set_total_sum(self, sum):
        self.total_sum = round(sum, 2)

    def get_total_sum(self):
        return self.total_sum
    
# Save the order and display a message indicating successful saving.
    def save_order(self):
        order = Order(self.shopping_cart) 
        order.save_order()  
        messagebox.showinfo("Order Saved", "Your order has been saved successfully!")

    def save_order_and_show_message(self):
        # Check if the user is a VIP
        if UserManager.current_user['is_vip']:
            order = SpecialOrder(self.shopping_cart)
            order.save_order()
            messagebox.showinfo("Order Saved", "Your order has been saved successfully! VIP discount applied.")
        else:
            self.save_order()

# Generate an order based on selected products.
    def generate_order(self):
        selected_products = Product.get_selected_products()
        return selected_products
    
    def become_vip(self):
        UserManager.become_vip(UserManager.current_user['id'])

        # Apply 10% discount to the total sum
        # self.total_sum *= 0.9
        # self.total_sum_label.config(text="Total sum: $" + str(round(self.total_sum, 2)))

        # Display message in the window
        messagebox.showinfo("VIP Status", "You have become a VIP!\nYou get-10% discount at the shopping cart")

        # Disable the "Become VIP" button
        self.become_vip_button.config(state=tk.DISABLED)
        self.become_vip_button.place_forget()
    
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
