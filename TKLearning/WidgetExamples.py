from tkinter import *

#Window
window = Tk()
window.title("Tkinter Python")
window.minsize(width=600,height=600)
window.config(padx=20, pady=20)

#Label
label = Label(text="my label")
label.config(bg="black")
label.config(fg="white")
label.config(padx=10,pady=10)
label.pack()

#Button
def button_clicked():
    print("button clicked")
    print(text.get("1.3",END))

button = Button(text="button", command=button_clicked)
button.config(padx=10, pady=10)
button.pack()

#Entry
entry = Entry(width=20)
entry.pack()

#Multiline text
text = Text(width=30, height=2)
text.focus()
text.pack()

#Scale
def scale_selected(value):
    print(value)

my_scale = Scale(from_=0,to=50, command=scale_selected)
my_scale.pack()

#Spinbox
def spinbox_selected():
    print(my_spinbox.get())

my_spinbox = Spinbox(from_=0,to=50,command=spinbox_selected)
my_spinbox.pack()

#Checkbutton
def checkbutton_selected():
    print(check_state.get())

check_state = IntVar()
my_checkbutton = Checkbutton(text="check",variable=check_state,command=checkbutton_selected)
my_checkbutton.pack()

#Radio button
def radio_selected():
    print(radio_checked_state.get())

radio_checked_state = IntVar()
my_radiobutton = Radiobutton(text="1. option", value=10, variable=radio_checked_state, command=radio_selected)
my_radiobutton_2 = Radiobutton(text="2. option", value=20, variable=radio_checked_state, command=radio_selected)
my_radiobutton.pack()
my_radiobutton_2.pack()

#Listbox

def listbox_selected(event):
    print(my_listbox.get(my_listbox.curselection()))
my_listbox = Listbox()
name_list = ["Hasan", "Hüseyin", "Ali", "Mehmet", "Heck"]
for i in range(len(name_list)):
    my_listbox.insert(i,name_list[i])
my_listbox.bind('<<ListboxSelect>>',listbox_selected)
my_listbox.pack()

window.mainloop()