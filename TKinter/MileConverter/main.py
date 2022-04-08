import tkinter


def converter():
    mile = mile_in.get()
    km = float(mile) * 1.609
    km_res_label.config(text=km)
    

window = tkinter.Tk()

window.title("Mile to Kilometer")
window.minsize(width=250, height=100)
window.config(padx=20, pady=20)


#Label
mile_in = tkinter.Entry(width=15)
mile_in.grid(column=1, row=0)

mile_label = tkinter.Label(text="Mile(s)")
mile_label.grid(column=2, row=0)

equal_label = tkinter.Label(text="is equal to")
equal_label.grid(column=0, row=1)

km_res_label = tkinter.Label()
km_res_label.grid(column=1, row=1)

km_label = tkinter.Label(text="km(s)")
km_label.grid(column=2, row=1)

button = tkinter.Button(text="Convert", command=converter)
button.grid(column=1, row=2)












window.mainloop()