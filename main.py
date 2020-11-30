import re 
try:
    from tkinter import *
except ImportError: 
    raise ImportError("Se requiere la lib|reria Tkinter") 

root = Tk()
root.title('Calculadora modular')
root.geometry("312x372")
root.resizable(0, 0)

mod_expression = ""
input_mod = StringVar()
module = ""
expression = "" 
input_text = StringVar()
operator = ""

#Esta funcion me permite asignar el valor del modulo
def set_module():
    try:
        global module
        module = int (mod_field.get())
        if module > 0 :
            print(module)
        else:
            input_mod.set('Error')
            module = ""    
    except ValueError:
        input_mod.set('Error')

#Esta funcion me permite actualizar el input cada vez que se van agregando valores
def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

#Esta funcion limpia el input en caso de eliminar o saber un nuevo resultado
def bt_clear(): 
    global expression 
    global module
    expression = "" 
    module = ""
    input_text.set("")
    input_mod.set("")

#suma modular
def addition(num1, num2):
    global module    
    result = (int(num1) + int(num2)) % module
    return result

#resta modular
def subtraction(num1, num2):
    global module    
    result = (int(num1) - int(num2)) % module
    return result

#producto modular
def multiplication(num1, num2):
    global module    
    result = (int(num1) * int(num2)) % module
    return result

def inverse(num1, num2):
    global module   
    i = False
    for r in range(module):
        m = multiplication(num2, r)
        if m == 1:
            i = True
            print('El valor b tiene reciproco')
            break
    if i:
        return multiplication(num1, r)
    else:
        return -1


#division modular
def division(num1, num2):
    global module
    inv = inverse(num1, num2)
    if(inv != -1):
        return inv
        print('El valor tiene reciproco')
    else:
        return ('Valor 2 no reciproco')

def bt_equal():
    global expression
    global module
    result = ""
    if(module !=""):
        expr_op = re.split(r'\+|\-|\*|\/', expression)
        if(len(expr_op) == 2):
            if(int(expr_op[0]) > 0 and int(expr_op[1]) > 0):
                if '+' in expression:
                    result = addition(expr_op[0], expr_op[1])
                elif '-' in expression:
                    result = subtraction(expr_op[0], expr_op[1])
                elif '*' in expression:
                    result = multiplication(expr_op[0], expr_op[1])
                elif '/' in expression:
                    result = division(expr_op[0], expr_op[1])
                input_text.set(str(result))
                expression = ""
            else:
                input_text.set('Valores menores a 1')
        else:
            input_text.set('Ingresar 2 valores')
    else:
        input_text.set('No hay modulo')

#Frame de modulo Inicio
mod_frame = Frame(root, width=312, height=50, bd=0, highlightbackground="green", highlightcolor="green", highlightthickness=2)
mod_frame.pack(side=TOP)
#Frame de modulo fin
#Input de modulo Inicio
mod_field = Entry(mod_frame, font=('arial', 18, 'bold'), textvariable=input_mod, width=50, bg="#eee", bd=0, justify=RIGHT)
mod_field.grid(row=0, column=0)
mod_field.pack(ipady=10)
#Input de modulo Fin
#Frame de resultado Inicio
input_frame = Frame(root, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
input_frame.pack(side=TOP)
#Frame de resultado Fin
#Input de ingreso y resultado Inicio
input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, state=DISABLED, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)
#Input de ingreso y resultado Fin
#Frame Botones Inicio
btns_frame = Frame(root, width=312, height=272.5, bg="grey")
btns_frame.pack()
#Frame Botones Fin
#Primera columna Inicio
clear = Button(btns_frame, text = "C", fg = "black", width = 32, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
divide = Button(btns_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)
#Primera columna Fin
#Segunda columna Inicio
seven = Button(btns_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
eight = Button(btns_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
nine = Button(btns_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
multiply = Button(btns_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
#Segunda columna Fin
#Tercer columna Inicio
four = Button(btns_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
five = Button(btns_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
six = Button(btns_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
minus = Button(btns_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
#Tercer columna Fin
#Cuarta columna Inicio
one = Button(btns_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
two = Button(btns_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
three = Button(btns_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
plus = Button(btns_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
#Cuarta columna 
#Quinto columna Inicio
zero = Button(btns_frame, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
mods = Button(btns_frame, text = "mod", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: set_module()).grid(row = 4, column = 2, padx = 1, pady = 1)
equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)
#Quinti columna Fin
root.mainloop()