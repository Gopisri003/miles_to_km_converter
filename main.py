import tkinter


def button_click():
    miles = float(input.get())
    km = float(miles * 1.609)
    my_lable3.config(text=km)


# Window
window = tkinter.Tk()
window.title("Miles to Kilometer converter")
window.minsize(width=350, height=300)

my_lable = tkinter.Label(text="Mile", font=("Arial", 12, "bold"))
my_lable1 = tkinter.Label(text="is equal to ", font=("Arial", 12, "bold"))
my_lable2 = tkinter.Label(text="Km", font=("Arial", 12, "bold"))
my_lable3 = tkinter.Label(text="0", font=("Arial", 12, "bold"))
my_lable.grid(column=2, row=0)
my_lable1.grid(column=0, row=1)
my_lable2.grid(column=2, row=1)
my_lable3.grid(column=1, row=1)
my_lable, my_lable1, my_lable2, my_lable3.config(padx=20, pady=20)

# Button
button = tkinter.Button(text="Calculate", font=("Arial", 12, "bold"), command=button_click)
button.grid(column=1, row=2)
button.config(padx=20, pady=20)

# Entry
input = tkinter.Entry(width=10)
input.grid(column=1, row=0)

window.mainloop()
