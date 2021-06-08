import tkinter as tk
from math import *

#globally declaring the variable  
expression = "" 

#  Function to update expression in the text entry box 
def press(num): 
    #declaring global,to make changes to the variable
    global expression 
    #concatenation of string
    expression = expression + str(num) 
    # update the expression by using set method 
    equation.set(expression) 

# Function to evaluate the final expression 
def equalpress(): 
    try: 
        global expression 
        #eval function to evaluate the expression
        total = str(eval(expression)) 
        equation.set(total) 
        expression = total

    #if error is generated,then to handle it by except block  
    except:       
        equation.set(" error ") 
        expression = "" 

#function to clear entered number or operator
def clear():
    global expression
    a = len(expression)
    expression = expression[0:a-1]
    equation.set(expression) 

#function to clear the expression
def allclear(): 
    global expression 
    expression = "" 
    equation.set("") 

if __name__ == "__main__": 
#set the configurations of GUI window 
    calci = tk.Tk() 
    calci.configure(bg="white", padx=20, pady=20) 
    calci.title("Scientific Calculator") 
    calci.geometry("680x240") 

#creating the text Entry box for displaying 
    equation = tk.StringVar() 
    expression_field = tk.Entry(calci,bg="blue",fg="black",font=("helvetica",14,'bold'),borderwidth=5,relief="sunken",textvariable=equation) 
    expression_field.grid(row=0,column=0,columnspan=6, ipadx=70, padx=10) 
    equation.set('Enter your expression') 

#Create Buttons and placing at particular positions
    button1 = tk.Button(calci, text=' 1 ', bg='powder blue', fg='black',font=("helvetica",12,'bold'),command=lambda: press(1), height=1, width=7) 
    button1.grid(row=4, column=0,pady=1) 
  
    button2 = tk.Button(calci, text=' 2 ', bg='powder blue', fg='black',font=("helvetica",12,'bold'),command=lambda: press(2), height=1, width=7) 
    button2.grid(row=4, column=1,pady=1) 
  
    button3 = tk.Button(calci, text=' 3 ', bg='powder blue', fg='black',font=("helvetica",12,'bold'),command=lambda: press(3), height=1, width=7) 
    button3.grid(row=4, column=2,pady=1) 
  
    button4 = tk.Button(calci, text=' 4 ', bg='powder blue', fg='black',font=("helvetica",12,'bold'),command=lambda: press(4), height=1, width=7) 
    button4.grid(row=3, column=0,pady=1) 
  
    button5 = tk.Button(calci, text=' 5 ', bg='powder blue', fg='black',font=("helvetica",12,'bold'),command=lambda: press(5), height=1, width=7) 
    button5.grid(row=3, column=1,pady=1) 
  
    button6 = tk.Button(calci, text=' 6 ', bg='powder blue', fg='black',font=("helvetica",12,'bold'),command=lambda: press(6), height=1, width=7) 
    button6.grid(row=3, column=2) 
  
    button7 = tk.Button(calci, text=' 7 ', bg='powder blue', fg='black',font=("helvetica",12,'bold'),command=lambda: press(7), height=1, width=7) 
    button7.grid(row=2, column=0,pady=1) 
  
    button8 = tk.Button(calci, text=' 8 ', bg='powder blue', fg='black',font=("helvetica",12,'bold'),command=lambda: press(8), height=1, width=7) 
    button8.grid(row=2, column=1,pady=1) 
  
    button9 = tk.Button(calci, text=' 9 ', bg='powder blue', fg='black',font=("helvetica",12,'bold'),command=lambda: press(9), height=1, width=7) 
    button9.grid(row=2, column=2,pady=1) 
  
    button0 = tk.Button(calci, text=' 0 ', bg='powder blue', fg='black',font=("helvetica",12,'bold'),command=lambda: press(0), height=1, width=7) 
    button0.grid(row=5, column=1) 

