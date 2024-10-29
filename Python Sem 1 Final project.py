import tkinter as tk
from math import *

# Create the main window
window = tk.Tk()
window.geometry("415x600")
window.config(background="black")

# Global variables
expression = ""
history = []

# Function to update the expression in the entry box
def button_click(item):
    global expression
    expression += str(item)
    entry.delete(0, tk.END)
    entry.insert(tk.END, expression)

# Function to evaluate the expression
def evaluate():
    global expression
    try:
        result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
        history.append(f"{expression} = {result}")
        expression = result
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
        expression = ""

# Function to clear the entry box
def clear():
    global expression
    expression = ""
    entry.delete(0, tk.END)

# Function to delete the last character
def delete():
    global expression
    expression = expression[:-1]
    entry.delete(0, tk.END)
    entry.insert(tk.END, expression)

# Function to display calculation history
def view_history():
    history_window = tk.Toplevel(window)
    history_window.title("Calculation History")
    history_window.geometry("300x400")
    history_window.config(background="lightgrey")

    history_label = tk.Label(history_window, text="Calculation History", font=("Arial", 14, "bold"), bg="lightgrey")
    history_label.pack(pady=10)

    history_text = tk.Text(history_window, font=("Arial", 12), bg="white", height=20, width=30)
    history_text.pack(padx=10, pady=10)
    for item in history:
        history_text.insert(tk.END, item + "\n")

    history_text.config(state="disabled")

# Scientific functions
def scientific_function(func):
    global expression
    try:
        expression = str(func(eval(expression)))
        entry.delete(0, tk.END)
        entry.insert(tk.END, expression)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
        expression = ""

# New functions for exponential and factorial
def exponential():
    global expression
    try:
        expression = str(exp(eval(expression)))
        entry.delete(0, tk.END)
        entry.insert(tk.END, expression)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
        expression = ""

def factorial_function():
    global expression
    try:
        expression = str(factorial(int(eval(expression))))
        entry.delete(0, tk.END)
        entry.insert(tk.END, expression)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
        expression = ""

# Show the calculator interface after the splash screen
def show_calculator():
    # Clear the splash screen
    for widget in window.winfo_children():
        widget.destroy()
    
    window.title("Scientific Calculator")
    window.config(background="cyan")
    
    # Entry box for input and result display
    global entry
    entry = tk.Entry(window, font=("Arial", 20), fg="black", bg="white", justify="right", bd=0, highlightbackground="darkgray", highlightcolor="black", highlightthickness=2)
    entry.grid(row=0, column=1, columnspan=4, sticky="nsew", padx=5, pady=(5, 10))

    # View History button to the left of the entry box
    history_button = tk.Button(window, text="History", font=("Arial", 12), command=view_history, bg="grey", fg="white")
    history_button.grid(row=0, column=0, padx=5, pady=(5, 10), sticky="nsew")

    # Button layout for numbers and basic operations
    button_list = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ]

    # Creating buttons for numbers and basic operations
    for (text, row, col) in button_list:
        if text == '=':
            button = tk.Button(window, text=text, font=("Arial", 18), command=evaluate)
        else:
            button = tk.Button(window, text=text, font=("Arial", 18), command=lambda t=text: button_click(t))
        button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

    # Scientific function buttons
    scientific_buttons = [
        ('sin', sin), ('cos', cos), ('tan', tan), ('log', log), ('√', sqrt)
    ]

    for i, (text, func) in enumerate(scientific_buttons):
        button = tk.Button(window, text=text, font=("Arial", 18), command=lambda f=func: scientific_function(f))
        button.grid(row=i+1, column=4, padx=5, pady=5, sticky="nsew")

    # Adding new buttons for exponential and factorial functions
    exp_button = tk.Button(window, text="exp", font=("Arial", 18), command=exponential)
    exp_button.grid(row=5, column=2, padx=5, pady=5, sticky="nsew")

    fact_button = tk.Button(window, text="fact", font=("Arial", 18), command=factorial_function)
    fact_button.grid(row=5, column=3, padx=5, pady=5, sticky="nsew")

    # Clear and delete buttons with red color
    clear_button = tk.Button(window, text="C", font=("Arial", 18), command=clear, bg="red", fg="white")
    clear_button.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")

    delete_button = tk.Button(window, text="Del", font=("Arial", 18), command=delete, bg="red", fg="white")
    delete_button.grid(row=5, column=1, padx=5, pady=5, sticky="nsew")

    # Configuring grid weights for resizing
    for i in range(6):
        window.grid_rowconfigure(i, weight=1)
        window.grid_columnconfigure(i, weight=1)

# Display splash screen details
def splash_screen():
    # Center frame with double-lined border effect
    outer_frame = tk.Frame(window, bg="white", bd=5)
    outer_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.9, relheight=0.28)
    
    inner_frame = tk.Frame(outer_frame, bg="black", bd=3, relief="solid")
    inner_frame.pack(fill="both", expand=True, padx=4, pady=4)
    
    # Splash screen details
    splash_text = [
        "Student Name: Kritika Sejwal",
        "UID: 24MCI10023",
        "Section/Group: 24MAM1-A",
        "Subject: Python Programming",
        "Project Title: Scientific Calculator"
    ]

    for text in splash_text:
        label = tk.Label(inner_frame, text=text, font=("Bookman Old Style", 13, "bold"), fg="black", bg="white")
        label.pack(pady=1)

# Display splash screen on start
splash_screen()

# Show calculator interface after 4 seconds
window.after(4000, show_calculator)

# Start the main loop
window.mainloop()
