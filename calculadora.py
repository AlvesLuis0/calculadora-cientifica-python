#importando o "tkinter", que é o responsável pela interface gráfica, e "math" pelos cálculos
from tkinter import *
import math


#configurando janela
root = Tk()
root.title("Calculadora Científica")
root.resizable(False, False)
root.geometry("200x400")


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

    if (char != ".") or ("." not in str(n2)):
        n2 += str(char)
        label2.config(text=n2)


#criando função de limpar a tela
def clear_view():
    global operator, n1, n2

    operator, n1, n2 = "", "", ""

    label1.config(text="")
    label2.config(text="")


#criando função de deletar um caractere
def backspace():
    global n2

    n2 = str(n2)[:-1]

    label2.config(text=n2)


#criando função de selecionar operador
def operator_selected(oper):
    global operator, n1, n2

    if n2 == "": return

    if (n1 != "") and (n2 != ""): calc()

    operator = oper
    n1 = n2
    n2 = ""
    
    if oper in ["sen", "cos", "tan", "√"]:
        return calc()
    
    elif oper == "xʸ":
        label1.config(text=f"{n1}^")
    
    else:
        label1.config(text=f"{n1} {oper}")
    
    label2.config(text="")


#criando função que calcula
def calc():
    global n1, n2, operator

    if n1 == "": return

    try:
        n1 = float(n1)
        n2 = float(n2)
    
    except: pass

    functions = {
        "sen": lambda: math.sin(n1),
        "cos": lambda: math.cos(n1),
        "tan": lambda: math.tan(n1),
        "+": lambda: n1 + n2,
        "-": lambda: n1 - n2,
        "*": lambda: n1 * n2,
        "/": lambda: n1 / n2,
        "√": lambda: n1 ** 0.5,
        "xʸ": lambda: n1 ** n2
    }

    try:
        result = functions[operator]()
        label1.config(text="")
        label2.config(text=result)

        n1 = ""
        n2 = result
    
    except: pass


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
button("C", [50,0], clear_view, sizex=50)
button("BACKSPACE", [50,100], backspace, sizex=15)

button("sen", [100,0], lambda: operator_selected("sen"), sizex=14)
button("cos", [100,50], lambda: operator_selected("cos"), sizex=14)
button("tan", [100,100], lambda: operator_selected("tan"), sizex=14)
button("/", [100,150], lambda: operator_selected("/"))

button(7, [150,0], lambda: char_selected(7))
button(8, [150,50], lambda: char_selected(8))
button(9, [150,100], lambda: char_selected(9))
button("*", [150,150], lambda: operator_selected("*"))

button(4, [200,0], lambda: char_selected(4))
button(5, [200,50], lambda: char_selected(5))
button(6, [200,100], lambda: char_selected(6))
button("-", [200,150], lambda: operator_selected("-"))

button(1, [250,0], lambda: char_selected(1))
button(2, [250,50], lambda: char_selected(2))
button(3, [250,100], lambda: char_selected(3))
button("+", [250,150], lambda: operator_selected("+"))

button("√", [300,0], lambda: operator_selected("√"))
button(0, [300,50], lambda: char_selected(0))
button(".", [300,100], lambda: char_selected("."))
button("xʸ", [300,150], lambda: operator_selected("xʸ"), sizex=18)

button("=", [350,0], calc, sizex=95)


#iniciando looping
root.mainloop()