#creating buttons for operations 
    plus = tk.Button(calci, text=' + ', fg='black', bg='powder blue',font=("helvetica",12,'bold'),command=lambda: press("+"), height=1, width=7) 
    plus.grid(row=1, column=3,pady=1) 
  
    minus = tk.Button(calci, text=' - ', fg='black', bg='powder blue',font=("helvetica",12,'bold'),command=lambda: press("-"), height=1, width=7)  
    minus.grid(row=2, column=3,pady=1) 
  
    multiply = tk.Button(calci, text=' * ', fg='black', bg='powder blue',font=("helvetica",12,'bold'),command=lambda: press("*"), height=1, width=7) 
    multiply.grid(row=3, column=3,pady=1) 
  
    divide = tk.Button(calci, text= chr(247) , fg='black', bg='powder blue',font=("helvetica",12,'bold'),command=lambda: press("/"), height=1, width=7) 
    divide.grid(row=4, column=3,pady=1) 
  
    equal = tk.Button(calci, text=' = ', fg='black', bg='powder blue',font=("helvetica",12,'bold'),command=equalpress, height=1, width=7) 
    equal.grid(row=5, column=3,pady=1) 
  
    allclear = tk.Button(calci, text='CE', fg='black', bg='powder blue',font=("helvetica",12,'bold'),command=allclear, height=1, width=7) 
    allclear.grid(row=1, column=1,pady=1) 

    clear = tk.Button(calci, text='C', fg='black', bg='powder blue',font=("helvetica",12,'bold'),command=clear, height=1, width=7) 
    clear.grid(row=1, column=0,pady=1) 

    Decimal= tk.Button(calci, text='.', fg='black', bg='powder blue',font=("helvetica",12,'bold'),command=lambda: press('.'), height=1, width=7) 
    Decimal.grid(row=5, column=0,pady=1) 

    btn_sq = tk.Button(calci,text="x²",width=7,height=1,bg="powder blue",font=("helvetica",12,'bold'),command=lambda: press("**2"))
    btn_sq.grid(row=1,column=4,pady=1)

    btn_Pi = tk.Button(calci,text="π",width=7,height=1,bg="powder blue",fg="black",font=("helvetica",12,'bold'),command=lambda: press('pi'))
    btn_Pi.grid(row=5,column=2,pady=1)

    btn_Mod = tk.Button(calci,text="%",width=7,height=1,bg="powder blue",font=("helvetica",12,'bold'),command= lambda : press("%"))
    btn_Mod.grid(row=1,column=2,pady=1)

    btn_E = tk.Button(calci,text="e",width=7,height=1,bg="powder blue",font=("helvetica",12,'bold'),command=lambda : press("e"))
    btn_E.grid(row=4,column=4,pady=1)

    btn_Exp = tk.Button(calci,text="e^×",width=7,height=1,bg="powder blue",font=("helvetica",12,'bold'),command=lambda : press("e**"))
    btn_Exp.grid(row=3,column=4,pady=1)

    btn_power = tk.Button(calci,text="x^y",width=7,height=1,bg="powder blue",font=("helvetica",12,'bold'),command=lambda :press("**"))
    btn_power.grid(row=2,column=4,pady=1)

    btn_fact = tk.Button(calci,text="n!",width=7,height=1,bg="powder blue",font=("helvetica",12,'bold'),command=lambda :press("factorial("))
    btn_fact.grid(row=5,column=4,pady=1)

    btn_bract = tk.Button(calci,text="(",width=7,height=1,bg="powder blue",font=("helvetica",12,'bold'),command=lambda :press("("))
    btn_bract.grid(row=3,column=5,pady=1) 

    btn_bract2 = tk.Button(calci,text=")",width=7,height=1,bg="powder blue",font=("helvetica",12,'bold'),command=lambda :press(")"))
    btn_bract2.grid(row=3,column=6,pady=1)

    btn_ndeg = tk.Button(calci,text="deg",width=7,height=1,bg="powder blue",font=("helvetica",12,'bold'),command=lambda: press("degrees("))
    btn_ndeg.grid(row=5,column=7,pady=1)

    btn_nrad = tk.Button(calci,text="rad",width=7,height=1,bg="powder blue",font=("helvetica",12,'bold'),command=lambda: press("radians("))
    btn_nrad.grid(row=5,column=6,pady=1)

    btn_inv = tk.Button(calci,text="1/x",width=7,height=1,bg="powder blue",font=("helvetica",12,'bold'),command=lambda: press("1/"))
    btn_inv.grid(row=4,column=5,pady=1)

    btn_sqrt = tk.Button(calci,text="√x",width=7,height=1,bg="powder blue",font=("helvetica",12,'bold'),command=lambda: press("sqrt("))
    btn_sqrt.grid(row=4,column=6,pady=1)

    btn_nthroot = tk.Button(calci,text="n√x",width=7,height=1,bg="powder blue",font=("helvetica",12,'bold'),command=lambda : press("**(1/"))
    btn_nthroot.grid(row=5,column=5,pady=1)

    btn_log10 = tk.Button(calci,text="log₁₀",width=7,height=1,bg="powder blue",font=("helvetica",12,'bold'),command=lambda: press("log10("))
    btn_log10.grid(row=3,column=7,pady=1)

    btn_ln = tk.Button(calci,text="ln",width=7,height=1,bg="powder blue",font=("helvetica",12,'bold'),command=lambda: press("log("))
    btn_ln.grid(row=4,column=7,pady=1)

