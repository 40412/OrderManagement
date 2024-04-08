# File name: widgetsManagement.py
# Author: Jasmin Fränti
# Description: This file contains functions to manage tkinter window widgets

import tkinter as tk

def hide_widget(widget):
    widget.place_forget()

def disable_button(button):
    button.config(state=tk.DISABLED)

def enable_button(button):
    button.config(state=tk.ACTIVE)

def show_widget(widget, x_pos, y_pos):
    widget.place(x=x_pos, y=y_pos)


def toggle_total_sum_label(label, onoff, win):
    if onoff == "on":
        label.place(x=180, y=500)
        label.config(text="Total sum: $" + str(win.total_sum))
    elif onoff == "off":
        label.place_forget()