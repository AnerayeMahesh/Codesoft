import random
import string
import tkinter as tk

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_display_password():
    length = int(entry_length.get())
    password = generate_password(length)
    password_var.set(password)

root = tk.Tk()
root.title("Password Generator")
root.geometry('300x300')

label_length = tk.Label(root, text="Enter the desired length of password:")
label_length.pack()

entry_length = tk.Entry(root)
entry_length.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_and_display_password)
generate_button.pack()

password_var = tk.StringVar(root)
password_label = tk.Label(root, textvariable=password_var)
password_label.pack()

root.mainloop()
