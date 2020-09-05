# 7/9/2020, Blue, Nicolas Keck, This program is supposed to act as an automatic pizza ordering system.
# By using tkinter instead of a text-based system, this program does not need much sanitization.
# Yes, the imports look odd, but apparently messagebox was not being imported by default
import tkinter as tk
from tkinter import messagebox


"""
This is a page container, all of the pages are stacked one on top of the other and 
whichever is needed is brought to the top. This is easier than simply destroying a
page after I'm done with it and also fixes some variable issues.
"""
class PageContainer(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("400x315")
        self.title("Pizza Co. Automatic Pizza System™")
        container = tk.Frame(self)
        container.configure(bg="white")
        container.pack()

        # This dictionary is used to store entry data from each page in order to write the receipt correctly
        self.program_data = {"name": "",
                             "pizza": None,
                             "toppings": []
                             }

        # This is where frames are initialized
        self.frames = {}
        for F in (HomePage, PizzaPage, ToppingPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")

    def show_frame(self, page_name):
        # Shows the frame for the given page name or outputs the bill
        if page_name == "Bill":
            total = float(self.program_data['pizza'][1]) + 0.25
            outstring = "Thank you for shopping at Pizza Co.!\n" \
                        "-------------\n" \
                        f"Customer name: {self.program_data['name']}\n" \
                        f"-------------\n" \
                        f"{self.program_data['pizza'][0]} - {str(self.program_data['pizza'][1])}\n"
            for topping in self.program_data['toppings']:
                outstring += f"{topping} - 0.10\n"
                total += 0.10
            outstring += "Taxes - 0.25\n" \
                         "-------------\n" \
                         f"Total: ${round(total, 2)}"
            tk.messagebox.showinfo("Receipt", outstring)
            self.quit()
        else:
            frame = self.frames[page_name]
            frame.tkraise()


# This is the frame for the home page
class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="white")
        tk.Label(self, text="Welcome to Pizza. Co!", font=(None, 29), bg="white").grid(row=0, column=0, columnspan=3)
        tk.Label(self, text="Please log in:", font=(None, 20), bg="white").grid(row=1, column=0, columnspan=3)
        tk.Label(self, text=" ", font=(None, 20), bg="white").grid(row=2)
        tk.Label(self, text="Full Name", font=(None, 20), bg="white").grid(row=3, column=0)
        self.nameEntry = tk.Entry(self, bg="white")
        self.nameEntry.insert(0, "")
        self.nameEntry.grid(row=3, column=1, columnspan=2)
        tk.Label(self, text="", font=(None, 20), bg="white").grid(row=4, column=0)
        tk.Button(self, text="Quit", command=controller.quit, font=(None, 20), bg="white").grid(row=5, column=0)
        tk.Button(self, text="Next", command=lambda: self.next(self.nameEntry.get()),
                  font=(None, 20), bg="white").grid(row=5, column=2)

    def next(self, entry):
        if entry == "":
            tk.messagebox.showerror("Error", "Please input a name to continue")
        else:
            self.controller.program_data["name"] = entry
            # I would love for the page itself to show the customer's name rather than a messagebox, but that would
            # take way too much time to implement unfortunately.
            tk.messagebox.showinfo("Welcome", f"Welcome back to Pizza Co. {entry}!")
            self.controller.show_frame("PizzaPage")


# This is the frame for the pizza selection page
class PizzaPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="white")
        self.title = tk.Label(self, text="Pizza Co. Selects",
                              font=(None, 29), bg="white")
        self.title.configure(anchor="center")
        self.title.grid(row=0, column=0, columnspan=4)
        tk.Label(self, text="Please select a pizza:", font=(None, 20), bg="white").grid(row=1, column=0, columnspan=4)
        tk.Label(self, text="Margarita", font=(None, 15), bg="white").grid(row=2, column=0, columnspan=2)
        tk.Button(self, text="M", font=(None, 10), bg="white", height=1, width=1,
                  command=lambda: self.select(("Margarita", 6.99))).grid(row=3, column=0)
        tk.Label(self, text="6.99", font=(None, 10), bg="white").grid(row=3, column=1)
        tk.Button(self, text="L", font=(None, 10), bg="white", height=1, width=1,
                  command=lambda: self.select(("Margarita", 8.99))).grid(row=4, column=0)
        tk.Label(self, text="8.99", font=(None, 10), bg="white").grid(row=4, column=1)
        tk.Label(self, text="Pepperoni", font=(None, 15), bg="white").grid(row=2, column=2, columnspan=2)
        tk.Button(self, text="M", font=(None, 10), bg="white", height=1, width=1,
                  command=lambda: self.select(("Pepperoni", 7.20))).grid(row=3, column=2)
        tk.Label(self, text="7.20", font=(None, 10), bg="white").grid(row=3, column=3)
        tk.Button(self, text="L", font=(None, 10), bg="white", height=1, width=1,
                  command=lambda: self.select(("Pepperoni", 9.00))).grid(row=4, column=2)
        tk.Label(self, text="9.00", font=(None, 10), bg="white").grid(row=4, column=3)
        tk.Label(self, text="Hawaii", font=(None, 15), bg="white").grid(row=5, column=0, columnspan=2)
        tk.Button(self, text="M", font=(None, 10), bg="white", height=1, width=1,
                  command=lambda: self.select(("Hawaii", 7.50))).grid(row=6, column=0)
        tk.Label(self, text="7.50", font=(None, 10), bg="white").grid(row=6, column=1)
        tk.Button(self, text="L", font=(None, 10), bg="white", height=1, width=1,
                  command=lambda: self.select(("Hawaii", 9.50))).grid(row=7, column=0)
        tk.Label(self, text="9.50", font=(None, 10), bg="white").grid(row=7, column=1)
        tk.Label(self, text="Tex Mex", font=(None, 15), bg="white").grid(row=5, column=2, columnspan=2)
        tk.Button(self, text="M", font=(None, 10), bg="white", height=1, width=1,
                  command=lambda: self.select(("Tex Mex", 7.50))).grid(row=6, column=2)
        tk.Label(self, text="7.50", font=(None, 10), bg="white").grid(row=6, column=3)
        tk.Button(self, text="L", font=(None, 10), bg="white", height=1, width=1,
                  command=lambda: self.select(("Tex Mex", 9.50))).grid(row=7, column=2)
        tk.Label(self, text="9.50", font=(None, 10), bg="white").grid(row=7, column=3)

    def select(self, info):
        # Allows the buttons on this page to function. Takes pizza name and price and saves it to the controller.
        # Also switches to the next page.
        self.controller.program_data["pizza"] = info
        self.controller.show_frame("ToppingPage")


