# File name: productListFunctions.py
# Author: Jasmin Fränti
# Description: This file contains all product list functions like listing the products and sorting the list

import product as prod

def create_all_products_list():
    """Reads the initial_products-file and creates objects from each row.
    Then lists all the products"""

    products_file = open("initialProducts","r")
    lines = products_file.readlines()
    products_file.close()
    products_list = []
    
    for line in lines:
        product_split = line.strip().split(",")
        product_name = product_split[0]
        product_price = product_split[1]
        product = prod.Product(product_name, product_price)
        products_list.append(product)

    sorted_list = sorted(products_list, key=lambda x: x.name)
    return sorted_list

def search_button_clicked(win):
    search_bar = win.search_bar
    list_items = win.list_items
    observable = win.observable_list_objects
    entry = search_bar.get().lower()
    products_file = open("initialProducts","r")
    lines = products_file.readlines()
    products_file.close()
    list_items.clear()

    for line in lines:
        product_split = line.strip().split(",")
        product_name = product_split[0]
        product_price = product_split[1]
        product = prod.Product(product_name, product_price)

        if entry != "" and entry != " ":
            
            if entry in product.get_product_name().lower():
                list_items.append(product)

        else:
            list_items.append(product)

    list_items = sorted(list_items, key=lambda x: x.name)
    update_product_list(list_items, observable)

def update_product_list(list, observable):
    observable.set(list)

def sort_product_list(win):
    list_items = win.list_items
    observable_list = win.observable_list_objects
    is_sorted_ascending = all(list_items[i].name <= list_items[i + 1].name 
                              for i in range(len(list_items) - 1))
    
    if is_sorted_ascending:
        sorted_items = sorted(list_items, key=lambda x: x.name, reverse=True)

    else:
        sorted_items = sorted(list_items, key=lambda x: x.name)
    
    list_items.clear()

    for i in sorted_items:
        list_items.append(i)

    update_product_list(list_items, observable_list)
            
