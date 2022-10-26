#importando o "tkinter", que é o responsável pela interface gráfica, e "math" pelos cálculos
from tkinter import *
import math


#configurando janela
root = Tk()
root.title("Calculadora Científica")
root.resizable(False, False)
root.geometry("180x300")


#criando função para adicionar caracteres
def addNumber(label: Label, char):
    global atual_number

    if char != "." or "." not in atual_number:
        atual_number += char
        label.config(text=atual_number)
        label.grid(row=0, column=0)


#criando a "borracha"
def backspace(label: Label):
    global atual_number
    atual_number = atual_number[:-1]
    label.config(text=atual_number)


#criando função para criar botões mais facilmente
def button(text, vector, command=lambda: 0, bg="blue"):
    Button(
        root,
        text=text,
        bg=bg,
        fg="white",
        width=5,
        height=2,
        command=command
    ).grid(row=vector[0], column=vector[1])


#renderizando o "visor" da calculadora
equation = ""
operator = ""
label1 = Label(root, text=equation)
label1.grid(row=0, column=0)

atual_number = ""
label2 = Label(root, text=atual_number)
label2.grid(row=1, column=0)


#renderizando o "botões" da calculadora
button("BACKSPACE", [1,1], lambda: backspace(label2))

button("sen", [2,0])
button("cos", [2,1])
button("tan", [2,2])
button("/", [2,3])

button(7, [3,0], lambda: addNumber(label2, "7"))
button(8, [3,1], lambda: addNumber(label2, "8"))
button(9, [3,2], lambda: addNumber(label2, "9"))
button("*", [3,3])

button(4, [4,0], lambda: addNumber(label2, "4"))
button(5, [4,1], lambda: addNumber(label2, "5"))
button(6, [4,2], lambda: addNumber(label2, "6"))
button("-", [4,3])

button(1, [5,0], lambda: addNumber(label2, "1"))
button(2, [5,1], lambda: addNumber(label2, "2"))
button(3, [5,2], lambda: addNumber(label2, "3"))
button("+", [5,3])

button("√", [6,0])
button(0, [6,1], lambda: addNumber(label2, "0"))
button(".", [6,2], lambda: addNumber(label2, "."))
button("=", [6,3])


#iniciando looping
root.mainloop()
