from tkinter import *
import tkinter
from tkinter import messagebox

val = ''
before = 0
operator = ''


def one():
    global val
    val = val + '1'
    value.set(val)
def two():
    global val
    val = val + '2'
    value.set(val)
def three():
    global val
    val = val + '3'
    value.set(val)
def four():
    global val
    val = val + '4'
    value.set(val)
def five():
    global val
    val = val + '5'
    value.set(val)
def six():
    global val
    val = val + '6'
    value.set(val)
def seven():
    global val
    val = val + '7'
    value.set(val)
def eight():
    global val
    val = val + '8'
    value.set(val)
def nine():
    global val
    val = val + '9'
    value.set(val)
def zero():
    global val 
    val = val + '0'
    value.set(val)
def plus():
    global before,val,operator
    before = int(val)
    operator = '+'
    val = val + '+'
    value.set(val)
def minus():
    global before,val,operator
    before = int(val)
    operator = '-'
    val = val + '-'
    value.set(val)
def multi():
    global before,val,operator
    before = int(val)
    operator = '*'
    val = val + '*'
    value.set(val)
def div():
    global before,val,operator
    before = int(val)
    operator = '/'
    val = val + '/'
    value.set(val)
def c():
    global before,val,operator
    before = 0
    operator = ''
    val = ''
    value.set(val)
def result():
    global before,val,operator
    val2 = val
    if operator == '+':
        x = int((val2.split('+')[1]))
        c = before + x 
        value.set(c)
        val = str(c)
    elif operator == '-':
        x = int((val2.split('-')[1]))
        c = before - x 
        value.set(c)
        val = str(c)
    elif operator == '*':
        x = int((val2.split('*')[1]))
        c = before * x 
        value.set(c)
        val = str(c)
    elif operator == '/':
        x = int((val2.split('/')[1]))
        if x == 0:
            messagebox.showerror('Error','Division by 0 not allowed')
            before = ''
            val = ''
            value.set(val)
        else:
            c = int(before/x) 
            value.set(c)
            val = str(c)
        

root = tkinter.Tk()
root.geometry('250x380')
root.resizable(0,0)
root.title('Calculator')
root.iconbitmap('D:\c.s12\img\calculator.png')

value = StringVar()
label1 = Label(root, text = 'label', anchor = SE ,height = 2, bd=5, font = ('Verdana', 20),textvariable = value).grid(row =1 ,column =1 ,columnspan =4)

fra1= Frame(root).grid(row = 2,column = 1,columnspan =4)
fra2= Frame(root).grid(row = 3,column = 1,columnspan =4)
fra3= Frame(root).grid(row = 4,column = 1,columnspan =4)
fra4= Frame(root).grid(row = 5,column = 1,columnspan =4)


button1 = Button(fra1,font = ('Verdana', 20), text = '1',command = one).grid(row = 2,column = 1,ipadx = 10,ipady =10)
button2 = Button(fra1,font = ('Verdana', 20), text = '2',command = two).grid(row = 2,column = 2,ipadx = 10,ipady =10)
button3 = Button(fra1,font = ('Verdana', 20), text = '3',command = three).grid(row = 2,column = 3,ipadx = 10,ipady =10)
buttonplus = Button(fra1,font = ('Verdana', 20), text = '+',command = plus).grid(row = 2,column = 4,ipadx = 10,ipady =10)

button4 = Button(fra2,font = ('Verdana', 20), text = '4',command = four).grid(row = 3,column = 1,ipadx = 10,ipady =10)
button5 = Button(fra2,font = ('Verdana', 20), text = '5',command = five).grid(row = 3,column = 2,ipadx = 10,ipady =10)
button6 = Button(fra2,font = ('Verdana', 20), text = '6',command = six).grid(row = 3,column = 3,ipadx = 10,ipady =10)
buttonminus = Button(fra2,font = ('Verdana', 20), text = '-',command = minus).grid(row = 3,column = 4,ipadx = 15,ipady =10)


button7 = Button(fra3,font = ('Verdana', 20), text = '7',command = seven).grid(row = 4,column = 1,ipadx = 10,ipady =10)
button8 = Button(fra3,font = ('Verdana', 20), text = '8',command = eight).grid(row = 4,column = 2,ipadx = 10,ipady =10)
button9 = Button(fra3,font = ('Verdana', 20), text = '9',command = nine).grid(row = 4,column = 3,ipadx = 10,ipady =10)
buttonmultiply = Button(fra3,font = ('Verdana', 20), text = '*',command = multi).grid(row = 4,column = 4,ipadx = 13,ipady =10)


buttonc = Button(fra4,font = ('Verdana', 20), text = 'c',command = c).grid(row = 5,column = 1,ipadx = 11,ipady =10)
button0 = Button(fra4,font = ('Verdana', 20), text = '0',command = zero).grid(row = 5,column = 2,ipadx = 10,ipady =10)
buttonequal = Button(fra4,font = ('Verdana', 20), text = '=',command = result).grid(row = 5,column = 3,ipadx = 7,ipady =10)
buttondivide = Button(fra4,font = ('Verdana', 20), text = '/',command = div).grid(row = 5,column = 4,ipadx = 15,ipady =10)



root.mainloop()