# This is the frame for the topping selection page
class ToppingPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="white")
        tk.Label(self, text="Pizza Co. Toppings",
                 font=(None, 29), bg="white").grid(row=0, column=0)
        tk.Label(self, text="Please select extra toppings:",
                 font=(None, 15), bg="white").grid(row=1, column=0)
        olives = tk.IntVar()
        tk.Checkbutton(self, text="Olives", variable=olives, bg="white",
                       font=(None, 10)).grid(row=3, column=0, sticky="w", pady=8)
        jalapenos = tk.IntVar()
        tk.Checkbutton(self, text="Jalapeños", variable=jalapenos, bg="white",
                       font=(None, 10)).grid(row=4, column=0, sticky="w", pady=8)
        corn = tk.IntVar()
        tk.Checkbutton(self, text="Sweet Corn", variable=corn, bg="white",
                       font=(None, 10)).grid(row=5, column=0, sticky="w", pady=8)
        pepperoni = tk.IntVar()
        tk.Checkbutton(self, text="Pepperoni", variable=pepperoni, bg="white",
                       font=(None, 10)).grid(row=6, column=0, sticky="w", pady=8)
        mushrooms = tk.IntVar()
        tk.Checkbutton(self, text="Mushrooms", variable=mushrooms, bg="white",
                       font=(None, 10)).grid(row=7, column=0, sticky="w", pady=8)
        tk.Button(self, text="Checkout", command=lambda: self.checkout([olives.get(), jalapenos.get(),
                                                                        corn.get(), pepperoni.get(),
                                                                        mushrooms.get()])).grid(row=8, column=0)

    def checkout(self, vars):
        # Adds all the selected toppings to program data and then outputs the bill
        # This is most certainly inefficient, but tkinter makes everything a pain.
        if vars[0] == 1:
            self.controller.program_data["toppings"].append("Olives")
        if vars[1] == 1:
            self.controller.program_data["toppings"].append("Jalapeños")
        if vars[2] == 1:
            self.controller.program_data["toppings"].append("Sweet Corn")
        if vars[3] == 1:
            self.controller.program_data["toppings"].append("Pepperoni")
        if vars[4] == 1:
            self.controller.program_data["toppings"].append("Mushrooms")
        self.controller.show_frame("Bill")

if __name__ == "__main__":
    start = PageContainer()
    start.mainloop()