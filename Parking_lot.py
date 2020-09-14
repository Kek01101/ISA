# Nicolas Keck, Parking lot program which allows you to check in and out of a parking lot with a GUI
# Also outputs your bill based on the minutes in the parking lot
# Make checkout appear once check-in is clicked <-- LATER
import tkinter as tk
from tkinter import messagebox
import datetime

# Program class
class ParkingLot(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.configure(bg="white")
        self.title("Premier digital parking lot software")
        self.geometry("370x200")
        self.inbutton = tk.Button(self, text="Check in", command=self.check_in, font=(None, 40),
                             bg="white", height=10, width=10)
        self.inbutton.pack()

        self.checkin = False
        self.time = 0
        self.minutes_passed = 0


    # Function for checking-in
    def check_in(self):
        if self.checkin:
            tk.messagebox.showerror("Error", "You have already checked-in!")
        else:
            self.inbutton.destroy()
            self.inbutton = tk.Button(self, text="Check out", command=self.check_out, font=(None, 40),
                              bg="white", height=10, width=10)
            self.inbutton.pack()
            self.checkin = True
            self.time = datetime.datetime.now()


    # Function for checking-out
    def check_out(self):
        if not self.checkin:
            tk.messagebox.showerror("Error", "You need to check in first!")
        else:
            # Will not work if a day has passed since the code started
            self.checkin = False
            self.inbutton.destroy()
            self.inbutton = tk.Button(self, text="Check in", command=self.check_in, font=(None, 40),
                             bg="white", height=10, width=10)
            self.inbutton.pack()
            self.time = datetime.datetime.now() - self.time
            self.time = str(self.time).split(":")
            for hour in range(0, int(self.time[0])):
                self.minutes_passed += 60
            for minute in range(0, int(self.time[1])):
                self.minutes_passed += 1
            tk.messagebox.showinfo("Bill", f"Minutes passed: {self.minutes_passed}\nPrice per minute: $0.99\nBill: "
                                           f"${round(self.minutes_passed*0.99, 2)}")


if __name__ == "__main__":
    start = ParkingLot()
    start.mainloop()