#for Trignometric and Hyperbolic functions
    name_Inverse = 0
    name_Hyperbolic = 0

    def Inverse():
        if (name_Inverse%2 == 1) :
            func_trigInv()
        else :
            func_trig()

        if (name_Hyperbolic%2 == 1):
            func_HypInv()
        else :
            func_Hyperbolic()

    def func_trig():
        btn_sin = tk.Button(calci,text="sin",width=7,height=1,bg="powder blue",font=("helvetica",12,'bold'),command=lambda: press('sin('))
        btn_sin.grid(row=1,column=5,pady=1)
        btn_cos = tk.Button(calci,text="cos",width=7,height=1,bg="powder blue",font=("helvetica",12,'bold'),command=lambda: press('cos('))
        btn_cos.grid(row=1,column=6,pady=1)
        btn_tan = tk.Button(calci,text="tan",width=7,height=1,bg="powder blue",font=("helvetica",12,'bold'),command=lambda: press('tan('))
        btn_tan.grid(row=1,column=7,pady=1)
        global name_Inverse
        name_Inverse += 1

    def func_trigInv():
        btn_asin = tk.Button(calci,text="sin¯¹",width=7,height=1,bg="powder blue",font=("helvetica",12,'bold'),command=lambda: press('asin('))
        btn_asin.grid(row=1,column=5,pady=1)
        btn_acos = tk.Button(calci,text="cos¯¹",width=7,height=1,bg="powder blue",font=("helvetica",12,'bold'),command=lambda: press('acos('))
        btn_acos.grid(row=1,column=6,pady=1)
        btn_atan = tk.Button(calci,text="tan¯¹",width=7,height=1,bg="powder blue",font=("helvetica",12,'bold'),command=lambda: press('atan('))
        btn_atan.grid(row=1,column=7,pady=1)
        global name_Inverse
        name_Inverse += 1

    def func_Hyperbolic():
        btn_sinh = tk.Button(calci,text="sinh",width=7,height=1,bg="powder blue",font=("helvetica",12,'bold'),command=lambda: press('sinh('))
        btn_sinh.grid(row=2,column=5,pady=1)
        btn_cosh = tk.Button(calci,text="cosh",width=7,height=1,bg="powder blue",font=("helvetica",12,'bold'),command=lambda: press('cosh('))
        btn_cosh.grid(row=2,column=6,pady=1)
        btn_tanh = tk.Button(calci,text="tanh",width=7,height=1,bg="powder blue",font=("helvetica",12,'bold'),command=lambda: press('tanh('))
        btn_tanh.grid(row=2,column=7,pady=1)
        global name_Hyperbolic
        name_Hyperbolic += 1    

    def func_HypInv():
        btn_asinh = tk.Button(calci,text="sinh¯¹",width=7,height=1,bg="powder blue",font=("helvetica",12,'bold'),command=lambda: press('asinh('))
        btn_asinh.grid(row=2,column=5,pady=1)
        btn_acosh = tk.Button(calci,text="cosh¯¹",width=7,height=1,bg="powder blue",font=("helvetica",12,'bold'),command=lambda: press('acosh('))
        btn_acosh.grid(row=2,column=6,pady=1)
        btn_atanh = tk.Button(calci,text="tanh¯¹",width=7,height=1,bg="powder blue",font=("helvetica",12,'bold'),command=lambda: press('atanh('))
        btn_atanh.grid(row=2,column=7,pady=1)
        global name_Hyperbolic
        name_Hyperbolic += 1    

    #To change the functions to inverse functions
    btn_Inverse = tk.Button(calci,text="Inv",width=7,height=1,bg="powder blue",font=("helvetica",12,'bold'),command=Inverse)
    btn_Inverse.grid(row=0,column=7,pady=1)
    
    #calling the function to initial place the buttons.
    func_trig()
    func_Hyperbolic()

    # start the GUI 
    calci.mainloop() 