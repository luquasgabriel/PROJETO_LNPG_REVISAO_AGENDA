import tkinter as tk
from tkinter import *

path="lista.txt"

#janela
main = Tk()
main.title("agenda")
main.resizable(0, 0)
width = 400
height = 300
posx = main.winfo_screenwidth()/2 - (400/2)
posy = main.winfo_screenheight()/2 - (300/2)
main.geometry("%dx%d+%d+%d" %(width, height, posx, posy))

okay = ""

def salva_contato():
    file = open(path, 'a', encoding='utf-8')
    file.write(nomecaixa.get()+","+emailcaixa.get()+","+telefonecaixa.get()+"\n")



def mostra_contatos():
    global nomecaixa_
    contatos.delete(0,tk.END)
    with open(path, 'r', encoding='utf-8') as listadecontatos:
        for contato in listadecontatos:
            info = contato.strip().split("|")
            contato = map(str.strip, info)

            contatos.insert(tk.END, contato) 






def verifica_campo():
    if not nomecaixa.get() == "" or not emailcaixa.get() == "" or not telefonecaixa.get() == "":
        okay = ""
        ok.config(text=okay)
    if nomecaixa.get() == "" or emailcaixa.get() == "" or telefonecaixa.get() == "":
        okay = "Todos os campos devem estar preenchidos"
        ok.config(text=okay)
    else:
        if not telefonecaixa.get().isdigit():
            okay = "O número de telefone deve conter apenas digitos!"
            ok.config(text=okay)
        
        if not "@" in emailcaixa.get() and "." not in emailcaixa.get():
            okay = "O e-mail deve conter um @ e um ."
            ok.config(text=okay)
        else:
            okay = "Contato salvo com sucesso!"
            ok.config(text=okay)
            salva_contato()

     
agenda_title = Label(main, text = "Agenda de Contatos")
agenda_title.pack()

nome = Label(main, 
        text = "Nome"
)
nome.pack()

nomecaixa = Entry(main,
)
nomecaixa.pack()

nomecaixa_ = nomecaixa.get()


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
Btn.bind("<Button-1>", mostra_contatos)
Btn.pack()


ok = Label(main, text = okay)
ok.pack()

placeholder=Label(main, text="")
placeholder.pack()

contatos=Listbox(main)
contatos.pack()

main.mainloop()
