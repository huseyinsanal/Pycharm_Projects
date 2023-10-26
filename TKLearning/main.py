import tkinter

def click_button():
    user_input = my_entry.get()
    print(user_input)

#Window
window = tkinter.Tk()
window.title("Python Tkinter")
window.wm_minsize(width=450, height=300)

#Label
my_label = tkinter.Label(text="this is a lable", font=('Arial', 30, "italic"))
#my_label.config(bg="black", fg="white")
#my_label.pack(side="top")
#my_label.place(x=0, y=0)
my_label.grid(row=0, column=0)

#Button
my_button = tkinter.Button(text="this is a button", command=click_button)
#my_button.pack(side="bottom")
#my_button.place(x=225-63, y=150-14)
#my_button.update()
#print(my_button.winfo_height())
#print(my_button.winfo_width())
my_button.grid(row=1, column=1)

#Entry
my_entry = tkinter.Entry(width=15)
#my_entry.pack(side="bottom")
#my_entry.place(x=300,y=200)
my_entry.grid(row=2,column=2)

window.mainloop()