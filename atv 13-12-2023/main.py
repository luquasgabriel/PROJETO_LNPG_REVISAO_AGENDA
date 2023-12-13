import tkinter as tk
from tkinter import *
import re


main = Tk()
main.title("agenda")


main.resizable(0, 0)

width = 400
height = 300
posx = main.winfo_screenwidth()/2 - (400/2)
posy = main.winfo_screenheight()/2 - (300/2)
main.geometry("%dx%d+%d+%d" %(width, height, posx, posy))

okay = ""

def verifica_campo():
    if not namecaixa.get() == "" or not emailcaixa.get() == "" or not telefonecaixa.get() == "":
        okay = ""
        ok.config(text=okay)
    if namecaixa.get() == "" or emailcaixa.get() == "" or telefonecaixa.get() == "":
        okay = "Todos os campos devem estar preenchidos"
        ok.config(text=okay)
    else:
        if not telefonecaixa.get().isdigit():
            okay = "O número de telefone deve conter apenas digitos!"
            ok.config(text=okay)
        
        if not "@" in emailcaixa.get() and "." not in emailcaixa.get():
            okay = "O e-mail deve conter um @ e um ."
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
