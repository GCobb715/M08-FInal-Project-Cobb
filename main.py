from tkinter import *
from tkinter import PhotoImage


# Create the main Window
window = Tk()
window.title("Gabe's Goulash Ordering")
window.minsize(1280, 720)

# Create title label
title_label = Label(window, text="Welcome to Gabe's Goulash! Construct your order, and click total to total your order.")
title_label.config(font=('', 25))
title_label.grid(row=0, column=3)


def total_click():
    # Open a new window
    new_window = Tk()
    # Get the input values from the Entry Fields
    num1 = entry_label1.get()
    num2 = entry_label2.get()
    num3 = entry_label3.get()
    # Convert the inputs to floats
    f_num1 = float(num1) * 7.50
    f_num2 = float(num2) * 5.50
    f_num3 = float(num3) * 3.50
    # Calculate the total and tax
    subtotal = f_num1 + f_num2 + f_num3
    tax = subtotal * .07
    total = subtotal + tax
    # Print total and create label to print in new window
    subtotaltext = "Your subtotal is: $%.2f" % subtotal
    subtotal_label = Label(new_window, text=subtotaltext)
    subtotal_label.grid(row=0, column=0)
    taxtext = "Your tax is: $%.2f" % tax
    tax_label = Label(new_window, text=taxtext)
    tax_label.grid(row=2, column=0)
    totaltext = "Your Total is: $%.2f" % total
    total_label1 = Label(new_window, text=totaltext)
    total_label1.grid(row=3, column=0)


# Create all the input fields
entry_label1 = Entry(window, width=20)
entry_label1.grid(row=2, column=2, padx=10, pady=50)
entry_label1.insert(0, '0')
entry_label2 = Entry(window, width=20)
entry_label2.grid(row=3, column=2, padx=10, pady=50)
entry_label2.insert(0, '0')
entry_label3 = Entry(window, width=20)
entry_label3.grid(row=4, column=2, padx=10, pady=50)
entry_label3.insert(0, '0')


# Create the total button and assign the command
total_button = Button(window, text="Total", command=lambda: total_click())
total_button.grid(row=5, column=0)


def button1_click():
    # Create a new window for the image and label
    new_window = Toplevel()
    large_label = Label(new_window, text="Large Goulash")
    large_label.pack()
    canvas = Canvas(new_window, width=500, height=500)
    canvas.pack(expand=YES, fill=BOTH)
    # Insert image into new window
    image1 = PhotoImage(file="goulash03.gif")
    canvas.create_image(10, 10, image=image1, anchor=NW)
    canvas.image1 = image1


def button2_click():
    new_window = Toplevel()
    medium_label = Label(new_window, text="Medium Goulash")
    medium_label.pack()
    canvas = Canvas(new_window, width=500, height=500)
    canvas.pack(expand=YES, fill=BOTH)
    image2 = PhotoImage(file="goulash02.gif")
    canvas.create_image(10, 10, image=image2, anchor=NW)
    canvas.image2 = image2


def button3_click():
    new_window = Toplevel()
    small_label = Label(new_window, text="Small Goulash")
    small_label.pack()
    canvas = Canvas(new_window, width=500, height=500)
    canvas.pack(expand=YES, fill=BOTH)
    image3 = PhotoImage(file="goulash01.gif")
    canvas.create_image(10, 10, image=image3, anchor=NW)
    canvas.image3 = image3


# Create the buttons to allow for images to be displayed
food_button1 = Button(window, text="Large Goulash: $7.50", command=button1_click)
food_button2 = Button(window, text="Medium Goulash: $5.50", command=button2_click)
food_button3 = Button(window, text="Small Goulash: $3.50", command=button3_click)

food_button1.grid(row=2, column=1)
food_button2.grid(row=3, column=1)
food_button3.grid(row=4, column=1)

window.mainloop()

