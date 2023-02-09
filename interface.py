# Importação
from tkinter import *

# Cores
co0 = '#000000' # PRETO
co1 = '#66245b' # ROXO
co2 = '#00A2AB' # Azul
co3 = '#C9D4D3' # Cinza
co4 = '#a8c4a2' # Verde Claro
co5 = '#F2AE00' # Amarelo
co6 = '#FFFFFF' # Branco

# Interface
janela = Tk()
janela.title('Calculadora')
janela.geometry('340x360')
janela.configure(background=co0)
janela.resizable(width=FALSE, height=FALSE)

# Configurando janela
frame_cima = Frame(janela, width=340, height=100, bg=co2, relief='flat')
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela,width=340, height=360, bg=co3, relief='flat')
frame_baixo.grid(row=1,column=0)

# Criando Label
valor_texto = StringVar()

app_label = Label(frame_cima, textvariable=valor_texto, width=20, height=3, relief=FLAT, anchor='e', justify=RIGHT,
                  font=('Ivy 20'),bg=co2, fg=co6)
app_label.place(x=0, y=0)

# Variaveis
todos_valores = ""
# Função
def entrar_valores(event):
    global todos_valores

    todos_valores = todos_valores + str(event)
    valor_texto.set(todos_valores)  # Passando Valor para Tela

def calcular():
    global todos_valores

    resultado = eval(todos_valores)
    valor_texto.set(resultado)  # Passando Valor para Tela

def clear():
    global todos_valores

    todos_valores = ""
    valor_texto.set("")

# Botões
b_1 = Button(frame_baixo, command= clear, text="C", width=15, height=2, font=('Arial 12 bold'), bg=co3, relief='raised', overrelief='ridge')
b_1.place(x=0, y=0)
b_2 = Button(frame_baixo, command=lambda: entrar_valores('%'), text="%", width=8, height=2,font=('Arial 12 bold'), bg=co3,
             relief='raised', overrelief='ridge')
b_2.place(x=160, y=0)
b_3 = Button(frame_baixo, command=lambda: entrar_valores('/'), text="/", width=8, height=2,font=('Arial 13 bold'), bg=co5, fg=co6, relief='raised', overrelief='ridge')
b_3.place(x=250, y=0)

b_4 = Button(frame_baixo,command=lambda: entrar_valores('*'), text="*", width=8, height=2, font=('Arial 13 bold'), bg=co5, fg=co6, relief='raised', overrelief='ridge')
b_4.place(x=250, y=52)
b_5 = Button(frame_baixo, command=lambda: entrar_valores('-'),  text="-", width=8, height=2, font=('Arial 13 bold'), bg=co5, fg=co6, relief='raised', overrelief='ridge')
b_5.place(x=250, y=104)
b_6 = Button(frame_baixo,command=lambda: entrar_valores('+'), text="+", width=8, height=2, font=('Arial 13 bold'), bg=co5, fg=co6, relief='raised', overrelief='ridge')
b_6.place(x=250, y=156)
b_7 = Button(frame_baixo, command= calcular, text="=", width=8, height=2, font=('Arial 13 bold'), bg=co5, fg=co6, relief='raised', overrelief='ridge')
b_7.place(x=250, y=208)

b_8 = Button(frame_baixo, command=lambda: entrar_valores('9'), text="9", width=8, height=2, font=('Arial 12 bold'), bg=co3, relief='raised', overrelief='ridge')
b_8.place(x=160, y=52)
b_9 = Button(frame_baixo, command=lambda: entrar_valores('8'), text="8", width=7, height=2, font=('Arial 12 bold'), bg=co3, relief='raised', overrelief='ridge')
b_9.place(x=80, y=52)
b_10 = Button(frame_baixo, command=lambda: entrar_valores('7'), text="7", width=7, height=2, font=('Arial 12 bold'), bg=co3, relief='raised', overrelief='ridge')
b_10.place(x=0, y=52)
b_11 = Button(frame_baixo, command=lambda: entrar_valores('6'), text="6", width=8, height=2, font=('Arial 12 bold'), bg=co3, relief='raised', overrelief='ridge')
b_11.place(x=160, y=104)
b_12 = Button(frame_baixo, command=lambda: entrar_valores('5'), text="5", width=7, height=2, font=('Arial 12 bold'), bg=co3, relief='raised', overrelief='ridge')
b_12.place(x=80, y=104)
b_13 = Button(frame_baixo, command=lambda: entrar_valores('4'), text="4", width=7, height=2, font=('Arial 12 bold'), bg=co3, relief='raised', overrelief='ridge')
b_13.place(x=0, y=104)
b_14 = Button(frame_baixo, command=lambda: entrar_valores('3'), text="3", width=8, height=2, font=('Arial 12 bold'), bg=co3, relief='raised', overrelief='ridge')
b_14.place(x=160, y=156)
b_15 = Button(frame_baixo, command=lambda: entrar_valores('2'), text="2", width=7, height=2, font=('Arial 12 bold'),bg=co3, relief='raised', overrelief='ridge')
b_15.place(x=80, y=156)
b_16 = Button(frame_baixo, command=lambda: entrar_valores('1'), text="1", width=7, height=2, font=('Arial 12 bold'), bg=co3, relief='raised', overrelief='ridge')
b_16.place(x=0, y=156)

b_17 = Button(frame_baixo, command=lambda: entrar_valores('0'), text="0", width=15, height=2, font=('Arial 12 bold'), bg=co3, relief='raised', overrelief='ridge')
b_17.place(x=0, y=208)
b_18 = Button(frame_baixo, command=lambda: entrar_valores('.'), text=".", width=8, height=2, font=('Arial 12 bold'), bg=co3, relief='raised', overrelief='ridge')
b_18.place(x=160, y=208)

# janela.mainloop()