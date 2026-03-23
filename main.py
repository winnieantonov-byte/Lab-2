import tkinter as tk
from tkinter import messagebox
import random
import string


def generate_block():
    digits = random.choices(string.digits, k=2)
    letters = random.choices(string.ascii_uppercase, k=3)
    block_list = digits + letters
    random.shuffle(block_list)
    return "".join(block_list)


def generate_key():
    key = f"{generate_block()}-{generate_block()}-{generate_block()}"
    key_entry.delete(0, tk.END)
    key_entry.insert(0, key)


root = tk.Tk()
root.title("Key Generator - Red Edition")
root.geometry("500x350")
root.resizable(False, False)
root.configure(bg='#1a0000')

title_label = tk.Label(root, text="KENERATOR", font=("Courier", 20, "bold"), 
                       fg="#ff0000", bg="#1a0000")
title_label.pack(pady=20)

key_entry = tk.Entry(root, font=("Courier", 18), justify='center', 
                     fg="#ff0000", bg="#2b0000", insertbackground='white',
                     highlightthickness=1, highlightbackground="#ff0000")
key_entry.pack(pady=20, padx=50, fill='x')

gen_button = tk.Button(root, text="GENERATE", font=("Courier", 14, "bold"),
                       command=generate_key, fg="#ffffff", bg="#aa0000",
                       activebackground="#ff0000", activeforeground="#ffffff", 
                       cursor="hand2", bd=0)
gen_button.pack(pady=10)

root.mainloop()
