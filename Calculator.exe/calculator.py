import tkinter as tk

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("500x800")
        self.window.resizable(0,0)
        self.window.title("Calculator")
    
        self.total = "0"
        self.current_num = "0"
        self.display_frame = self.create_display()

        self.total_label, self.label = self.create_display_labels()

        self.digits = {
            7: (1, 1), 8: (1, 2), 9:(1, 3),
            4: (2, 1), 5: (2, 2), 6:(2, 3),
            1: (3, 1), 2: (3, 2), 3:(3, 3),
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

    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total, anchor=tk.E, bg="#F5F5F5", fg="#25265E", padx=24, font = ["Arial", 16])
        total_label.pack(expand = True, fill = "both")

        label = tk.Label(self.display_frame, text=self.current_num, anchor=tk.E, bg="#F5F5F5", fg="#25265E", padx=24, font = ["Arial", 40, "bold"])
        label.pack(expand = True, fill = "both")

        return total_label, label

    def create_display(self):
        display = tk.Frame(self.window, height=300, bg="#F5F5F5")
        display.pack(expand = True, fill = "both")
        return display
    
    def create_digits_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg="#FFFFFF", fg="#25265E", font = ["Arial", 24, "bold"], borderwidth = 0)
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text = symbol, bg = "#F8FAFF", fg="#25265E", font = ["Arial", 20], borderwidth = 0)
            button.grid(row = i, column = 4, sticky = tk.NSEW)
            i += 1

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", bg="#F8FAFF", fg="#25265E", font=["Arial", 20], borderwidth=0)
        button.grid(row=0, column=1, columnspan=3, sticky=tk.NSEW)

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg="#CCEDFF", fg="#25265E", font=["Arial", 20], borderwidth=0)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    def create_buttons(self):
        buttons = tk.Frame(self.window)
        buttons.pack(expand = True, fill = "both")
        return buttons

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()