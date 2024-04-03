import tkinter as tk

bg_color = "#3D3D3D"  # dark gray
bg_light_color = "#5A5A5A"  # light gray
display_color = "#212121"  # darker gray
text_color = "#EEEEEE"
equal_button_color = "#EEEEEE"  # whiteish

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("500x800")
        self.window.resizable(0, 0)
        self.window.title("Calculator")

        self.total = ""
        self.current_num = ""
        self.display_frame = self.create_display()

        self.total_label, self.label = self.create_display_labels()

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }

        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}

        self.buttons_frame = self.create_buttons()

        self.buttons_frame.rowconfigure(0, weight=1)

        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)

        self.create_digits_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()
        self.keyboard()

        self.window.mainloop()

    def keyboard(self):
        self.window.bind("<Return>", lambda event: self.evaluate())
        for key in self.digits:
            self.window.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))

        for key in self.operations:
            self.window.bind(key, lambda event, operator=key: self.append_operator(operator))

    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
        self.create_square_button()
        self.create_square_root_button()

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total, anchor=tk.E, bg=display_color, fg=text_color, padx=24,
                               font=["Arial", 16])
        total_label.pack(expand=True, fill="both")

        label = tk.Label(self.display_frame, text=self.current_num, anchor=tk.E, bg=display_color, fg=text_color, padx=24,
                         font=["Arial", 48, "bold"])
        label.pack(expand=True, fill="both")

        return total_label, label

    def create_display(self):
        display = tk.Frame(self.window, height=300, bg="#424242")
        display.pack(expand=True, fill="both")
        return display

    def add_to_expression(self, value):
        self.current_num += str(value)
        self.update_label()

    def create_digits_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=bg_light_color, fg=text_color,
                               font=["Arial", 24, "bold"], borderwidth=0,
                               command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def append_operator(self, operator):
        self.current_num += operator
        self.total += self.current_num
        self.current_num = ""
        self.update_total_label()
        self.update_label()

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=bg_color, fg=text_color, font=["Arial", 20],
                               borderwidth=0,
                               command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", bg=bg_color, fg=text_color, font=["Arial", 20], borderwidth=0,
                           command=self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def create_square_button(self):
        button = tk.Button(self.buttons_frame, text="x\u00b2", bg=bg_color, fg=text_color, font=["Arial", 20],
                           borderwidth=0,
                           command=self.square)
        button.grid(row=0, column=2, sticky=tk.NSEW)

    def create_square_root_button(self):
        button = tk.Button(self.buttons_frame, text="\u221ax", bg=bg_color, fg=text_color, font=["Arial", 20],
                           borderwidth=0,
                           command=self.square_root)
        button.grid(row=0, column=3, sticky=tk.NSEW)

    def clear(self):
        self.current_num = ""
        self.total = ""
        self.update_label()
        self.update_total_label()

    def square(self):
        self.current_num = str(eval(f"{self.current_num}**2"))
        self.update_label()

    def square_root(self):
        self.current_num = str(eval(f"{self.current_num}**0.5"))
        self.update_label()

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg=equal_button_color, fg=bg_color, font=["Arial", 20], borderwidth=0,
                           command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    def evaluate(self):
        self.total += self.current_num
        self.update_total_label()

        try:
            self.current_num = str(eval(self.total))
            self.total = ""

        except Exception as e:
            self.current_num = "Error"

        finally:
            self.update_label()

    def create_buttons(self):
        buttons = tk.Frame(self.window)
        buttons.pack(expand=True, fill="both")
        return buttons

    def update_total_label(self):
        expression = self.total
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_label.config(text=expression)

    def update_label(self):
        self.label.config(text=self.current_num[:11])


if __name__ == "__main__":
    Calculator()
