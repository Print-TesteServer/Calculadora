from tkinter import *
from tkinter import ttk

# Cores
co0 = '#000000' # PRETO
co1 = '#66245b' # ROXO
co2 = '#616382' # Azul cinzento
co3 = '#69a5a4' # Verde BEBE
co4 = '#a8c4a2' # Verde Claro
co5 = '#e5eaa4' # Amarelo fraco

# Interface
janela = Tk()
janela.title('Calculadora')
janela.geometry('340x500')
janela.configure(background=co0)
#janela.resizable(width=FALSE, height=FALSE)

# Configurando janela
frame_cima = Frame(janela, width=340, height=130, bg=co1, relief='flat')
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela,width=340, height=500, bg=co2, relief='flat')
frame_baixo.grid(row=1,column=0)

# Botões
b_1 = Button(frame_baixo, text="C", width=13, height=2,font=('Arial 12 bold'),bg=co3,relief='raised', overrelief='ridge')
b_1.place(x=0, y=0)

b_2 = Button(frame_baixo, text="%", width=9, height=2,font=('Arial 12 bold'),bg=co3,relief='raised', overrelief='ridge')
b_2.place(x=140, y=0)

b_3 = Button(frame_baixo, text="/", width=9, height=2,font=('Arial 12 bold'),bg=co3,relief='raised', overrelief='ridge')
b_3.place(x=240, y=0)

b_4 = Button(frame_baixo, text="*", width=9, height=2,font=('Arial 12 bold'),bg=co3,relief='raised', overrelief='ridge')
b_4.place(x=240, y=52)

b_5 = Button(frame_baixo, text="-", width=9, height=2,font=('Arial 12 bold'),bg=co3,relief='raised', overrelief='ridge')
b_5.place(x=240, y=104)

b_6 = Button(frame_baixo, text="+", width=9, height=2,font=('Arial 12 bold'),bg=co3,relief='raised', overrelief='ridge')
b_6.place(x=240, y=156)

b_7 = Button(frame_baixo, text="=", width=9, height=2,font=('Arial 12 bold'),bg=co3,relief='raised', overrelief='ridge')
b_7.place(x=240, y=208)

b_8 = Button(frame_baixo, text="9", width=12, height=2,font=('Arial 12 bold'),bg=co3,relief='raised', overrelief='ridge')
b_8.place(x=0, y=0)

b_9 = Button(frame_baixo, text="8", width=12, height=2,font=('Arial 12 bold'),bg=co3,relief='raised', overrelief='ridge')
b_9.place(x=0, y=0)

b_10 = Button(frame_baixo, text="7", width=12, height=2,font=('Arial 12 bold'),bg=co3,relief='raised', overrelief='ridge')
b_10.place(x=0, y=0)

b_11 = Button(frame_baixo, text="6", width=12, height=2,font=('Arial 12 bold'),bg=co3,relief='raised', overrelief='ridge')
b_11.place(x=0, y=0)

b_12 = Button(frame_baixo, text="5", width=12, height=2,font=('Arial 12 bold'),bg=co3,relief='raised', overrelief='ridge')
b_12.place(x=0, y=0)

b_13 = Button(frame_baixo, text="4", width=12, height=2,font=('Arial 12 bold'),bg=co3,relief='raised', overrelief='ridge')
b_13.place(x=0, y=0)

b_14 = Button(frame_baixo, text="3", width=12, height=2,font=('Arial 12 bold'),bg=co3,relief='raised', overrelief='ridge')
b_14.place(x=0, y=0)

b_15 = Button(frame_baixo, text="2", width=12, height=2,font=('Arial 12 bold'),bg=co3,relief='raised', overrelief='ridge')
b_15.place(x=0, y=0)

b_16 = Button(frame_baixo, text="1", width=12, height=2,font=('Arial 12 bold'),bg=co3,relief='raised', overrelief='ridge')
b_16.place(x=0, y=0)

b_17 = Button(frame_baixo, text="0", width=12, height=2,font=('Arial 12 bold'),bg=co3,relief='raised', overrelief='ridge')
b_17.place(x=0, y=0)


janela.mainloop()