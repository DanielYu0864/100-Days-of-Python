from tkinter import *
window = Tk()
window.title('Mile to Km Converter')
window.minsize(width=500, height=250)
window.config(padx=100, pady=30)  # padding_x and padding_y

def convert_mile_to_km():
    mile = float(mile_input.get())
    km = round(mile * 1.60934, 2)
    km_output.config(text=f'{km}')

# label

miles = Label(text='Miles', font=('Arial', 10, 'bold'))
miles.grid(column=2, row=0)
miles.config(padx=20, pady=20)

label_2 = Label(text='is equal to', font=('Arial', 10, 'bold'))
label_2.grid(column=0, row=1)
label_2.config(padx=20, pady=20)

km_label = Label(text='Km', font=('Arial', 10, 'bold'))
km_label.grid(column=2, row=1)
km_label.config(padx=20, pady=20)

km_output = Label(text='0', font=('Arial', 10, 'bold'))
km_output.grid(column=1, row=1)
km_output.config(padx=20, pady=20)

# button
cal_btn = Button(text='Calculate', command=convert_mile_to_km)
cal_btn.grid(column=1, row=2)

# entry

mile_input = Entry(width=20)
mile_input.grid(column=1, row=0)


window.mainloop()
