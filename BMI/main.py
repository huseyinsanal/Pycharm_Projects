import tkinter

x = 300
y = 150

FONT = ('San Fransisco',13,"italic")



window = tkinter.Tk()
window.title("Body Mass Index Calculator")
window.wm_minsize(x,y)

mass_label = tkinter.Label(text="Enter Your Weight(kg)",font=FONT)
mass_label.pack()

mass_entry = tkinter.Entry()
mass_entry.pack()

height_label = tkinter.Label(text="Enter Your Height(cm)",font=FONT)
height_label.pack()

height_entry = tkinter.Entry()
height_entry.pack()



def button_clicked():

    height_string = height_entry.get()
    mass_string = mass_entry.get()

    mass_value = int(mass_string)
    height_value = int(height_string)

    result = mass_value / ((height_value / 100)**2)
    bmi_label.config(text=result)

    print("Button Clicked")

button = tkinter.Button(text="Calculate",command=button_clicked)
button.pack()

bmi_label = tkinter.Label(text="To see the result enter your informations...",font=FONT)
bmi_label.pack()

window.mainloop()