from tkinter import *
import tkinter
from datetime import datetime

#cores
cor1 = "#faf5f5" #branco
cor2 = "#0a0a0a" #preto
cor3 = "#b4b2b8" #cinza
cor4 = "#7847ff" #roxo
cor5 = "#f2ef29" #amarelo
cor6 = "#f7023c" #rosa

fundo = cor2
cor = cor1

janela=Tk()
janela.title("")
janela.geometry("440x180")
janela.resizable(width=FALSE, height=FALSE)
janela.configure(bg=cor2)

def relogio():
   tempo = datetime.now()
   hora = tempo.strftime("%H:%M:%S")
   dia_semana = tempo.strftime("&A")
   dia = tempo.day
   mes = tempo.strftime("%b")
   ano = tempo.strftime("%Y")
   
   li.config(text=hora)
   li.after(200, relogio)
   l2.config(text=dia_semana + "  " + str(dia) + "/" + str(mes) + "/" + str(ano))
   
li = Label (janela,font=("Arial 80"), text="",bg=fundo,fg=cor)
li.grid(row=0, column=0, sticky=NW, padx=5)

l2 = Label (janela,font=("Arial 20"), text="",bg=fundo,fg=cor)
l2.grid(row=1, column=0, sticky=NW, padx=5)

relogio()
janela.mainloop()
