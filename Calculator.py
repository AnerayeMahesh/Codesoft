import tkinter as tk

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def calculate():
    operation = choice_var.get()
    num1 = float(entry1.get())
    num2 = float(entry2.get())

    if operation == 'Add':
        result_var.set(add(num1, num2))
    elif operation == 'Subtract':
        result_var.set(subtract(num1, num2))
    elif operation == 'Multiply':
        result_var.set(multiply(num1, num2))
    elif operation == 'Divide':
        result_var.set(divide(num1, num2))

root = tk.Tk()
root.title("Calculator")
root.geometry("300x200")

choice_var = tk.StringVar(root)
choice_var.set('Add')

label1 = tk.Label(root, text="Enter first number:")
label1.grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

label2 = tk.Label(root, text="Enter second number:")
label2.grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

label3 = tk.Label(root, text="Select operation:")
label3.grid(row=2, column=0)
choices = ['Add', 'Subtract', 'Multiply', 'Divide']
dropdown = tk.OptionMenu(root, choice_var, *choices)
dropdown.grid(row=2, column=1)

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2)

result_var = tk.StringVar(root)
result_label = tk.Label(root, textvariable=result_var)
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()
