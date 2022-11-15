from tkinter import *
import math
exp = ""


def key_press(num, equation):
    global exp
    exp = exp + str(num)
    equation.set(exp)


def back_press(equation):
    global exp
    exp = exp[0:len(exp)-1]
    equation.set(exp)


def equal_press(equation):
    try:
        global exp
        if '%' in exp:
            left_num = int(exp[0:exp.index('%')])
            right_num = int(exp[exp.index('%')+1:])
            equation.set(str((left_num*right_num)/100))
            exp = ""
            return
        if 'm' in exp:
            left_num = int(exp[0:exp.index('m')])
            right_num = int(exp[exp.index('m') + 3:])
            equation.set(str(left_num % right_num))
            exp = ""
            return
        if '^' in exp:
            left_num = int(exp[0:exp.index('^')])
            right_num = int(exp[exp.index('^')+1:])
            equation.set(str(math.pow(left_num, right_num)))
            exp = ""
            return
        value = str(eval(exp))
        equation.set(value)
        exp = ""
    except:
        equation.set("Invalid Expression")
        exp = ""


def clear_screen(equation):
    global exp
    exp = ""
    equation.set("")


def calc_sin(equation):
    global exp
    num = int(exp)
    val = str(math.sin(num))
    equation.set(val)


def calc_cos(equation):
    global exp
    num = int(exp)
    val = str(math.cos(num))
    equation.set(val)


def calc_tan(equation):
    global exp
    num = int(exp)
    val = str(math.tan(num))
    equation.set(val)


def calc_area(equation):
    global exp
    radius = int(exp)
    val = str(3.14 * pow(radius, 2))
    equation.set(val)


def calc_peri(equation):
    global exp
    radius = int(exp)
    val = str(2 * 3.14 * radius)
    equation.set(val)


def calc_log(base, equation):
    global exp
    num = int(exp)
    val = str(math.log(num, base))
    equation.set(val)


def calc_power(equation):
    global exp
    value = int(exp)
    equation.set(str(value ** 2))
    exp = ""


def special_divide(equation):
    global exp
    value = int(exp)
    equation.set(str(1/value))
    exp = ""


def calc_absolute(equation):
    global exp
    value = int(exp)
    if value < 0:
        value *= -1
    exp = str(value)
    equation.set(exp)


def calculate_factorial(equation):
    global exp
    fact = 1
    num = int(exp)
    for i in range(1, num+1):
        fact *= i
    exp = str(fact)
    equation.set(exp)


def root_press(equation):
    global exp
    value = int(exp)
    equation.set(str(math.sqrt(value)))
    exp = ""


def negate_press(equation):
    global exp
    value = int(exp)
    value *= -1
    equation.set(str(value))
    exp = str(value)


