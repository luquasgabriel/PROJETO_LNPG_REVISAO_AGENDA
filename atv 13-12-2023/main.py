import tkinter as tk
from tkinter import *

main = Tk()
main.title("agenda")

okay = ""

def verifica_campo():
    if namecaixa.get() or emailcaixa.get() or telefonecaixa.get() == "":
        okay = "Todos os campos devem estar preenchidos"
        ok.config(text=okay)

        
agenda_title = Label(main, text = "Agenda de Contatos")
agenda_title.pack()

name = Label(main, 
    text = "Nome"

)
name.pack()
namecaixa = Entry(main,
    

)
namecaixa.pack()

email = Label(main, 
    text = "Email"

)
email.pack()
emailcaixa = Entry(main,
    

)
emailcaixa.pack()

telefone = Label(main, 
    text = "Telefone"

)
telefone.pack()
telefonecaixa = Entry(main,
    

)
telefonecaixa.pack()

Btn = Button(main, text= "Salvar contato", command=verifica_campo)
Btn.pack()


ok = Label(main, text = okay)
ok.pack()

main.mainloop()