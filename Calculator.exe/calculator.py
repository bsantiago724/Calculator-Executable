import tkinter as tk
from tkinter import ttk

GRAY = "#3D3D3D"
LGRAY = "#5A5A5A"
DGRAY = "#212121"
WHITE = "#EEEEEE"

# enter button fix

class Calculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x800")
        self.root.minsize(325, 500)
        self.root.title("Calculator")

        self.total_expression = ""
        self.current_expression = ""
        self.display_frame = self.create_display()

        self.total_label, self.label = self.create_display_labels()

        self.digits = {
            7: (2, 1), 8: (2, 2), 9: (2, 3),
            4: (3, 1), 5: (3, 2), 6: (3, 3),
            1: (4, 1), 2: (4, 2), 3: (4, 3),
            0: (5, 2), '.': (5, 3)
        }

        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}

        self.buttons_frame = self.create_buttons()

        self.buttons_frame.rowconfigure(0, weight=1)

        for x in range(1, 6):
            self.buttons_frame.rowconfigure(x, weight=1)
        for x in range(1, 5):
            self.buttons_frame.columnconfigure(x, weight=1)

        self.create_digits_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()
        self.keyboard()

        self.root.mainloop()

    def create_display(self):
        display = tk.Frame(self.root, height=300)
        display.pack(expand=True, fill="both")
        return display

    def create_buttons(self):
        buttons=tk.Frame(self.root, bg=DGRAY)
        buttons.pack(expand=True, fill="both")
        return buttons

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=DGRAY, fg=WHITE, padx=24, bd=0,
                               font=["Arial", 16])
        total_label.pack(expand=True, fill="both")

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=DGRAY, fg=WHITE, padx=24,  bd=0,
                         font=["Arial", 48, "bold"])
        label.pack(expand=True, fill="both")

        return total_label, label

    def create_digits_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit),
                                background=LGRAY, foreground=WHITE, font=("Arial", 24, "bold"), bd=0,
                                command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW, padx=1, pady=1)

    def create_operator_buttons(self):
        i = 1
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol,
                                background=GRAY, foreground=WHITE, font=("Arial", 20), bd=0,
                                command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW, padx=1, pady=1)
            i += 1

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", bg=GRAY, fg=WHITE,
                           font=("Arial", 20), bd=0,
                           command=self.clear)
        button.grid(row=0, column=1, columnspan=2, sticky=tk.NSEW, padx=1, pady=1)

    def create_backspace_button(self):
        button = tk.Button(self.buttons_frame, text="⌫", bg=GRAY, fg=WHITE,
                                 font=("Arial", 20), bd=0,
                                 command=self.backspace)
        button.grid(row=0, column=3, columnspan=2, sticky=tk.NSEW, padx=1, pady=1)

    def create_factorial_button(self):
        button = tk.Button(self.buttons_frame, text="x!", bg=GRAY, fg=WHITE,
                           font=("Arial", 20), bd=0,
                           command=self.factorial)
        button.grid(row=1, column=1, sticky=tk.NSEW, padx=1, pady=1)

    def create_square_button(self):
        button = tk.Button(self.buttons_frame, text="x\u00b2", bg=GRAY, fg=WHITE,
                           font=("Arial", 20), bd=0,
                           command=self.square)
        button.grid(row=1, column=2, sticky=tk.NSEW, padx=1, pady=1)

    def create_square_root_button(self):
        button = tk.Button(self.buttons_frame, text="\u221ax", bg=GRAY, fg=WHITE,
                           font=("Arial", 20), bd=0,
                           command=self.square_root)
        button.grid(row=1, column=3, sticky=tk.NSEW, padx=1, pady=1)

    def create_change_sign(self):
        button = tk.Button(self.buttons_frame, text="+/-",
                                background=LGRAY, foreground=WHITE, font=("Arial", 24), bd=0,
                                command=self.change_sign)
        button.grid(row=5, column=1, sticky=tk.NSEW, padx=1, pady=1)

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg=WHITE, fg=GRAY,
                           font=("Arial", 20), bd=0,
                           command=self.evaluate)
        button.grid(row=5, column=4, sticky=tk.NSEW, padx=1, pady=1)

    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
        self.create_square_button()
        self.create_square_root_button()
        self.create_change_sign()
        self.create_backspace_button()
        self.create_factorial_button()

    def add_to_expression(self, value):
        if self.current_expression.endswith(" = "):
            self.current_expression = ""

        if self.total_expression.endswith(" = "):
            self.current_expression = ""

        if self.current_expression == "Error":
            self.current_expression = ""

        if len(self.current_expression) < 11:
            self.current_expression += str(value)
            self.update_label()


    def append_operator(self, operator):
        if self.total_expression.endswith(" = "):
            self.total_expression = self.current_expression + operator
            self.current_expression = ""

        else:
            self.current_expression += operator
            self.total_expression += self.current_expression
            self.current_expression = ""

        self.update_total_label()
        self.update_label()

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()

    def backspace(self):
        if self.current_expression == "Error":
            self.clear()
        elif self.total_expression.endswith(" = "):
            self.current_expression = ""
        else:
            self.current_expression = self.current_expression[:-1]
        self.update_label()

    def factorial(self):
        try:
            self.total_expression = f"fact({self.current_expression})"
            n = int(eval(self.current_expression))
            if n < 0:
                raise ValueError("Factorial is undefined for negative numbers")
            result = 1
            for i in range(1, n + 1):
                result *= i
            self.current_expression = str(result)
            self.update_total_label()
            self.update_label()
        except Exception as e:
            self.current_expression = "Error"
            self.update_label()

    def square(self):
        self.total_expression = f"sqr({self.current_expression})"
        self.current_expression = str(eval(f"{self.current_expression}**2"))
        formatted_result = "{:.10g}".format(float(self.current_expression))
        self.current_expression = formatted_result
        self.update_total_label()
        self.update_label()

    def square_root(self):
        self.total_expression = f"\u221a({self.current_expression})"
        self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        formatted_result = "{:.10g}".format(float(self.current_expression))
        self.current_expression = formatted_result
        self.update_total_label()
        self.update_label()

    def change_sign(self):
        if self.current_expression == "":
            self.current_expression= "-"
        elif self.current_expression[0] == "-":
            self.current_expression = self.current_expression[1:]
            
        elif "." in self.current_expression:
            if self.current_expression.startswith("-"):
                self.current_expression = self.current_expression[1:]
            else:
                self.current_expression = "-" + self.current_expression
        else:
            if self.current_expression.startswith("-"):
                self.current_expression = str(-int(self.current_expression))
            else:
                self.current_expression = str(-int(self.current_expression))

        self.update_label()

    def evaluate(self):
        if self.total_expression.endswith(")"):
                return 
        
        if self.total_expression.endswith(" = "):

            operands = []
            operators = []
            current_operand = []
            for char in self.total_expression:
                if char.isdigit() or char == '.':
                    current_operand += char
                else:
                    if current_operand:
                        operands.append(current_operand)
                        current_operand = ''

                    operators.append(char)

            operands.append(current_operand)

            self.total_expression = f"{self.current_expression}{operators[0]}{operands[1]}"
            self.current_expression = str(eval(self.total_expression))
            self.total_expression += " = "
            self.update_total_label()
            self.update_label()
            return

        self.total_expression += f"{self.current_expression}"
        self.update_total_label()

        try:
            result = eval(self.total_expression)

            formatted_result = "{:.10g}".format(result)
            self.current_expression = formatted_result

            self.total_expression += " = "

        except Exception as e:
            self.total_expression += " = "
            self.current_expression = "Error"

        finally:
            self.update_total_label()
            self.update_label()

    def keyboard(self):
        self.root.bind("<Return>", lambda event: self.evaluate())
        self.root.bind("<BackSpace>", lambda event: self.backspace())
        for key in self.digits:
            self.root.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))

        for key in self.operations:
            self.root.bind(key, lambda event, operator=key: self.append_operator(operator))

    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_label.config(text=expression)

    def update_label(self):
        self.label.config(text=self.current_expression[:11])

if __name__ == "__main__":
    calc = Calculator()
