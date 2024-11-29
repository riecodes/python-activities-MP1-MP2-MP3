import tkinter as tk
from tkinter import messagebox

def infix_to_postfix(infix_expr):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2, '^': 3, '>': 0, '<': 0, '>=': 0, '<=': 0, '!=': 0, '==': 0}
    postfix_expr = ""
    stack = []

    i = 0
    while i < len(infix_expr):
        token = infix_expr[i]
        if token.isdigit():
            # Read the entire number
            number = ""
            while i < len(infix_expr) and infix_expr[i].isdigit():
                number += infix_expr[i]
                i += 1
            postfix_expr += number + " "
            continue
        elif token in precedence:
            if token == '>':
                op = token
                if i + 1 < len(infix_expr) and infix_expr[i + 1] == '=':
                    op += '='
                    i += 1
            else:
                op = token

            while stack and stack[-1] != '(' and precedence.get(op, 0) <= precedence.get(stack[-1], 0):
                postfix_expr += stack.pop() + " "
            stack.append(op)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                postfix_expr += stack.pop() + " "
            stack.pop()

        i += 1

    while stack:
        postfix_expr += stack.pop() + " "

    return postfix_expr.strip()

def evaluate_postfix(postfix_expr):
    stack = []
    operators = {'+', '-', '*', '/', '%', '^', '>', '<', '>=', '<=', '!=', '=='}

    for token in postfix_expr.split():
        if token.isdigit():
            stack.append(int(token))
        elif token in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = perform_operation(token, operand1, operand2)
            stack.append(result)

    return stack.pop()

def perform_operation(operator, operand1, operand2):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        return operand1 / operand2
    elif operator == '%':
        return operand1 % operand2
    elif operator == '^':
        return operand1 ** operand2
    elif operator == '>':
        return int(operand1 > operand2)
    elif operator == '<':
        return int(operand1 < operand2)
    elif operator == '>=':
        return int(operand1 >= operand2)
    elif operator == '<=':
        return int(operand1 <= operand2)
    elif operator == '!=':
        return int(operand1 != operand2)
    elif operator == '==':
        return int(operand1 == operand2)

def convert_expression():
    infix_expr = input_field.get()

    if infix_expr:
        try:
            postfix_expr = infix_to_postfix(infix_expr)

            output_field.config(state="normal")
            output_field.delete("1.0", tk.END)
            output_field.insert(tk.END, postfix_expr)
            output_field.config(state="disabled")

            evaluated_value = evaluate_postfix(postfix_expr)
            eval_field.config(state="normal")
            eval_field.delete(0, tk.END)
            eval_field.insert(tk.END, str(evaluated_value))
            eval_field.config(state="readonly")
        except ValueError:
            messagebox.showerror("Error", "Invalid infix expression.")
        except ZeroDivisionError:
            messagebox.showerror("Error", "Division by zero is not allowed.")
    else:
        messagebox.showwarning("Warning", "Please enter an infix expression.")

# Create the main window
window = tk.Tk()
window.title("Infix to Postfix Converter")

# Create the input label and field
input_label = tk.Label(window, text="Enter an infix expression:")
input_label.pack()
input_field = tk.Entry(window)
input_field.pack()

# Create the convert button
convert_button = tk.Button(window, text="Convert", command=convert_expression)
convert_button.pack()

# Create the output label and field
output_label = tk.Label(window, text="Postfix expression:")
output_label.pack()
output_field = tk.Text(window, state="disabled", height=3, width=30)
output_field.pack()

# Create the evaluated value label and field
eval_label = tk.Label(window, text="Evaluated value:")
eval_label.pack()
eval_field = tk.Entry(window, state="readonly")
eval_field.pack()

window.mainloop()