import tkinter as tk
from PIL import Image, ImageTk
import sqlite3
import os
import re
from tkinter import ttk

# Database setup function
def setup_database():
    """Creates SQLite database for user authentication"""
    # Create database if it doesn't exist
    if not os.path.exists('learn_sync.db'):
        conn = sqlite3.connect('learn_sync.db')
        cursor = conn.cursor()

        # Create tables for students and instructors
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id TEXT PRIMARY KEY,
            full_name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS instructors (
            id TEXT PRIMARY KEY,
            full_name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')

        conn.commit()
        conn.close()
        print("Database created successfully")
    return True


# Student form opening function
def open_student_form():
    """Opens the student login/signup form"""
    open_role_form("STUDENT")


# Instructor form opening function
def open_instructor_form():
    """Opens the instructor login/signup form"""
    open_role_form("INSTRUCTOR")


# Main form handler function
def open_role_form(role):
    """Creates and manages the main form for student/instructor authentication"""
    root.destroy()  # Close the main window

    # Create new window for form
    form_window = tk.Tk()
    form_window.title(f"{role} Form - Learn Sync")
    form_window.state('zoomed')

    # Create main container
    main_container = tk.Frame(form_window)
    main_container.pack(fill=tk.BOTH, expand=True)

    # Create a new top-level window
    left_window = tk.Toplevel(form_window)
    left_window.attributes("-topmost", True)
    left_window.attributes("-alpha", 0.7)

    # Inside the top-level window, create a frame (left panel)
    left_panel = tk.Frame(left_window, width=250, bg="#a0a0a0")
    left_panel.pack(side=tk.LEFT, fill=tk.Y)
    left_panel.pack_propagate(False)

    # Header
    header_label = tk.Label(left_panel, text=f"{role} FORM", font=("Open Sans", 14, "bold"),
                            bg="#a0a0a0", fg="black", pady=10)
    header_label.pack(fill=tk.X, pady=10)

    # Navigation buttons
    login_btn = tk.Button(left_panel, text="Log In", font=("Open Sans", 12),
                          bg="white", fg="black", width=15, relief=tk.RAISED, pady=5,
                          command=lambda: show_login_form(content_frame, role))
    login_btn.pack(fill=tk.X,pady=10)

    signup_btn = tk.Button(left_panel, text="Sign up", font=("Open Sans", 12),
                           bg="white", fg="black", width=15, relief=tk.RAISED, pady=5,
                           command=lambda: show_signup_form(content_frame, role))
    signup_btn.pack(fill=tk.X,pady=10)

    # Back button with arrow
    back_frame = tk.Frame(left_panel, bg="#a0a0a0")
    back_frame.pack(pady=10)

    back_arrow = tk.Label(back_frame, text="←", font=("Open Sans", 14), bg="#a0a0a0")
    back_arrow.pack(side=tk.LEFT)

    back_btn = tk.Button(back_frame, text="Back", font=("Open Sans", 12),
                         bg="#a0a0a0", fg="black", bd=0,
                         command=lambda: back_to_main(form_window))
    back_btn.pack(side=tk.LEFT)

    # Instructions section
    instructions_label = tk.Label(left_panel, text="INSTRUCTIONS", font=("Open Sans", 12, "bold"),
                                  bg="#a0a0a0", fg="black", pady=10)
    instructions_label.pack(fill=tk.X, pady=(20, 5))

    # Customize instructions based on role
    id_type = "Student ID" if role == "STUDENT" else "Faculty ID"
    instructions_text = f"""1. Log in Learn Sync account 
using your {id_type} 
number as username
2. Please Sign up Learn Sync 
account if you do not have 
one and use your {id_type} 
number as username."""

    instructions = tk.Label(left_panel, text=instructions_text,
                            font=("Open Sans", 10), bg="#a0a0a0",
                            fg="black", justify=tk.LEFT)
    instructions.pack(fill=tk.X, padx=10)

    # Main content area with university logo background
    content_frame = tk.Frame(main_container)
    content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    # Load or create simulated background
    create_background(content_frame)

    # Default to showing login form initially
    show_login_form(content_frame, role)

    form_window.mainloop()


# Background creation function
def create_background(parent):
    """Creates the background for the form (logo or simulated)"""
    try:
        # Get full screen dimensions
        screen_width = parent.winfo_screenwidth()
        screen_height = parent.winfo_screenheight()

        # Open and resize the image to full screen
        bg_image = Image.open("BLURED LOGO COENGG.png")
        bg_image = bg_image.resize((screen_width, screen_height), Image.LANCZOS)
        bg_photo = ImageTk.PhotoImage(bg_image)

        # Create background label
        bg_label = tk.Label(parent, image=bg_photo)
        bg_label.image = bg_photo  # Keep a reference
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    except Exception as e:
        print(f"Error loading background image: {e}")
        # If image loading fails, create a simulated background with university logo
        create_simulated_background(parent)


# Login form display function
def show_login_form(content_frame, role):
    """Displays the login form for students/instructors"""
    # Clear any existing form
    clear_content_frame(content_frame)

    # Login form overlay
    login_frame = tk.Frame(content_frame, bg="#a0a0a0", bd=1, relief=tk.SOLID)
    login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=350, height=310)

    # Create form header with logo
    create_form_header(login_frame)


    # Role label (STUDENT or INSTRUCTOR)
    role_label = tk.Label(login_frame, text=role, font=("Open Sans", 14, "bold"),
                          bg="#a0a0a0", fg="black")
    role_label.pack(pady=7)


    # ID field (Username)
    id_entry = tk.Entry(login_frame, font=("Open Sans", 12), bd=1,width=30)
    id_entry.insert(0, "ID Number")
    id_entry.config(fg="gray")
    id_entry.pack(fill=tk.X,padx=20,pady=7)

    # Add focus events for placeholder behavior
    id_entry.bind("<FocusIn>", lambda e: on_entry_focus_in(e, id_entry, "ID Number"))
    id_entry.bind("<FocusOut>", lambda e: on_entry_focus_out(e, id_entry, "ID Number"))

    # Password field with eye icon
    password_frame, password_entry = create_password_field(login_frame)

    # Login button
    login_button = tk.Button(login_frame, text="Log in", bg="#a0a0a0", fg="black",
                             font=("Arial", 12), width=12, bd=1,
                             command=lambda: handle_login(id_entry.get(), password_entry.get(), role))
    login_button.pack(pady=15)


