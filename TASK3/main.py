import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length, complexity):
    characters = string.ascii_letters + string.digits
    if complexity == "high":
        characters += string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password_button():
    length = int(length_entry.get())
    complexity = complexity_var.get()

    password = generate_password(length, complexity)
    result.config(text=f"Your password is: {password}")


window = tk.Tk()
window.title("Password Generator")
window.config(bg="white")

heading = tk.Label(window, text="Password Generator", font=("Arial", 20, "bold"),bg="black",fg="white")
heading.grid(pady=10, column=1, columnspan=10)
    
length = tk.Label(window, text="Password Length:", font=("Arial", 15),bg="white",fg="black")
length.grid(row=2, column=1, padx=10, pady=15)

length_entry = tk.Entry(window, width=30)
length_entry.grid(row=2, column=2, padx=10, pady=15)

complexity = tk.Label(window, text="Level:", font=(" Arial", 15),bg="white",fg="black")
complexity.grid(row=3, column=1, padx=10, pady=15)

complexity_var = tk.StringVar()
complexity_var.set("low")

radio_low = tk.Radiobutton(window, text="Low", variable=complexity_var, value="low",bg="gray91")
radio_low.grid(row=3, column=2, padx=10, pady=15, sticky="w")

radio_high = tk.Radiobutton(window, text="High", variable=complexity_var, value="high",bg="gray91")
radio_high.grid(row=4, column=2, padx=10, pady=15, sticky="w")

generate_password1 = tk.Button(window, text="Generate Password", command=generate_password_button, font=("Arial", 15), bg="white" )
generate_password1.grid(row=5, column=1, columnspan=19, padx=10, pady=10)

result = tk.Label(window, text="", wraplength=400, bg="white", font=("Helvetica", 12))
result.grid(row=6, column=1, columnspan=2, padx=10, pady=15)

window.mainloop()
