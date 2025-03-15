#TUI Implementation
# Simple TUI Calculator

#GUI Conversion of the Calculator:
import tkinter as tk
from tkinter import messagebox

# Functions for calculations
history = []

def add():
    calculate(lambda a, b: a + b, "+")

def subtract():
    calculate(lambda a, b: a - b, "-")

def multiply():
    calculate(lambda a, b: a * b, "*")

def divide():
    calculate(lambda a, b: a / b if b != 0 else "Error! Division by zero.", "/")

def square_root():
    try:
        num = float(entry1.get())
        result_value = math.sqrt(num) if num >= 0 else "Error! Negative root"
        result.set(result_value)
        history.append(f"√{num} = {result_value}")
        update_history()
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

def power_2():
    try:
        num = float(entry1.get())
        result_value = num ** 2
        result.set(result_value)
        history.append(f"{num}² = {result_value}")
        update_history()
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

def power_3():
    try:
        num = float(entry1.get())
        result_value = num ** 3
        result.set(result_value)
        history.append(f"{num}³ = {result_value}")
        update_history()
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

def sin_func():
    try:
        num = float(entry1.get())
        result_value = math.sin(math.radians(num))  # Convert degrees to radians
        result.set(result_value)
        history.append(f"sin({num}) = {result_value}")
        update_history()
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

def cos_func():
    try:
        num = float(entry1.get())
        result_value = math.cos(math.radians(num))
        result.set(result_value)
        history.append(f"cos({num}) = {result_value}")
        update_history()
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

def tan_func():
    try:
        num = float(entry1.get())
        if num % 90 == 0 and (num // 90) % 2 != 0:  # Avoid undefined tan(90°), tan(270°)...
            result_value = "Error! Undefined"
        else:
            result_value = math.tan(math.radians(num))
        result.set(result_value)
        history.append(f"tan({num}) = {result_value}")
        update_history()
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

def calculate(operation, symbol):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result_value = operation(num1, num2)
        result.set(result_value)
        history.append(f"{num1} {symbol} {num2} = {result_value}")
        update_history()
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values.")

def update_history():
    history_listbox.delete(0, tk.END)
    for item in history[-5:]:  # Show last 5 calculations
        history_listbox.insert(tk.END, item)

def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result.set("")

def main():
    print("Simple Calculator")
    print("Options:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. History")

    choice = input("Select operation (1/2/3/4/5): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid input.")

if __name__ == "_main_":
    main()

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("315x350")


# Create StringVar to hold the result
result = tk.StringVar()

# Layout
tk.Label(root, text="Enter first number:", font='Times_New_Roman 10 bold').grid(row=1, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=1, column=1)

tk.Label(root, text="Enter second number:", font='Times_New_Roman 10 bold').grid(row=2, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=2, column=1)

tk.Label(root, text="OPERATION:", font='Times_New_Roman 9 underline').grid(row=3, column=0)

# Buttons for operations
tk.Button(root, text="Add", command=add).grid(row=4, column=0)
tk.Button(root, text="Subtract", command=subtract).grid(row=4, column=1)
tk.Button(root, text="Multiply", command=multiply).grid(row=5, column=0)
tk.Button(root, text="Divide", command=divide).grid(row=5, column=1)

# Buttons for Advanced Operations
tk.Button(root, text="√ (Square Root)", command=square_root).grid(row=6, column=0)
tk.Button(root, text="x² (Square)", command=power_2).grid(row=6, column=1)
tk.Button(root, text="x³ (Cube)", command=power_3).grid(row=7, column=0)

# Trigonometric Functions
tk.Button(root, text="sin", command=sin_func).grid(row=7, column=1)
tk.Button(root, text="cos", command=cos_func).grid(row=8, column=0)
tk.Button(root, text="tan", command=tan_func).grid(row=8, column=1)

# Clear button
tk.Button(root, text="Clear", command=clear, bg="red", fg="white").grid(row=0, column=3)

# Result Label
tk.Label(root, text="Result:", font='Times_New_Roman 10 bold').grid(row=10, column=0)
result_label = tk.Label(root, textvariable=result)
result_label.grid(row=10, column=1)

# History Section
tk.Label(root, text="History:", font='Times_New_Roman 10 bold').grid(row=12, column=0)
history_listbox = tk.Listbox(root, height=5, bg='#a3daa9')
history_listbox.grid(row=12, column=1)

# Start the main loop
root.mainloop()
