from tkinter import *
import math
exp = ""


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
        value = str(eval(exp))
        equation.set(value)
        exp = ""
    except:
        equation.set("Invalid Expression")
        exp = ""


def check_prime(equation):
    global exp
    num = int(exp)
    ctr = 0
    for i in range(1, num+1):
        if num % i == 0:
            ctr += 1
    if ctr == 2:
        exp = f"{num} Prime Number"
    else:
        exp = f"{num} Not a Prime Number"
    equation.set(exp)


def calc_gcd(equation):
    global exp
    num1 = int(exp[0:exp.index(',')])
    num2 = int(exp[exp.index(',')+1:])
    gcd = math.gcd(num1, num2)
    exp = str(gcd)
    equation.set(exp)


def calc_lcm(equation):
    global exp
    num1 = int(exp[0:exp.index(',')])
    num2 = int(exp[exp.index(',')+1:])
    gcd = math.gcd(num1, num2)
    lcm = int((num1 * num2) / gcd)
    exp = str(lcm)
    equation.set(exp)


def calculate_factorial(equation):
    global exp
    fact = 1
    num = int(exp)
    for i in range(1, num+1):
        fact *= i
    exp = str(fact)
    equation.set(exp)


def calculate_factor(equation):
    global exp
    num = int(exp)
    factors = ""
    for i in range(1, num+1):
        if num % i == 0:
            factors += str(i) + " "
    exp = str(factors)
    equation.set(exp)


def convert_binary(equation):
    global exp
    num = int(exp)
    val = bin(num)
    exp = str(val)[2:]
    equation.set(exp)


def convert_octal(equation):
    global exp
    num = int(exp)
    val = oct(num)
    exp = str(val)[2:]
    equation.set(exp)


def convert_hexadecimal(equation):
    global exp
    num = int(exp)
    val = hex(num)
    exp = str(val)[2:].upper()
    equation.set(exp)


def func():
    window = Tk()
    window.geometry("410x400")
    window.minsize(width=410, height=400)
    window.maxsize(width=410, height=400)
    window.title("Programmer Calculator")
    equation = StringVar()
    expression_field = Entry(window, textvariable=equation, width=20, font=('Georgia', 20, 'bold'))
    expression_field.grid(pady=20, columnspan=4)
    button1 = Button(text="&", width=13, height=2, command=lambda: key_press('&', equation))
    button1.grid(row=2, column=0)
    button2 = Button(text="|", width=13, height=2, command=lambda: key_press('|', equation))
    button2.grid(row=2, column=1)
    button3 = Button(text="~", width=13, height=2, command=lambda: key_press('~', equation))
    button3.grid(row=2, column=2)
    button4 = Button(text="^", width=13, height=2, command=lambda: key_press('^', equation))
    button4.grid(row=2, column=3)
    button5 = Button(text=">>", width=13, height=2, command=lambda: key_press('>>', equation))
    button5.grid(row=3, column=0)
    button6 = Button(text="<<", width=13, height=2, command=lambda: key_press('<<', equation))
    button6.grid(row=3, column=1)
    button7 = Button(text="Check Prime", height=2, width=13, command=lambda: check_prime(equation))
    button7.grid(row=3, column=2)
    button8 = Button(text="Check Perfect", height=2, width=13, command=lambda: key_press('Perfect:- ', equation))
    button8.grid(row=3, column=3)
    button9 = Button(text="7", width=13, height=2, command=lambda: key_press('7', equation))
    button9.grid(row=4, column=0)
    button10 = Button(text="8", width=13, height=2, command=lambda: key_press('8', equation))
    button10.grid(row=4, column=1)
    button11 = Button(text="9", width=13, height=2, command=lambda: key_press('9', equation))
    button11.grid(row=4, column=2)
    button12 = Button(text="4", width=13, height=2, command=lambda: key_press('4', equation))
    button12.grid(row=5, column=0)
    button13 = Button(text="5", width=13, height=2, command=lambda: key_press('5', equation))
    button13.grid(row=5, column=1)
    button14 = Button(text="6", width=13, height=2, command=lambda: key_press('6', equation))
    button14.grid(row=5, column=2)
    button15 = Button(text="1", width=13, height=2, command=lambda: key_press('1', equation))
    button15.grid(row=6, column=0)
    button16 = Button(text="2", width=13, height=2, command=lambda: key_press('2', equation))
    button16.grid(row=6, column=1)
    button17 = Button(text="3", width=13, height=2, command=lambda: key_press('3', equation))
    button17.grid(row=6, column=2)
    button18 = Button(text="=", width=13, height=2, command=lambda: equal_press(equation))
    button18.grid(row=6, column=3)
    button19 = Button(text="n!", width=13, height=2, command=lambda: calculate_factorial(equation))
    button19.grid(row=4, column=3)
    button20 = Button(text="Factor", width=13, height=2, command=lambda: calculate_factor(equation))
    button20.grid(row=5, column=3)
    button21 = Button(text="0", width=13, height=2, command=lambda: key_press('0', equation))
    button21.grid(row=7, column=0)
    button22 = Button(text=",", width=13, height=2, command=lambda: key_press(',', equation))
    button22.grid(row=7, column=1)
    button23 = Button(text="gcd(a,b)", width=13, height=2, command=lambda: calc_gcd(equation))
    button23.grid(row=7, column=2)
    button24 = Button(text="lcm(a,b)", width=13, height=2, command=lambda: calc_lcm(equation))
    button24.grid(row=7, column=3)
    button25 = Button(text="bin(x)", width=13, height=2, command=lambda: convert_binary(equation))
    button25.grid(row=8, column=0)
    button26 = Button(text="oct(x)", width=13, height=2, command=lambda: convert_octal(equation))
    button26.grid(row=8, column=1)
    button27 = Button(text="hex(x)", width=13, height=2, command=lambda: convert_hexadecimal(equation))
    button27.grid(row=8, column=2)
    button28 = Button(text="C", width=13, height=2, command=lambda: clear_screen(equation))
    button28.grid(row=8, column=3)
    window.mainloop()