# Signup form display function
def show_signup_form(content_frame, role):
    """Displays the signup form for students/instructors"""
    # Clear any existing form
    clear_content_frame(content_frame)

    # Signup form overlay
    signup_frame = tk.Frame(content_frame, bg="#a0a0a0", bd=1, relief=tk.SOLID)
    signup_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=350, height=430)

    # Create form header with logo
    create_form_header(signup_frame)

    # Role label for signup
    role_label = tk.Label(signup_frame, text=f"{role} SIGN UP", font=("Open Sans", 12, "bold"),
                          bg="#a0a0a0", fg="black")
    role_label.pack(pady=15)

    # Full Name field
    fullname_entry = tk.Entry(signup_frame, font=("Open Sans", 12), bd=1)
    fullname_entry.insert(0, "Full Name")
    fullname_entry.config(fg="#a0a0a0")
    fullname_entry.pack(fill=tk.X, padx=20, pady=7)
    fullname_entry.bind("<FocusIn>", lambda e: on_entry_focus_in(e, fullname_entry, "Full Name"))
    fullname_entry.bind("<FocusOut>", lambda e: on_entry_focus_out(e, fullname_entry, "Full Name"))

    # ID Number field (Student ID or Faculty ID)
    id_label = "Student ID" if role == "STUDENT" else "Faculty ID"
    id_entry = tk.Entry(signup_frame, font=("Open Sans", 12), bd=1)
    id_entry.insert(0, id_label)
    id_entry.config(fg="#a0a0a0")
    id_entry.pack(fill=tk.X, padx=20, pady=7)
    id_entry.bind("<FocusIn>", lambda e: on_entry_focus_in(e, id_entry, id_label))
    id_entry.bind("<FocusOut>", lambda e: on_entry_focus_out(e, id_entry, id_label))

    # Email field
    email_entry = tk.Entry(signup_frame, font=("Open Sans", 12), bd=1)
    email_entry.insert(0, "Email")
    email_entry.config(fg="#a0a0a0")
    email_entry.pack(fill=tk.X, padx=20, pady=7)
    email_entry.bind("<FocusIn>", lambda e: on_entry_focus_in(e, email_entry, "Email"))
    email_entry.bind("<FocusOut>", lambda e: on_entry_focus_out(e, email_entry, "Email"))

    # Password field with eye icon
    password_frame, password_entry = create_password_field(signup_frame)

    # Confirm Password field with eye icon
    conf_password_frame = tk.Frame(signup_frame, bg="#a0a0a0")
    conf_password_frame.pack(fill=tk.X, padx=20, pady=7)

    conf_password_entry = tk.Entry(conf_password_frame, font=("Open Sans", 12), bd=1)
    conf_password_entry.insert(0, "Confirm Password")
    conf_password_entry.config(fg="#a0a0a0", show="")
    conf_password_entry.pack(fill=tk.X, side=tk.LEFT, expand=True)
    conf_password_entry.bind("<FocusIn>", lambda e: on_entry_focus_in(e, conf_password_entry, "Confirm Password"))
    conf_password_entry.bind("<FocusOut>", lambda e: on_entry_focus_out(e, conf_password_entry, "Confirm Password"))

    # Eye icon for confirm password visibility
    eye_conf_btn = tk.Label(conf_password_frame, font=("Open Sans", 12), text="👁", bg="#a0a0a0", cursor="hand2")
    eye_conf_btn.pack(side=tk.RIGHT, padx=7)
    eye_conf_btn.bind("<Button-1>", lambda e:
    conf_password_entry.config(show="" if conf_password_entry.cget("show") == "*" else "*")
    if conf_password_entry.get() != "Confirm Password" else None)

    # Sign up button
    signup_button = tk.Button(signup_frame, text="Sign up", bg="#a0a0a0", fg="black",
                              font=("Arial", 11), width=12, bd=1,
                              command=lambda: handle_signup(fullname_entry.get(), id_entry.get(),
                                                            email_entry.get(), password_entry.get(),
                                                            conf_password_entry.get(), role))
    signup_button.pack(pady=15)


