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

    height_value = height_entry.get()
    mass_value = mass_entry.get()

    try:

        bmi_result = float(mass_value) / ((float(height_value) / 100)**2)

        if bmi_result < 18.5:
            user_info = f"Your BMI result is {round(bmi_result,2)}. And you are Underweight! "
        elif 18.5 <= bmi_result < 25:
            user_info = f"Your BMI result is {round(bmi_result, 2)}. And you are in Normal Range. "
        elif 25 <= bmi_result < 30:
            user_info = f"Your BMI result is {round(bmi_result, 2)}. And you are Overweight! "
        elif 30 <= bmi_result < 35:
            user_info = f"Your BMI result is {round(bmi_result, 2)}. And you are Obese Class 1! "
        elif 35 <= bmi_result < 40:
            user_info = f"Your BMI result is {round(bmi_result, 2)}. And you are Obese Class 2! "
        else:
            user_info = f"Your BMI result is {round(bmi_result, 2)}. And you are Obese Class 3! "

        bmi_label.config(text=user_info)


    except:
        bmi_label.config(text="Please write a valid number.")

button = tkinter.Button(text="Calculate",command=button_clicked)
button.pack()

bmi_label = tkinter.Label(text="To see the result enter your informations...",font=FONT)
bmi_label.pack()

window.mainloop()