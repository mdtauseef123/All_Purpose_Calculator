from tkinter import *
import normal_calc
import programmer_calc
import scientific_calc
window = Tk()
window.geometry("300x300")
window.title("Calculator")
window.minsize(width=300, height=300)
window.maxsize(width=300, height=300)


def change_page_normal(window_new):
    window_new.destroy()
    normal_calc.func()


def change_page_programmer(window_new):
    window_new.destroy()
    programmer_calc.func()


def change_page_scientific(window_new):
    window_new.destroy()
    scientific_calc.func()


Label(text="All Purpose Calculator").pack(padx=10, pady=10)
button1 = Button(text="Normal Calculator", command=lambda: change_page_normal(window))
button2 = Button(text="Programmer Calculator", command=lambda: change_page_programmer(window))
button3 = Button(text="Scientific Calculator", command=lambda: change_page_scientific(window))
button1.pack(padx=30, pady=10)
button2.pack(padx=30, pady=10)
button3.pack(padx=30, pady=10)
window.mainloop()
