import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QWidget, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Infix to Postfix Converter")
        self.setGeometry(200, 200, 400, 200)

        self.init_ui()

    def init_ui(self):
        # Create the input label and field
        self.input_label = QLabel("Enter an infix expression:")
        self.input_field = QLineEdit()

        # Create the convert button
        self.convert_button = QPushButton("Convert")
        self.convert_button.clicked.connect(self.convert_expression)

        # Create the output label and field
        self.output_label = QLabel("Postfix expression:")
        self.output_field = QTextEdit()
        self.output_field.setReadOnly(True)

        # Create the evaluated value label and field
        self.eval_label = QLabel("Evaluated value:")
        self.eval_field = QLineEdit()
        self.eval_field.setReadOnly(True)

        # Create the main layout
        layout = QVBoxLayout()
        layout.addWidget(self.input_label)
        layout.addWidget(self.input_field)
        layout.addWidget(self.convert_button)
        layout.addWidget(self.output_label)
        layout.addWidget(self.output_field)
        layout.addWidget(self.eval_label)
        layout.addWidget(self.eval_field)

        # Create a central widget and set the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def convert_expression(self):
        # Get the infix expression from the input field
        infix_expr = self.input_field.text()

        if infix_expr:
            try:
                # Convert the infix expression to postfix
                postfix_expr = infix_to_postfix(infix_expr)
                self.output_field.setPlainText(postfix_expr)

                # Evaluate the postfix expression
                evaluated_value = evaluate_postfix(postfix_expr)
                self.eval_field.setText(str(evaluated_value))
            except Exception as e:
                # Display an error message box if there's an exception
                QMessageBox.critical(self, "Error", str(e))
        else:
            # Display a warning message if no infix expression is entered
            QMessageBox.warning(self, "Warning", "Please enter an infix expression.")

def infix_to_postfix(infix_expr):
    # Define the precedence of operators
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2, '^': 3, '>': 0, '<': 0, '>=': 0, '<=': 0, '!=': 0, '==': 0}
    postfix_expr = ""  # Initialize an empty string to store the postfix expression
    stack = []  # Initialize an empty stack to store operators

    i = 0
    while i < len(infix_expr):
        token = infix_expr[i]
        if token.isdigit():
            # If the token is a digit, it represents a number
            # Read the entire number and append it to the postfix expression
            number = ""
            while i < len(infix_expr) and infix_expr[i].isdigit():
                number += infix_expr[i]
                i += 1
            postfix_expr += number + " "
            continue
        elif token in precedence:
            if token == '>':
                op = token
                # Handle the special case of the ">=" operator
                if i + 1 < len(infix_expr) and infix_expr[i + 1] == '=':
                    op += '='
                    i += 1
            else:
                op = token

            # Pop operators from the stack and append them to the postfix expression
            # based on their precedence and associativity
            while stack and stack[-1] != '(' and precedence.get(op, 0) <= precedence.get(stack[-1], 0):
                postfix_expr += stack.pop() + " "
            stack.append(op)  # Push the current operator onto the stack
        elif token == '(':
            stack.append(token)  # Push opening parenthesis onto the stack
        elif token == ')':
            # Pop operators from the stack and append them to the postfix expression
            # until an opening parenthesis is encountered
            while stack and stack[-1] != '(':
                postfix_expr += stack.pop() + " "
            stack.pop()  # Discard the opening parenthesis

        i += 1

    # Pop any remaining operators from the stack and append them to the postfix expression
    while stack:
        postfix_expr += stack.pop() + " "

    return postfix_expr.strip()  # Remove leading/trailing whitespace and return the postfix expression

def evaluate_postfix(postfix_expr):
    stack = []
    for token in postfix_expr.split():
        if token.isdigit():
            # If the token is a number, convert it to an integer and push it onto the stack
            stack.append(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            # Evaluate the operator and perform the corresponding operation on the operands
            result = evaluate_operator(token, operand1, operand2)
            # Push the result back onto the stack
            stack.append(result)
    # The final result is at the top of the stack
    return stack.pop()

def evaluate_operator(operator, operand1, operand2):
    if operator == '+':
        # Addition operation
        return operand1 + operand2
    elif operator == '-':
        # Subtraction operation
        return operand1 - operand2
    elif operator == '*':
        # Multiplication operation
        return operand1 * operand2
    elif operator == '/':
        # Division operation
        return operand1 / operand2
    elif operator == '%':
        # Modulo operation
        return operand1 % operand2
    elif operator == '^':
        # Exponentiation operation
        return operand1 ** operand2
    elif operator == '>':
        # Greater than comparison
        return int(operand1 > operand2)
    elif operator == '<':
        # Less than comparison
        return int(operand1 < operand2)
    elif operator == '>=':
        # Greater than or equal to comparison
        return int(operand1 >= operand2)
    elif operator == '<=':
        # Less than or equal to comparison
        return int(operand1 <= operand2)
    elif operator == '!=':
        # Not equal to comparison
        return int(operand1 != operand2)
    elif operator == '==':
        # Equal to comparison
        return int(operand1 == operand2)
    else:
        # Raise an exception for an invalid operator
        raise ValueError("Invalid operator: " + operator)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())