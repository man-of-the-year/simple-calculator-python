from tkinter import *


def button_press(num):

    global equation_text
    equation_text = equation_text + str(num)
    var_label.set(equation_text)

def equals():
    
    global equation_text
    try:
        total = str(eval(equation_text))
        var_label.set(total)
        equation_text = total
    except ZeroDivisionError:
        var_label.set('U divided by zero')
        equation_text = ''

    except SyntaxError:
        var_label.set('Not correct syntax')
        equation_text = ''

def clear():
    global equation_text
    var_label.set('')
    equation_text = '' 


broken = Tk()
broken.geometry('500x550')

equation_text = ''
var_label = StringVar()


label = Label(broken,textvariable=var_label,width=24,bg='black',height=3,font=('ink free',20),fg='#7fff3b')
label.pack()

frame = Frame(broken)
frame.pack()

button1 = Button(frame,text=1,height=4,width=9,command=lambda:button_press(1),bg='black',fg='#7fff3b',font=35)
button1.grid(row=0,column=0)

button2 = Button(frame,text=2,height=4,width=9,command=lambda:button_press(2),bg='black',fg='#7fff3b',font=35)
button2.grid(row=0,column=1)

button3 = Button(frame,text=3,height=4,width=9,command=lambda:button_press(3),bg='black',fg='#7fff3b',font=35)
button3.grid(row=0,column=2)

button4 = Button(frame,text=4,height=4,width=9,command=lambda:button_press(4),bg='black',fg='#7fff3b',font=35)
button4.grid(row=1,column=0)

button5 = Button(frame,text=5,height=4,width=9,command=lambda:button_press(5),bg='black',fg='#7fff3b',font=35)
button5.grid(row=1,column=1)

button6 = Button(frame,text=6,height=4,width=9,command=lambda:button_press(6),bg='black',fg='#7fff3b',font=35)
button6.grid(row=1,column=2)

button7 = Button(frame,text=7,height=4,width=9,command=lambda:button_press(7),bg='black',fg='#7fff3b',font=35)
button7.grid(row=2,column=0)

button8 = Button(frame,text=8,height=4,width=9,command=lambda:button_press(8),bg='black',fg='#7fff3b',font=35)
button8.grid(row=2,column=1)

button9 = Button(frame,text=9,height=4,width=9,command=lambda:button_press(9),bg='black',fg='#7fff3b',font=35)
button9.grid(row=2,column=2)

button0 = Button(frame,text=0,height=4,width=9,command=lambda:button_press(0),bg='black',fg='#7fff3b',font=35)
button0.grid(row=3,column=1)

plus = Button(frame,text='+',height=4,width=9,command=lambda:button_press('+'),bg='black',fg='#7fff3b',font=35)
plus.grid(row=0,column=3)

minus = Button(frame,text='-',height=4,width=9,command=lambda:button_press('-'),bg='black',fg='#7fff3b',font=35)
minus.grid(row=1,column=3)

multiply = Button(frame,text='*',height=4,width=9,command=lambda:button_press('*'),bg='black',fg='#7fff3b',font=35)
multiply.grid(row=3,column=2)

divide = Button(frame,text='/',height=4,width=9,command=lambda:button_press('/'),bg='black',fg='#7fff3b',font=35)
divide.grid(row=3,column=0)

equal = Button(frame,text='=',height=4,width=9,command=equals,bg='black',fg='#7fff3b',font=35)
equal.grid(row=3,column=3)

decimal = Button(frame,text='.',height=4,width=9,command=lambda:button_press('.'),bg='black',fg='#7fff3b',font=35)
decimal.grid(row=2,column=3)

clear = Button(frame,text='Clear',height=4,width=9,command=clear,bg='black',fg='#7fff3b',font=35)
clear.grid(row=4,column=3)


broken.mainloop()