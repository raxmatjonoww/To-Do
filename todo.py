import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Ogohlantirish", "Vazifa matnini kiriting!")

def delete_task():
    try:
        selected_index = listbox.curselection()[0]
        tasks.pop(selected_index)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Ogohlantirish", "O'chirish uchun vazifani tanlang!")

def save_tasks():
    with open("tasks.txt", "w", encoding="utf-8") as f:
        for task in tasks:
            f.write(task + "\n")
    messagebox.showinfo("Ma'lumot", "Vazifalar saqlandi!")

def load_tasks():
    try:
        with open("tasks.txt", "r", encoding="utf-8") as f:
            loaded_tasks = f.readlines()
            for task in loaded_tasks:
                tasks.append(task.strip())
        update_listbox()
    except FileNotFoundError:
        pass

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

root = tk.Tk()
root.title("To-Do List Manager")
root.geometry("400x400")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

add_button = tk.Button(root, text="Vazifa qo'shish", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Vazifa o'chirish", command=delete_task)
delete_button.pack(pady=5)

save_button = tk.Button(root, text="Vazifalarni saqlash", command=save_tasks)
save_button.pack(pady=5)

listbox = tk.Listbox(root, width=50, height=15)
listbox.pack(pady=10)

load_tasks()

root.mainloop()
