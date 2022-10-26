#importando o "tkinter", que é o responsável pela interface gráfica, e "math" pelos cálculos
from tkinter import *
import math


#configurando janela
root = Tk()
root.title("Calculadora Científica")
root.resizable(False, False)
root.geometry("200x350")


#iniciando variáveis importantes
n1 = ""
operator = ""
n2 = ""


#função de criar botões mais facilmente
def button(text, position, command=lambda: 0, sizex=20):
    Button(
        root,
        text=text,
        bg="lightblue",
        padx=sizex,
        pady=14,
        command=command
    ).place(x=position[1], y=position[0])


#criando função de selecionar caractere
def char_selected(char):
    global n2

    if (char != ".") or ("." not in n2):
        n2 += str(char)
        label2.config(text=n2)


#criando função de selecionar operador
def operator_selected(oper):
    global operator, n1, n2

    operator = oper
    n1 = float(n2)
    n2 = ""
    
    if oper in ["sen", "cos", "tan", "√"]:
        return label1.config(text=f"{oper}{n1}")
    
    label1.config(text=f"{n1} {oper}")
    label2.config(text="")


#criando função que calcula
def calc():
    global n1, n2

    n1 = float(n1)
    n2 = float(n2)

    functions = {
        "sen": lambda: math.sin(n1),
        "cos": lambda: math.cos(n2),
        "tan": lambda: math.tan(n2),
        "+": lambda: n1 + n2,
        "-": lambda: n1 - n2,
        "*": lambda: n1 * n2,
        "/": lambda: n1 / n2,
        "√": lambda: n1 ** 0.5,
        "xʸ": lambda: n1 ** n2
    }


#renderizando "visor"
label1 = Label(
    root,
    text="",
)
label1.pack()

label2 = Label(
    root,
    text="",
)
label2.pack()


#renderizando botões
button("sen", [50,0], sizex=14)
button("cos", [50,50], sizex=14)
button("tan", [50,100], sizex=14)
button("/", [50,150], lambda: operator_selected("/"))

button(7, [100,0], lambda: char_selected(7))
button(8, [100,50], lambda: char_selected(8))
button(9, [100,100], lambda: char_selected(9))
button("*", [100,150], lambda: operator_selected("*"))

button(4, [150,0], lambda: char_selected(4))
button(5, [150,50], lambda: char_selected(5))
button(6, [150,100], lambda: char_selected(6))
button("-", [150,150], lambda: operator_selected("-"))

button(1, [200,0], lambda: char_selected(1))
button(2, [200,50], lambda: char_selected(2))
button(3, [200,100], lambda: char_selected(3))
button("+", [200,150], lambda: operator_selected("+"))

button("√", [250,0])
button(0, [250,50], lambda: char_selected(0))
button(".", [250,100], lambda: char_selected("."))
button("xʸ", [250,150], lambda: operator_selected("xʸ"), sizex=18)

button("=", [300,0], sizex=95)


#iniciando looping
root.mainloop()
