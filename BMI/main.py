import tkinter

x = 300
y = 150

FONT = (None,13,"bold italic")

def button_clicked():
    user_mass = mass_entry.get()
    user_height = height_entry.get()

    print("Button Clicked")
    print(user_mass, user_height)

window = tkinter.Tk()
window.title("Body Mass Index Calculator")
window.wm_minsize(x,y)

mass_label = tkinter.Label(text="Enter Your Weight(kg)",font=FONT)
mass_label.pack()

mass_entry = tkinter.Entry()
mass_entry.pack()
mass_entry.focus()

height_label = tkinter.Label(text="Enter Your Height(cm)",font=FONT)
height_label.pack()

height_entry = tkinter.Entry()
height_entry.pack()

button = tkinter.Button(text="Calculate",command=button_clicked)
button.pack()


window.mainloop()