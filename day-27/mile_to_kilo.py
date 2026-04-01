from tkinter import *

window = Tk()
window.title("Mile to Kilometer Converter")

window.minsize(width=500, height=300)
window.config(padx=20, pady=20)
window.resizable(False, False)

text = Label(text="Miles")
text.grid(column=2, row=0)

entry = Entry(width=10)
entry.grid(column=1, row=0) 

text2 = Label(text="is equal to")
text2.grid(column=0, row=1)

text3 = Label(text="0")
text3.grid(column=1, row=1)

text4 = Label(text="Kilometers")
text4.grid(column=2, row=1)

def button_clicked():
    miles = float(entry.get())
    kilometers = miles * 1.60934
    text3.config(text=f"{kilometers:.2f}")

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()
