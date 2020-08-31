from tkinter import *

window = Tk()
window.title(" Unit converter")

def convert():
    text1.delete(1.0,END)
    text2.delete(1.0,END)
    text3.delete(1.0,END)
    kg_to_g()
    kg_to_pounds()
    kg_to_ounces()


def kg_to_g():
    text1.insert(END,str(float(entry_value.get()) / 1000) + 'g') 

def kg_to_pounds():
    text2.insert(END,str(float(entry_value.get()) * 2.20462) + 'pounds')

def kg_to_ounces():
    text3.insert(END,str(float(entry_value.get()) * 35.274) + 'ounces')

entry_value = StringVar()

entry = Entry(window,textvariable = entry_value )
entry.grid(row=0, column=0, padx=10, pady=10)

button1 = Button(window, text="Convert", command=convert)
button1.grid(row=0, column=2, padx=10, pady=10)

Label(window, text='Kg', height=1, width=20).grid(row=0, column=1, padx=10, pady=10)


text1 = Text(window, height=1, width=20)
text1.grid(row=1, column=0, padx=10, pady=10)

text2 = Text(window, height=1, width=20)
text2.grid(row=1, column=1, padx=10, pady=10)

text3 = Text(window, height=1, width=20)
text3.grid(row=1, column=2, padx=10, pady=10)



window.mainloop()