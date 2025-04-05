import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


# Window
class MyWindow:
    def __init__(self, window):
        self.frame = tk.Frame(window, bd=10,bg='#AFDDFF', relief="flat")
        self.frame.pack(padx=10, pady=10)

        self.display = tk.Entry(self.frame, width=19, font=("Arial", 25), bd=20,bg= "#BDDDE4", justify="right")
        self.display.grid(row=0, column=0, pady=5, padx=3, columnspan=4)

        self.current_expression = ""

        # Button layout
        buttons = [
            ("C", 1, 0, 4),
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("/", 2, 3),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("*", 3, 3),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("-", 4, 3),
            ("0", 5, 0, 2), (".", 5, 2, 1), ("+", 5, 3),
            ("=", 6, 0, 4)
        ]

        # Create and place buttons
        for (text, row, col, *span) in buttons:
            span_value = span[0] if span else 1
            button = tk.Button(self.frame, text=text, width=10, height=2, bd=2, font=("Arial", 15), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, columnspan=span_value, sticky="nsew", pady=3)


        for i in range(7):
            self.frame.grid_rowconfigure(i, weight=1)

        for i in range(4):
            self.frame.grid_columnconfigure(i, weight=1)

    def on_button_click(self, text):
        if text == "C":
            self.current_expression = ""
        elif text == "=":
            try:
                self.current_expression = str(eval(self.current_expression))
            except Exception:
                self.current_expression = "Error"
        else:
            self.current_expression += text
        self.update_display()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.current_expression)



window = tk.Tk()
mywin = MyWindow(window)
window.title('Calculator')
window.resizable(False, False)

window_height = 500
window_width = 400
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_cordinate = int((screen_width / 2) - (window_width / 2))
y_cordinate = int((screen_height / 2) - (window_height / 2))
window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

window.iconbitmap('calculator.ico')
window.configure(bg='#AFDDFF')

window.mainloop()
