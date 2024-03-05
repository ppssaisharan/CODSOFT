import tkinter as tk
from tkinter import messagebox
def add():
    perform_operation("+")
def subtract():
    perform_operation("-")
def multiply():
    perform_operation("*")
def divide():
    perform_operation("/")
def perform_operation(operation):
    num1 = float(entry1.get())
    num2 = float(entry2.get())

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            messagebox.showerror("Error", "Division by zero is not allowed")
            return
        else:
            result = num1 / num2

    result_label.config(text="Result: " + str(result))

root = tk.Tk()
root.title("Simple Calculator")
entry1 = tk.Entry(root)
entry1.pack()
entry2 = tk.Entry(root)
entry2.pack()
button_frame = tk.Frame(root)
button_frame.pack()
add_button = tk.Button(button_frame, text="+", command=add)
add_button.pack(side=tk.LEFT, padx=5)
subtract_button = tk.Button(button_frame, text="-", command=subtract)
subtract_button.pack(side=tk.LEFT, padx=5)
multiply_button = tk.Button(button_frame, text="*", command=multiply)
multiply_button.pack(side=tk.LEFT, padx=5)
divide_button = tk.Button(button_frame, text="/", command=divide)
divide_button.pack(side=tk.LEFT, padx=5)
result_label = tk.Label(root, text="Result: ")
result_label.pack()
root.mainloop()