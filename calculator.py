import tkinter as tk
from tkinter.messagebox import showerror

elements = ['+','-','/','*']
root = tk.Tk()
root.title('My Calculator')

root.resizable(0,0)
root.config(bg='Black')


def make_equation(number):
    present = e.get()
    clear()
    e.insert(0,present+number)

def check(equation):
    global elements
    for i in elements:
        if i in equation:
            return False
    else:
        return True

def calculate():
    try:
        equation = e.get()
        if len(equation) == 0 or check(equation):
            showerror('Error','Nothing Found to calculate')
        else:
            calculated = eval(equation)
            clear()
            e.insert(0,str(calculated))
    except:
        showerror('Error!','Something went wrong!')

def clear():
    e.delete(0,tk.END)

#Main entry

e=tk.Entry(root,font=('Hevetica',17),borderwidth=0,bg='Black',fg='#39FF14')
e.grid(row=0,column=0,columnspan=3,padx=10,pady=20,ipady=20)

button_clear = tk.Button(root,text='C',command = clear,font=('Helvetica',12),padx=25,pady=25,bg='black',fg='#39FF14',borderwidth=0)

#row 1
button1 = tk.Button(root,text='1',command=lambda:make_equation('1'),font=('Helvetica',12),padx=25,pady=25,bg='Black',fg='#39FF14',borderwidth=0)
button1.grid(row=1,column=0,padx=2)

button2 = tk.Button(root,text='2',command = lambda:make_equation('2'),font=('Helvetica',12),padx=25,pady=25,bg='Black',fg='#39FF14',borderwidth=0)
button2.grid(row=1,column=1)

button3 = tk.Button(root,text='3',command = lambda:make_equation('3'),font=('Helvetica',12),padx=25,pady=25,bg='Black',fg='#39FF14',borderwidth=0)
button3.grid(row=1,column=2)

button_div = tk.Button(root,text='/',command = lambda:make_equation('/'),font=('Helvetica',12),padx=23,pady=25,bg='Black',fg='#39FF14',borderwidth=0)
button_div.grid(row=1,column=3)

#row 2
button4 = tk.Button(root,text='4',command=lambda:make_equation('4'),font=('Helvetica',12),padx=25,pady=25,bg='Black',fg='#39FF14',borderwidth=0)
button4.grid(row=2,column=0)

button5 = tk.Button(root,text='5',command=lambda:make_equation('5'),font=('Helvetica',12),padx=25,pady=25,bg='Black',fg='#39FF14',borderwidth=0)
button5.grid(row=2,column=1)

button6 = tk.Button(root,text='6',command=lambda:make_equation('6'),font=('Helvetica',12),padx=25,pady=25,bg='Black',fg='#39FF14',borderwidth=0)
button6.grid(row=2,column=2)

button_multi = tk.Button(root,text='*',command=lambda:make_equation('*'),font=('Helvetica',12),padx=24,pady=25,bg='Black',fg='#39FF14',borderwidth=0)
button_multi.grid(row=2,column=3)

#row 3
button7 = tk.Button(root,text='7',command=lambda:make_equation('7'),font=('Helvetica',12),padx=25,pady=25,bg='Black',fg='#39FF14',borderwidth=0)
button7.grid(row=3,column=0)

button8 = tk.Button(root,text='8',command=lambda:make_equation('8'),font=('Helvetica',12),padx=25,pady=25,bg='Black',fg='#39FF14',borderwidth=0)
button8.grid(row=3,column=1)

button9 = tk.Button(root,text='9',command=lambda:make_equation('9'),font=('Helvetica',12),padx=25,pady=25,bg='Black',fg='#39FF14',borderwidth=0)
button9.grid(row=3,column=2)

button_sub = tk.Button(root,text='-',command=lambda:make_equation('-'),font=('Helvetica',12),padx=27,pady=25,bg='Black',fg='#39FF14',borderwidth=0)
button_sub.grid(row=3,column=3)

#row 4
button_dot = tk.Button(root,text='.',command=lambda:make_equation('.'),font=('Helvetica',25),padx=20,pady=10,bg='Black',fg='#39FF14',borderwidth=0)
button_dot.grid(row=4,column=0)

button_zero = tk.Button(root,text='0',command=lambda:make_equation('0'),font=('Helvetica',12),padx=25,pady=15,bg='Black',fg='#39FF14',borderwidth=0)
button_zero.grid(row=4,column=1)

button_equate = tk.Button(root,text='=',command=calculate,font=('Helvetica',12),padx=25,pady=25,bg='#000000',fg='#39FF14',borderwidth=0)
button_equate.grid(row=4,column=2)

button_add = tk.Button(root,text='+',command=lambda:make_equation('+'),font=('Helvetica',12),padx=25,pady=25,bg='Black',fg='#39FF14',borderwidth=0)
button_add.grid(row=4,column=3)

root.mainloop()