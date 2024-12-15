import tkinter as tk
from tkinter import messagebox
import os
from tkinter import filedialog

def info():
    messagebox.showinfo("Информация", "Добро пожаловать в Блокнот!\n\n"
                                        "Чтобы добавить текст, просто начните печатать.\n"
                                        "Чтобы сохранить текст, нажмите Ctrl+S.\n"
                                        "Чтобы открыть файл, нажмите Ctrl+O.\n"
                                        "Чтобы выйти из программы, нажмите Ctrl+Q.")

def about():
    messagebox.showinfo("О программе", "Блокнот\n\n"
                                       "Автор: Арсений Тызыхян\n"
                                       "Версия: 1.0")
root = tk.Tk()
root.title("Блокнот")

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Инфо", command=info)
filemenu.add_command(label="О программе", command=about)
filemenu.add_separator()
filemenu.add_command(label="Выход", command=root.quit)
menubar.add_cascade(label="Файл", menu=filemenu)

root.config(menu=menubar)

text = tk.Text(root)
text.pack(expand=True, fill="both")

root.mainloop()