# File name: modifyProductList.py
# Author: Jasmin Fränti
# Description: This file contains functionality for shop owner/admin to add, remove or modify
# products in the products list

import widgetsManagement as wm
import tkinter as tk
import productListFunctions as pf

def admin_log_in(win):
    wm.disable_button(win.show_cart_button)
    wm.disable_button(win.add_button)
    wm.show_widget(win.add_label, 650, 200)
    wm.show_widget(win.new_product_box, 650, 250)
    win.new_product_box.insert(0, "Product name")
    win.new_product_box.bind('<FocusIn>', lambda event: 
                             clear_entry(event, win.new_product_box)) # Clears the text when the box is clicked
    wm.show_widget(win.price_box, 650, 300)
    win.price_box.insert(0, "Price")
    win.price_box.bind('<FocusIn>', lambda event: 
                             clear_entry(event, win.price_box))
    wm.show_widget(win.save_button, 700, 350)
    win.login_button.config(text="Log out", command=lambda: log_out(win))
    wm.show_widget(win.remove_products_button, 455, 200)
    win.list_of_products.config(selectmode=tk.SINGLE)

def log_out(win):
    wm.enable_button(win.show_cart_button)
    wm.enable_button(win.add_button)
    wm.hide_widget(win.add_label)
    wm.hide_widget(win.new_product_box)
    wm.hide_widget(win.price_box)
    wm.hide_widget(win.save_button)
    win.login_button.config(text="Log in as Admin", command=lambda: admin_log_in(win))
    wm.hide_widget(win.remove_products_button)
    win.list_of_products.config(selectmode=tk.MULTIPLE)


def save_button_clicked(win):
    name = win.new_product_box.get()
    price = win.price_box.get()
    line = name + "," + price + "\n"

    if validate_name(name) and validate_price(price):
        product_file = open("initialProducts", "a")
        product_file.write(line)
        product_file.close()
    else:
        tk.messagebox.showinfo("Incorrect input", 
                               "Product name cannot be longer than 50 characters. Price has to be a number")

    win.list_items.clear() # Empties the list of all products
    win.list_items = pf.create_all_products_list() # Lists all the products again from the file
    pf.update_product_list(win.list_items, win.observable_list_objects) # Updates the list in the UI

def clear_entry(event, entry):
    entry.delete(0, tk.END)

def validate_name(name): # returns true or false based on the length of the name
    return len(name) < 51

def validate_price(price): # returns true or false depending if price is all numbers or not
    numbers = price.replace(".", "", 1)
    return numbers.isdigit()

def remove_products(win):
    lbox = win.list_of_products
    selected_indices = lbox.curselection()
    removable_items = []
    not_removable = False

    # creates a list of names to be removed
    for index in selected_indices:
        product_name = lbox.get(index).rsplit(" ", 1)[0].strip()
        removable_items.append(product_name)

    file = open("initialProducts", "r")
    lines = file.readlines() # Saves the file as lines in the variable
    file.close()

    if removable_items:

        file = open("initialProducts", "w")

        for line in lines:
            # checks if the line should be written in the file or not
            for item in removable_items:

                if item != line.rsplit(",", 1)[0].strip():
                    not_removable = True
                else:
                    not_removable = False
            
            if not_removable:
                file.write(line)

        file.close()

    win.list_items.clear()
    win.list_items = pf.create_all_products_list()

    pf.update_product_list(win.list_items, win.observable_list_objects)
