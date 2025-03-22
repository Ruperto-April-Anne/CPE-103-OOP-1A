import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


#window
window = tk.Tk()
window.title('Account Registration System')
window.eval(f'tk::PlaceWindow {str(window)}')
window.resizable(False, False)
window_height = 580
window_width = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
window.iconbitmap("cute.ico")
window.configure(bg='#A1E3F9')


#Texts
tk.Label(window, text="Registration Form", font='Times_New_Roman 20 bold', bg='#A1E3F9', fg='#3674B5').place(x=130,y=10)
tk.Label(window, text="Personal Information", font='Arial 14 bold', bg='#A1E3F9', fg='#3674B5').place(x=20, y=60)
tk.Label(window, text="First Name", font='Arial 12 bold', bg='#A1E3F9', fg='#3674B5').place(x=10, y=85)
tk.Label(window, text="Last Name", font='Arial 12 bold', bg='#A1E3F9', fg='#3674B5').place(x=255, y=85)
tk.Label(window, text="Email", font='Arial 12 bold', bg='#A1E3F9', fg='#3674B5').place(x=10, y=140)
tk.Label(window, text="Contact Number", font='Arial 12 bold', bg='#A1E3F9', fg='#3674B5').place(x=10, y=200)
tk.Label(window, text="Account Information", font='Arial 14 bold', bg='#A1E3F9', fg='#3674B5').place(x=20, y=255)
tk.Label(window, text="Username", font='Arial 12 bold', bg='#A1E3F9', fg='#3674B5').place(x=205, y=280)
tk.Label(window, text="Password", font='Arial 12 bold', bg='#A1E3F9', fg='#3674B5').place(x=205, y=345)
tk.Label(window, text="Confirm Password", font='Arial 12 bold', bg='#A1E3F9', fg='#3674B5').place(x=175, y=415)


#ENTRIES
#First Name
entry1 = tk.Entry(window, width= 38)
entry1.place(x=10, y=110)

#Last Name
entry2 = tk.Entry(window, width= 38)
entry2.place(x=255, y=110)

#Email
entry3 = tk.Entry(window, width= 79)
entry3.place(x=10, y=165)

#Contact Number
def validate_input(new_value):
    return new_value.isdigit() and len(new_value) <= 11
vcmd = (window.register(validate_input), '%P')
entry4 = tk.Entry(window, validate='key', validatecommand=vcmd)
entry4.place(x=10, y=220)

#Username
entry5 = tk.Entry(window, width=79)
entry5.place(x=10, y=305)

#Password
entry6 = tk.Entry(window,  show="*", width=79)
entry6.place(x=10, y=370)

#Confirm Password
entry7 = tk.Entry(window,  show="*", width=79)
entry7.place(x=10, y=440)


# Functions
def submit():
    first_name = entry1.get()
    last_name = entry2.get()
    email = entry3.get()
    contact = entry4.get()
    username = entry5.get()
    password = entry6.get()
    confirm_password = entry7.get()

    if not (first_name and last_name and email and contact and username and password and confirm_password):
        showinfo("Error", "All fields must be filled!")
        return

    if password != confirm_password:
        showinfo("Error", "Passwords do not match!")
        return

    showinfo("Success", f"Registration Successful!\nWelcome, {first_name} {last_name}!")

def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    entry4.delete(0, tk.END)
    entry5.delete(0, tk.END)
    entry6.delete(0, tk.END)
    entry7.delete(0, tk.END)

# Buttons
submit_button = tk.Button(window, text="Submit", font='Arial 12 bold', command=submit, bg='#578FCA', fg="white")
submit_button.place(x=130, y=500)

clear_button = tk.Button(window, text="Clear", font='Arial 12 bold', command=clear, bg='#98D2C0', fg="white")
clear_button.place(x=300, y=500)

window.mainloop()