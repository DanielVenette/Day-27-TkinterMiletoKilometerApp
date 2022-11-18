from tkinter import *

# program window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=260, height=150)
window.config(padx=20, pady=20)

# number entry box
miles_input = Entry(width=5)
miles_input.grid(column=1, row=0)
miles_input.insert(END, string="0")
# miles_input.config(padx=10, pady=10) <-- no such option with entry

# text labels
miles_label = Label()
miles_label.grid(column=2, row=0)
miles_label.config(text="Miles", font=("Arial", 10, "normal"))
miles_label.config(padx=10, pady=10)

equal_label = Label()
equal_label.grid(column=0, row=1)
equal_label.config(text="is equal to", font=("Arial", 10, "normal"))
equal_label.config(padx=10, pady=10)

converted_num_label = Label()
converted_num_label.grid(column=1, row=1)
converted_num_label.config(text="0", font=("Arial", 10, "normal"))
converted_num_label.config(padx=10, pady=10)

km_label = Label()
km_label.grid(column=2, row=1)
km_label.config(text="Km", font=("Arial", 10, "normal"))
km_label.config(padx=10, pady=10)

# calculate button
def convert():
    miles = float(miles_input.get())
    km = round(miles * 1.609, 2)
    converted_num_label["text"] = f"{km}"


calculate_button = Button()
calculate_button["command"] = convert
calculate_button["text"] = "Calculate"
calculate_button.grid(column=1, row=2)
calculate_button.config(padx=5, pady=5)


window.mainloop()
