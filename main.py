import tkinter
from tkinter import DISABLED
from tkinter import NORMAL


window = tkinter.Tk()
window.title("BMI analysis")
window.minsize(300,200)

Underweight = 18.4
def calculate():
    weight = entry_weight.get()
    height = entry_height.get()
    if not weight or not height:
        return
    result = float(entry_weight.get()) / (float(entry_height.get())*float(entry_height.get())) * 10000
    if result <= 18.4:
        print(result_label.config(text="Underweight"))
    elif 18.5 <= result <= 29.9:
        print(result_label.config(text="Overweight "))
    elif 30.0 <= result <= 34.9:
        print(result_label.config(text="Obese - Class I "))
    elif 35.0 <= result <= 44.9:
        print(result_label.config(text="Obese - Class II "))
    elif 45.0 <= result:
        print(result_label.config(text="Extremely Obese - Class III "))
    else:
        print(result_label.config(text="I dont understand!"))


def checkEntries():
    if not entry_weight.get() or not entry_weight.get():
        button.configure(state=DISABLED)
    else:
        button.configure(state=NORMAL)





#space
space = tkinter.Label(text="")
space.pack(pady=3)

# weight
bmi_weight = tkinter.Label(text="Enter Your Weight")
bmi_weight.pack()
#frame = tkinter.Frame(bmi_weight)
#frame.pack(pady=15)

# entry_weight
entry_weight = tkinter.Entry()
entry_weight.pack(pady=2)

# height
bmi_hight = tkinter.Label(text= "Enter Your Height")
bmi_hight.pack()

#entry_height
entry_height = tkinter.Entry()
entry_height.pack(pady=2)

#button
button = tkinter.Button(text= "calculate", command= calculate)
button.pack(pady=7)

entry_weight.bind("<KeyRelease>", lambda e: checkEntries())
entry_height.bind("<KeyRelease>", lambda e: checkEntries())


#result
result_label = tkinter.Label(window, text='')
result_label.pack()

def checkNumberOnly(action, value_if_allowed):
    if action != '1':
        return True
    try:
        return value_if_allowed.isnumeric()
    except ValueError:
        return False

vcmd = (window.register(checkNumberOnly), '%d', '%P')
entry_weight.configure(validate='key', validatecommand=vcmd)



def checkNumberOnly(action, value_if_allowed):
    if action != '1':
        return True
    try:
        return value_if_allowed.isnumeric()
    except ValueError:
        return False

vcmd = (window.register(checkNumberOnly), '%d', '%P')
entry_height.configure(validate='key', validatecommand=vcmd)









window.mainloop()













