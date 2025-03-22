import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Creating tkinter window and set dimensions
window = tk.Tk()
window.title('Combobox')
window.geometry('500x250')

def choice(event):
    month = event.widget.get()
    print("Your birth month", month)

#Set Label
ttk.Label(window, text="Select the month of your birth :", font=("Times New Roman", 12)).grid(column=0, row=5, padx=5, pady=25)

# Create Combobox
n = tk.StringVar()
month = ttk.Combobox(window, width=27, textvariable=n)

# Adding combobox drop down list
month['value'] = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

#label text for title
ttk.Label(window, text="Choose your birth month", background='light yellow', foreground='black', font=("Times New Roman", 15)).grid(row=0, column=1)
month.grid(column=1, row=5)
month.current()

def choice(event):
    showinfo(title="Selection", message=f"You selected {n.get()}.")

month.bind("<<ComboboxSelected>>", choice)
window.mainloop()