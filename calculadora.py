#importando o "tkinter", que é o responsável pela interface gráfica, e "math" pelos cálculos
from tkinter import *
import math


#configurando janela
root = Tk()
root.title("Calculadora Científica")
root.resizable(False, False)
root.geometry("210x300")


#criando função que seleciona o operador
operator = ""

def select(oper):
    global operator
    operator = oper


#criando função que calcula
def calc():
    global operator

    operators_functions = {
        "+": lambda: n1.get() + n2.get(),
        "-": lambda:  n1.get() - n2.get(),
        "*": lambda:  n1.get() * n2.get(),
        "/": lambda:  n1.get() / n2.get(),
        "√": lambda: n1.get() ** 0.5,
        "^": lambda: n1.get() ** n2.get(),
        "sen": lambda: math.sin(n1.get()),
        "cos": lambda: math.cos(n1.get()),
        "tan": lambda: math.tan(n1.get()),
        "": ""
    }

    result.config(text=operators_functions[operator]())
    result.pack()


#renderizando input de N1
n1 = Entry(root).grid(row=0,column=0)


#renderizando operadores
Button(
    root,
    text="+",
    bg="blue",
    fg="white",
    command=lambda: select("+")
).grid(row=1,column=0)

Button(
    root,
    text="-",
    bg="blue",
    fg="white",
    command=lambda: select("-")
).grid(row=1,column=1)

Button(
    root,
    text="*",
    bg="blue",
    fg="white",
    command=lambda: select("*")
).grid(row=1,column=2)

Button(
    root,
    text="/",
    bg="blue",
    fg="white",
    command=lambda: select("/")
).grid(row=2,column=0)

Button(
    root,
    text="√",
    bg="blue",
    fg="white",
    command=lambda: select("√")
).grid(row=2,column=1)

Button(
    root,
    text="^",
    bg="blue",
    fg="white",
    command=lambda: select("^")
).grid(row=2,column=2)

Button(
    root,
    text="sen",
    bg="blue",
    fg="white",
    command=lambda: select("sen")
).grid(row=3,column=0)

Button(
    root,
    text="cos",
    bg="blue",
    fg="white",
    command=lambda: select("cos")
).grid(row=3,column=1)

Button(
    root,
    text="tan",
    bg="blue",
    fg="white",
    command=lambda: select("tan")
).grid(row=3,column=2)


#renderizando input de N2
n2 = Entry(root).grid(row=4,column=0)


#renderizando local de resposta
result = Label(root)


#renderizando botão para calcular
Button(
    root,
    text="Calcular",
    bg="blue",
    fg="white",
    command=lambda: calc()
).grid(row=5,column=0)


#iniciando looping
root.mainloop()