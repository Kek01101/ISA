# 13/9/2020, Blue, Nicolas Keck, This program takes a number and then splits it into it's respective place values
# Expansion: Added the option to show place values in scientific notation as well, this extra mode also allows for
# floats.
import tkinter as tk
from tkinter import messagebox


# Help, I am addicted to making UI modules, I can' stop
# This is the only page this program really required
class HomePage(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("400x200")
        self.configure(bg="white")
        self.title("Mathtastic™ Premium-Deluxe™ Math™ Assistant™")
        tk.Label(self, text="Expansion Assistant™", font=(None, 30), bg="white").grid(row=0, column=0, columnspan=5)
        self.placevalue = tk.Label(self, text="Place Value Mode", font=(None, 15), bg="white")
        self.placevalue.grid(row=1, column=0, columnspan=2)
        self.notation = tk.Button(self, text="Scientific Notation Mode", font=(None, 15), command=self.switch,
                                  bg="white")
        self.notation.grid(row=1, column=3, columnspan=2)
        tk.Label(self, text="Input number:", font=(None, 15), bg="white").grid(row=2, column=0, columnspan=5)
        self.numEntry = tk.Entry(self, bg="white")
        self.numEntry.insert(0, "")
        self.numEntry.grid(row=3, column=0, columnspan=5)
        tk.Label(self, text="", font=(None, 15), bg="white").grid(row=4, column=0)
        tk.Button(self, text="Quit", font=(None, 10), bg="white", command=self.quit).grid(row=5, column=0)
        tk.Button(self, text="Calculate", font=(None, 10), bg="white", command=self.calculate).grid(row=5, column=4)

        # The variable required for the switching function
        self.notationOff = True

    def calculate(self):
        # Calculates and outputs an answer based upon the inputted information, can do so in both place value and
        # scientific notation modes.
        entry = self.numEntry.get()
        try:
            entry = float(entry)
        except ValueError:
            tk.messagebox.showerror("Error", "Please input a valid number")
        if entry <= 0:
            tk.messagebox.showerror("Error", "Please input a positive number")
        elif self.notationOff and not entry.is_integer():
            tk.messagebox.showerror("Error", "Place value mode does not support decimals")
        elif isinstance(entry, float):
            output = "Thank you for using Mathtastic™ Expansion Assistant™\n" \
                     "-------------\n" \
                     f"Number: {entry}\n" \
                     f"-------------\n"
            if self.notationOff:
                entry = str(int(entry))
                length = len(entry)-1
                for digit in entry:
                    if digit != "0":
                        output += f"{int(digit)*(10**length)}\n"
                    length -= 1
            else:
                entry = str(entry).split(".")
                length = len(entry[0])-1
                for digit in entry[0]:
                    if digit != "0":
                        output += f"{digit} * 10^{length}\n"
                    length -= 1
                if entry[1] != "0":
                    output += ".\n"
                    length = -1
                    for digit in entry[1]:
                        if digit != "0":
                            output += f"{digit} * 10^{length}\n"
                        length -= 1
            tk.messagebox.showinfo("Done!", output)

    def switch(self):
        # This function switches the placevalue and scientific notation buttons/labels. This makes it look like one of
        # the buttons was "selected" which looks nice. It just destroys the desired widgets and redefines them.
        self.placevalue.destroy()
        self.notation.destroy()
        if self.notationOff:
            self.placevalue = tk.Button(self, text="Place Value Mode", font=(None, 15), command=self.switch,
                                        bg="white")
            self.placevalue.grid(row=1, column=0, columnspan=2)
            self.notation = tk.Label(self, text="Scientific Notation Mode", font=(None, 15),
                                     bg="white")
            self.notation.grid(row=1, column=3, columnspan=2)
            self.notationOff = False
        else:
            self.placevalue = tk.Label(self, text="Place Value Mode", font=(None, 15),
                                       bg="white")
            self.placevalue.grid(row=1, column=0, columnspan=2)
            self.notation = tk.Button(self, text="Scientific Notation Mode", font=(None, 15), command=self.switch,
                                      bg="white")
            self.notation.grid(row=1, column=3, columnspan=2)
            self.notationOff = True


if __name__ == "__main__":
    start = HomePage()
    start.mainloop()