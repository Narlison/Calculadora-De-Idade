from tkinter import *
from tkinter import ttk


#------importando calendario---------
from tkcalendar import Calendar,DateEntry

#-------importando dateutil---------
from dateutil.relativedelta import relativedelta
from datetime import *


#configuracoes de janela
janela = Tk()
janela.title("Calculadora De Idade")
janela.geometry("1000x2400")

#cores
cor1 = "#3b3b3b" #preto/leve
cor2 = "#333333" #preto/pesado
cor3 = "#ffffff" #branca
cor4 = "#FF7F00" #laranja
cor5 = "#FF0000" #vermelho



#criando frames
frame_cima = Frame(janela,width=1000,height=500,padx=0,pady=0,relief=FLAT,bg=cor2)
frame_cima.grid(column = 0,row=0)

frame_baixo = Frame(janela,width=1000,height=2400,pady=0,padx=0,relief=FLAT,bg=cor1)
frame_baixo.grid(column = 0,row = 1)





#--------------------textos----------------------
texto_calculadora = Label(frame_cima,text="CALCULADORA",width =25,height = 3,padx=3,relief=FLAT,anchor="center",font=("Ivi 15 bold"),bg=cor2,fg=cor3)

texto_calculadora.place(x=-100,y=60)

texto_calculadora2 = Label(frame_cima,text="DE IDADE",width =30,height = 1,padx=3,relief=FLAT,anchor="center",font=("Arial 18 bold"),bg=cor2,fg=cor4)

texto_calculadora2.place(x=-400,y=260)


#----------funcão calcular-------------
def calcular():
    inicial=calendar_1.get()
    terminal=calendar_2.get()
    
    
    #-------separando os valores--------
    mes_1,dia_1,ano_1 = [int(f)for f in inicial.split("/")]
    data_inicial = date(ano_1,mes_1,dia_1)
    
    #-------separando valores finais---------
    mes_2,dia_2,ano_2 = [int(f)for f in terminal.split("/")]
    data_final = date(ano_2,mes_2,dia_2)
    
    #-------relative----------------
    anos = relativedelta(data_inicial,data_final).years
    meses = relativedelta(data_inicial,data_final).months
    dias = relativedelta(data_inicial,data_final).days
    
    
    l_ano ["text"] = anos
    l_meses ["text"] = meses
    l_dias ["text"] = dias
    
    
    
    
    



inicial_data = Label(frame_baixo,text="Data De Nascimento",width = 20,height=-20,padx=0,relief=FLAT,anchor="center",font=("Arial 8 bold"),bg=cor1,fg=cor3)
inicial_data.place(x=400,y=80)

nasc_data = Label(frame_baixo,text="Data Atual",width = 20,height=-10,padx=0,relief=FLAT,anchor="center",font=("Arial 8 bold"),bg=cor1,fg=cor3)
nasc_data.place(x=400,y=160)

#------------calendario config----------------
calendar_1 = DateEntry(frame_baixo,width=10,bg="darkblue",fg=cor3,borderwidth=3,date_pattern = "mm/dd/y",y=2022)
calendar_1.place(x=30,y=160)

calendar_2 = DateEntry(frame_baixo,width=10,bg="darkblue",fg=cor3,borderwidth=10,date_pattern = 'mm/dd/y',y=2022)
calendar_2.place(x=30,y=80)

#------------Número Anos----------
l_ano = Label(frame_baixo,text="--",width=20,padx=0,relief=FLAT,anchor="center",font=("Arial 15 bold"),bg=cor1,fg=cor3)
l_ano.place(x=-360,y=600)

#----------anos texto----------------
l_anostxt = Label(frame_baixo,text="Anos",width=10,padx=0,relief=FLAT,anchor="center",font=("Arial 10"),bg=cor1,fg=cor5)
l_anostxt.place(x=-35,y=700)

#----------Numero Mês----------------
l_meses = Label(frame_baixo,text="--",width=2,padx=0,relief=FLAT,anchor="center",font=("Arial 15 bold"),bg=cor1,fg=cor3)
l_meses.place(x=400,y=600)

#---------Meses Texto-----------------
l_mesestxt = Label(frame_baixo,text="Meses",width=8,padx=0,relief=FLAT,anchor="center",font=("Arial 10"),bg=cor1,fg=cor5)
l_mesestxt.place(x=320,y=700)

#---------numero dias----------------
l_dias = Label(frame_baixo,text="--",width=6,padx=0,relief=FLAT,anchor="center",font=("Arial 15 bold"),bg=cor1,fg=cor3)
l_dias.place(x=660,y=600)

#--------Dias texto------------------
l_diastxt = Label(frame_baixo,text="Dias",width=6,padx=0,relief=FLAT,anchor="center",font=("Arial 10"),bg=cor1,fg=cor5)
l_diastxt.place(x=720,y=700)




#-------Botao de calcular-----------
botao = Button(frame_baixo,command=calcular,text="Calcular",width=17,relief="raised",overrelief="ridge",font=("Ivi 10 bold"),bg=cor1,fg=cor3)
botao.place(x=160,y=900)



janela.mainloop()