# Password field creator function
def create_password_field(parent):
    """Creates a password field with toggle visibility button"""
    password_frame = tk.Frame(parent, bg="#a0a0a0")
    password_frame.pack(fill=tk.X, padx=20, pady=7)

    password_entry = tk.Entry(password_frame, font=("Open Sans", 12), bd=1)
    password_entry.insert(0, "Password")
    password_entry.config(fg="#a0a0a0", show="")
    password_entry.pack(fill=tk.X, side=tk.LEFT, expand=True)

    # Add focus events for placeholder behavior
    password_entry.bind("<FocusIn>", lambda e: on_entry_focus_in(e, password_entry, "Password"))
    password_entry.bind("<FocusOut>", lambda e: on_entry_focus_out(e, password_entry, "Password"))

    # Eye icon for password visibility
    eye_btn = tk.Label(password_frame, font=("Open Sans", 12),text="👁", bg="#a0a0a0", cursor="hand2")
    eye_btn.pack(side=tk.RIGHT, padx=7)
    eye_btn.bind("<Button-1>", lambda e:
    password_entry.config(show="" if password_entry.cget("show") == "*" else "*")
    if password_entry.get() != "Password" else None)

    return password_frame, password_entry


# Form header creator function
def create_form_header(parent):
    """Creates the Learn Sync logo header for forms"""
    try:
        logo = Image.open("LS.png")
        logo = logo.resize((60, 80))
        logo_photo = ImageTk.PhotoImage(logo)

        container = tk.Frame(parent)
        logo_label = tk.Label(container, image=logo_photo, bg="#a0a0a0")
        logo_label.image = logo_photo
        logo_label.pack(fill=tk.X)

        # Learn Sync text next to logo
        sync_label = tk.Label(container, text="Learn Sync", font=("Open Sans", 14, "bold"),
                              bg="#a0a0a0", fg="black")
        sync_label.pack()
        container.pack(pady=5)


    except Exception as e:
        print(f"Error loading logo: {e}")
        # If logo loading fails, create a text-based header
        header_frame = tk.Frame(parent, bg="#a0a0a0")
        header_frame.pack(fill=tk.X, pady=5)

        logo_placeholder = tk.Frame(header_frame, width=30, height=30, bg="#a0a0a0")
        logo_placeholder.pack(side=tk.LEFT, padx=5)

        sync_label = tk.Label(header_frame, text="Learn Sync", font=("Open Sans", 12, "bold"),
                              bg="#a0a0a0")
        sync_label.pack(side=tk.LEFT, padx=5)