def func():
    window = Tk()
    window.geometry("505x450")
    window.minsize(width=505, height=450)
    window.maxsize(width=505, height=450)
    window.title("Scientific Calculator")
    equation = StringVar()
    expression_field = Entry(window, textvariable=equation, width=25, font=('Georgia', 20, 'bold'))
    expression_field.grid(pady=20, columnspan=5)
    button1 = Button(text="c", width=13, height=2, command=lambda: key_press('300000000', equation))
    button1.grid(row=2, column=0)
    button2 = Button(text="Π", width=13, height=2, command=lambda: key_press('3.14', equation))
    button2.grid(row=2, column=1)
    button3 = Button(text="e", width=13, height=2, command=lambda: key_press('2.718', equation))
    button3.grid(row=2, column=2)
    button4 = Button(text="C", width=13, height=2, command=lambda: clear_screen(equation))
    button4.grid(row=2, column=3)
    button5 = Button(text="<-", width=13, height=2, command=lambda: back_press(equation))
    button5.grid(row=2, column=4)
    button6 = Button(text="x^2", width=13, height=2, command=lambda: calc_power(equation))
    button6.grid(row=3, column=0)
    button7 = Button(text="1/x", width=13, height=2, command=lambda: special_divide(equation))
    button7.grid(row=3, column=1)
    button8 = Button(text="|x|", width=13, height=2, command=lambda: calc_absolute(equation))
    button8.grid(row=3, column=2)
    button9 = Button(text="%", width=13, height=2, command=lambda: key_press('%', equation))
    button9.grid(row=3, column=3)
    button10 = Button(text="mod", width=13, height=2, command=lambda: key_press('mod', equation))
    button10.grid(row=3, column=4)
    button11 = Button(text="√x", width=13, height=2, command=lambda: root_press(equation))
    button11.grid(row=4, column=0)
    button12 = Button(text="(", width=13, height=2, command=lambda: key_press('(', equation))
    button12.grid(row=4, column=1)
    button13 = Button(text=")", width=13, height=2, command=lambda: key_press(')', equation))
    button13.grid(row=4, column=2)
    button14 = Button(text="n!", width=13, height=2, command=lambda: calculate_factorial(equation))
    button14.grid(row=4, column=3)
    button15 = Button(text="÷", width=13, height=2, command=lambda: key_press('/', equation))
    button15.grid(row=4, column=4)
    button16 = Button(text="x^y", width=13, height=2, command=lambda: key_press('^', equation))
    button16.grid(row=5, column=0)
    button17 = Button(text="7", width=13, height=2, command=lambda: key_press('7', equation))
    button17.grid(row=5, column=1)
    button18 = Button(text="8", width=13, height=2, command=lambda: key_press('8', equation))
    button18.grid(row=5, column=2)
    button19 = Button(text="9", width=13, height=2, command=lambda: key_press('9', equation))
    button19.grid(row=5, column=3)
    button20 = Button(text="*", width=13, height=2, command=lambda: key_press('*', equation))
    button20.grid(row=5, column=4)
    button21 = Button(text="10^x", width=13, height=2, command=lambda: key_press('10^', equation))
    button21.grid(row=6, column=0)
    button22 = Button(text="4", width=13, height=2, command=lambda: key_press('4', equation))
    button22.grid(row=6, column=1)
    button23 = Button(text="5", width=13, height=2, command=lambda: key_press('5', equation))
    button23.grid(row=6, column=2)
    button24 = Button(text="6", width=13, height=2, command=lambda: key_press('6', equation))
    button24.grid(row=6, column=3)
    button25 = Button(text="-", width=13, height=2, command=lambda: key_press('-', equation))
    button25.grid(row=6, column=4)
    button26 = Button(text="log", width=13, height=2, command=lambda: calc_log(10, equation))
    button26.grid(row=7, column=0)
    button27 = Button(text="1", width=13, height=2, command=lambda: key_press('1', equation))
    button27.grid(row=7, column=1)
    button28 = Button(text="2", width=13, height=2, command=lambda: key_press('2', equation))
    button28.grid(row=7, column=2)
    button29 = Button(text="3", width=13, height=2, command=lambda: key_press('3', equation))
    button29.grid(row=7, column=3)
    button30 = Button(text="+", width=13, height=2, command=lambda: key_press('+', equation))
    button30.grid(row=7, column=4)
    button31 = Button(text="ln", width=13, height=2, command=lambda: calc_log(2.71, equation))
    button31.grid(row=8, column=0)
    button32 = Button(text="+/-", width=13, height=2, command=lambda: negate_press(equation))
    button32.grid(row=8, column=1)
    button33 = Button(text="0", width=13, height=2, command=lambda: key_press('0', equation))
    button33.grid(row=8, column=2)
    button34 = Button(text=".", width=13, height=2, command=lambda: key_press('.', equation))
    button34.grid(row=8, column=3)
    button35 = Button(text="=", width=13, height=2, command=lambda: equal_press(equation))
    button35.grid(row=8, column=4)
    button36 = Button(text="sin(x)", width=13, height=2, command=lambda: calc_sin(equation))
    button36.grid(row=9, column=0)
    button37 = Button(text="cos(x)", width=13, height=2, command=lambda: calc_cos(equation))
    button37.grid(row=9, column=1)
    button38 = Button(text="tan(x)", width=13, height=2, command=lambda: calc_tan(equation))
    button38.grid(row=9, column=2)
    button39 = Button(text="Πr^2", width=13, height=2, command=lambda: calc_area(equation))
    button39.grid(row=9, column=3)
    button40 = Button(text="2Πr", width=13, height=2, command=lambda: calc_peri(equation))
    button40.grid(row=9, column=4)
    window.mainloop()
