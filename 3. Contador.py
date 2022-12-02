#3: Contador

import tkinter as tk
from tkinter import ttk

def sumar():
    numero.set(str(int(numero.get()) + 1))  
    
root = tk.Tk()
root.title("Contador")
root.geometry("400x200")
root.config(bg="#404258")

numero = tk.StringVar(root, "0")
num = tk.Entry(root, textvariable=numero, justify="center")
num.pack()
num.place(x=140, y=50)

contador = ttk.Button(root, text="+", command=sumar)
contador.pack()
contador.place(x=165, y=90)

root.mainloop() 