# Form clearing function
def clear_content_frame(content_frame):
    """Clears any existing forms but keeps the background"""
    for widget in content_frame.winfo_children():
        if isinstance(widget, tk.Frame) and widget.winfo_class() == "Frame":
            widget.destroy()


# Login handler function
def handle_login(id_num, password, role):
    """Handles login authentication against database"""
    # Validate inputs
    if id_num in ["", "ID Number"] or password in ["", "Password"]:
        tk.messagebox.showerror("Login Error", "Please enter ID and password")
        return

    try:
        # Connect to database
        conn = sqlite3.connect('learn_sync.db')
        cursor = conn.cursor()

        # Select the appropriate table based on role
        table = "students" if role == "STUDENT" else "instructors"

        # Check credentials
        cursor.execute(f"SELECT id, full_name FROM {table} WHERE id = ? AND password = ?",
                       (id_num, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            tk.messagebox.showinfo("Login Success", f"Welcome back, {user[1]}!")
            # Here you would redirect to the main application
        else:
            tk.messagebox.showerror("Login Failed", "Invalid ID or password")

    except sqlite3.Error as e:
        tk.messagebox.showerror("Database Error", f"Error accessing database: {e}")


# Signup handler function
def handle_signup(fullname, id_num, email, password, conf_password, role):
    """Handles new user registration in database"""
    # Validate inputs
    if fullname in ["", "Full Name"] or id_num in ["", "Student ID", "Faculty ID"] or \
            email in ["", "Email"] or password in ["", "Password"] or conf_password in ["", "Confirm Password"]:
        tk.messagebox.showerror("Signup Error", "Please fill in all fields")
        return

    if password != conf_password:
        tk.messagebox.showerror("Signup Error", "Passwords do not match")
        return

    # Validate email format
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        tk.messagebox.showerror("Signup Error", "Please enter a valid email address")
        return

    try:
        # Connect to database
        conn = sqlite3.connect('learn_sync.db')
        cursor = conn.cursor()

        # Select the appropriate table based on role
        table = "students" if role == "STUDENT" else "instructors"

        # Check if ID already exists
        cursor.execute(f"SELECT id FROM {table} WHERE id = ?", (id_num,))
        if cursor.fetchone():
            tk.messagebox.showerror("Signup Error", f"This {id_num} is already registered")
            conn.close()
            return

        # Check if email already exists
        cursor.execute(f"SELECT email FROM {table} WHERE email = ?", (email,))
        if cursor.fetchone():
            tk.messagebox.showerror("Signup Error", "This email is already registered")
            conn.close()
            return

        # Insert new user
        cursor.execute(f"INSERT INTO {table} (id, full_name, email, password) VALUES (?, ?, ?, ?)",
                       (id_num, fullname, email, password))
        conn.commit()
        conn.close()

        tk.messagebox.showinfo("Signup Success",
                               f"{role} account created successfully!\nID: {id_num}\nName: {fullname}")

    except sqlite3.Error as e:
        tk.messagebox.showerror("Database Error", f"Error creating account: {e}")


# Back to main function
def back_to_main(current_window):
    """Returns to the main window from forms"""
    current_window.destroy()
    initialize_main_window()


# Entry field focus handling functions
def on_entry_focus_in(event, entry, placeholder):
    """Handles entry field focus-in event for placeholders"""
    if entry.get() == placeholder:
        entry.delete(0, tk.END)
        entry.config(fg="black")
        if placeholder in ["Password", "Confirm Password"]:
            entry.config(show="*")


def on_entry_focus_out(event, entry, placeholder):
    """Handles entry field focus-out event for placeholders"""
    if entry.get() == "":
        entry.insert(0, placeholder)
        entry.config(fg="gray")
        if placeholder in ["Password", "Confirm Password"]:
            entry.config(show="")


# Simulated background creator function
def create_simulated_background(parent):
    """Creates a simulated university logo background when image isn't available"""
    # Create a canvas for the background
    bg_canvas = tk.Canvas(parent, highlightthickness=0)
    bg_canvas.pack(fill=tk.BOTH, expand=True)

    # Get the width and height of the frame
    width = parent.winfo_width() if parent.winfo_width() > 1 else 800
    height = parent.winfo_height() if parent.winfo_height() > 1 else 600

    # Create a circular logo background
    bg_canvas.create_oval((width // 2) - 200, (height // 2) - 200, (width // 2) + 200, (height // 2) + 200,
                          outline="#86b049", width=20, fill="#e8c5a8")

    # Create gear icons for engineering college
    bg_canvas.create_oval(width // 2 - 30, height // 2 - 30, width // 2 + 30, height // 2 + 30, outline="#666666",
                          width=3)
    bg_canvas.create_oval(width // 2 + 50, height // 2 - 10, width // 2 + 90, height // 2 + 30, outline="#666666",
                          width=3)

    # Add text for university name around the circle
    bg_canvas.create_text(width // 2, height // 2 - 150, text="COLLEGE OF ENGINEERING",
                          font=("Arial", 14, "bold"), fill="#86b049")
    bg_canvas.create_text(width // 2, height // 2 + 150, text="UNIVERSITY OF CALOOCAN CITY",
                          font=("Arial", 14, "bold"), fill="#86b049")


# Main window initializer function
def initialize_main_window():
    """Initializes the main application window with logo and buttons"""
    global root
    # Initialize the main window
    root = tk.Tk()
    root.title("Learning Management System")
    root.state('zoomed')  # Make the window full screen
    root.configure(bg="white")

    # Create a frame to center the images
    image_frame = tk.Frame(root, bg="white")
    image_frame.pack(pady=60)

    # Load and display images
    photo1 = load_image("UCC.png", (140, 130))
    photo2 = load_image("COE.png", (160, 170))
    photo3 = load_image("LS.png", (200, 215))

    if photo1:
        image_label1 = tk.Label(image_frame, image=photo1, bg="white")
        image_label1.image = photo1  # Keep reference
        image_label1.pack(side=tk.LEFT, padx=20)

    if photo2:
        image_label2 = tk.Label(image_frame, image=photo2, bg="white")
        image_label2.image = photo2  # Keep reference
        image_label2.pack(side=tk.LEFT, padx=10)

    if photo3:
        image_label3 = tk.Label(image_frame, image=photo3, bg="white")
        image_label3.image = photo3  # Keep reference
        image_label3.pack(side=tk.LEFT, padx=10)

    # University and College Name
    label1 = tk.Label(root, text="UNIVERSITY OF CALOOCAN CITY", font=("Open Sans", 50), bg="white")
    label1.pack()
    label2 = tk.Label(root, text="COLLEGE OF ENGINEERING", font=("Open Sans", 20), bg="white")
    label2.pack(pady=20)

    # Buttons for Student and Instructor
    frame = tk.Frame(root, bg="white")
    frame.pack(pady=20)

    student_button = tk.Button(frame, text="STUDENT", font=("Poppins", 14, "bold"), bg="gray", fg="black",
                               width=20, height=2, command=open_student_form)
    student_button.pack(side=tk.LEFT, padx=70, pady=20)

    instructor_button = tk.Button(frame, text="INSTRUCTOR", font=("Poppins", 14, "bold"), bg="gray", fg="black",
                                  width=20, height=2, command=open_instructor_form)
    instructor_button.pack(side=tk.LEFT, padx=70, pady=20)


# Image loader function
def load_image(image_path, size):
    """Safely loads and resizes images for the UI"""
    try:
        img = Image.open(image_path)
        img = img.resize(size)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Error loading image {image_path}: {e}")
        return None


# Start the application
if __name__ == "__main__":
    # Import messagebox for notifications
    from tkinter import messagebox

    # Setup database before launching application
    setup_database()

    # Initialize and run the application
    initialize_main_window()
    root.mainloop()