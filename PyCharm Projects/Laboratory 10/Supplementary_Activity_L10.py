import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Create window
window = tk.Tk()
window.title('Combobox')
window.eval(f'tk::PlaceWindow {str(window)}')
window.resizable(False, False)

window_height = 280
window_width = 420
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
window.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

# Title
tk.Label(window, text="Choose Your Birthdate", font='Arial 15 bold').place(x=100, y=10)

# Variables (Initially Empty)
month_var = tk.StringVar(value="")
day_var = tk.StringVar(value="")
year_var = tk.StringVar(value="")

# Month Combobox
ttk.Label(window, text="Select the month of your birth:", font=("Times New Roman", 12)).place(x=15, y=50)
month = ttk.Combobox(window, width=27, textvariable=month_var, state="readonly")
month['values'] = ('January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December')
month.place(x=210, y=50)

# Day Combobox
ttk.Label(window, text="Select the day of your birth:", font=("Times New Roman", 12)).place(x=15, y=90)
day = ttk.Combobox(window, width=27, textvariable=day_var, state="readonly")
day['values'] = tuple(range(1, 32))
day.place(x=210, y=90)

# Year Combobox
ttk.Label(window, text="Select your birth year:", font=("Times New Roman", 12)).place(x=15, y=130)
year = ttk.Combobox(window, width=27, textvariable=year_var, state="readonly")
year['values'] = tuple(range(1980, 2026))
year.place(x=210, y=130)

# Function to show info only if all fields are selected
def choice(event):
    if month_var.get() and day_var.get() and year_var.get():
        showinfo(title="Selection", message=f"You selected {month_var.get()} {day_var.get()}, {year_var.get()}.")


month.bind("<<ComboboxSelected>>", choice)
day.bind("<<ComboboxSelected>>", choice)
year.bind("<<ComboboxSelected>>", choice)

# Run application
window.mainloop()
