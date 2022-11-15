from tkinter import *
import math
exp = ""


def back_press(equation):
    global exp
    exp = exp[0:len(exp)-1]
    equation.set(exp)


def key_press(num, equation):
    global exp
    exp = exp + str(num)
    equation.set(exp)


def clear_screen(equation):
    global exp
    exp = ""
    equation.set("")


def equal_press(equation):
    try:
        global exp
        if '%' in exp:
            left_num = int(exp[0:exp.index('%')])
            right_num = int(exp[exp.index('%')+1:])
            equation.set(str((left_num*right_num)/100))
            exp = ""
            return
        value = str(eval(exp))
        equation.set(value)
        exp = ""
    except:
        equation.set("Invalid Expression")
        exp = ""


def power_button(equation):
    global exp
    value = int(exp)
    equation.set(str(value ** 2))
    exp = ""


def root_press(equation):
    global exp
    value = int(exp)
    equation.set(str(math.sqrt(value)))
    exp = ""


def special_divide(equation):
    global exp
    value = int(exp)
    equation.set(str(1/value))
    exp = ""


def negate_press(equation):
    global exp
    value = int(exp)
    value *= -1
    equation.set(str(value))
    exp = str(value)


def func():
    window = Tk()
    window.geometry("410x350")
    window.minsize(width=410, height=350)
    window.maxsize(width=410, height=350)
    window.title("Normal Calculator")
    equation = StringVar()
    expression_field = Entry(window, textvariable=equation, width=20, font=('Georgia', 20, 'bold'))
    expression_field.grid(pady=20, columnspan=4)
    button1 = Button(text="%", width=13, height=2, command=lambda: key_press('%', equation))
    button1.grid(row=2, column=0)
    button2 = Button(text="CE", width=13, height=2,  command=lambda: clear_screen(equation))
    button2.grid(row=2, column=1)
    button3 = Button(text="C", width=13, height=2, command=lambda: clear_screen(equation))
    button3.grid(row=2, column=2)
    button4 = Button(text="<-", width=13, height=2, command=lambda: back_press(equation))
    button4.grid(row=2, column=3)
    button5 = Button(text="1/x", width=13, height=2, command=lambda: special_divide(equation))
    button5.grid(row=3, column=0)
    button6 = Button(text="x^2", width=13, height=2, command=lambda: power_button(equation))
    button6.grid(row=3, column=1)
    button7 = Button(text="√", width=13, height=2, command=lambda: root_press(equation))
    button7.grid(row=3, column=2)
    button8 = Button(text="÷", width=13, height=2, command=lambda: key_press('/', equation))
    button8.grid(row=3, column=3)
    button9 = Button(text="7", width=13, height=2, command=lambda: key_press('7', equation))
    button9.grid(row=4, column=0)
    button10 = Button(text="8", width=13, height=2, command=lambda: key_press('8', equation))
    button10.grid(row=4, column=1)
    button11 = Button(text="9", width=13, height=2, command=lambda: key_press('9', equation))
    button11.grid(row=4, column=2)
    button12 = Button(text="*", width=13, height=2, command=lambda: key_press('*', equation))
    button12.grid(row=4, column=3)
    button13 = Button(text="4", width=13, height=2, command=lambda: key_press('4', equation))
    button13.grid(row=5, column=0)
    button14 = Button(text="5", width=13, height=2, command=lambda: key_press('5', equation))
    button14.grid(row=5, column=1)
    button15 = Button(text="6", width=13, height=2, command=lambda: key_press('6', equation))
    button15.grid(row=5, column=2)
    button16 = Button(text="-", width=13, height=2, command=lambda: key_press('-', equation))
    button16.grid(row=5, column=3)
    button17 = Button(text="1", width=13, height=2, command=lambda: key_press('1', equation))
    button17.grid(row=6, column=0)
    button18 = Button(text="2", width=13, height=2, command=lambda: key_press('2', equation))
    button18.grid(row=6, column=1)
    button19 = Button(text="3", width=13, height=2, command=lambda: key_press('3', equation))
    button19.grid(row=6, column=2)
    button20 = Button(text="+", width=13, height=2, command=lambda: key_press('+', equation))
    button20.grid(row=6, column=3)
    button21 = Button(text="+/-", width=13, height=2, command=lambda: negate_press(equation))
    button21.grid(row=7, column=0)
    button22 = Button(text="0", width=13, height=2, command=lambda: key_press('0', equation))
    button22.grid(row=7, column=1)
    button23 = Button(text=".", width=13, height=2, command=lambda: key_press('.', equation))
    button23.grid(row=7, column=2)
    button24 = Button(text="=", width=13, height=2, command=lambda: equal_press(equation))
    button24.grid(row=7, column=3)
    window.mainloop()
