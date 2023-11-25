import tkinter

x = 300
y = 150

FONT = ('San Fransisco',13,"italic")



def button_clicked():
    global mass_float
    global height_float
    print(mass_float / (height_float/100)(height_float/100))
    print("Button Clicked")

'''

user_height = input(int())
user_mass = input(int())

def button_clicked():
    global user_mass
    global user_height
    print("Button Clicked")
    print(user_mass, user_height)


def calculation():
    global user_mass
    global user_height
    result = [(user_height/100) * (user_height/100)] / user_mass
    print(result)
    
'''


window = tkinter.Tk()
window.title("Body Mass Index Calculator")
window.wm_minsize(x,y)

mass_label = tkinter.Label(text="Enter Your Weight(kg)",font=FONT)
mass_label.pack()

mass_entry = tkinter.Entry()
mass_float = int(mass_entry)
mass_entry.pack()
mass_entry.focus()

height_label = tkinter.Label(text="Enter Your Height(cm)",font=FONT)
height_label.pack()

height_entry = tkinter.Entry()
height_float = int(height_entry)
height_entry.pack()

button = tkinter.Button(text="Calculate",command=button_clicked)
button.pack()




window.mainloop()