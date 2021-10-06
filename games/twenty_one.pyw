from tkinter import *
from tkinter import messagebox
import random
import time

root=Tk()
root.title("21 juego")
root.resizable(0,0)
root.geometry("+450+200")
root.config(bd=10)

miFrame=Frame(root)
miFrame.pack()

default=root.cget('bg')  #obtener código del color por defecto

diccCartas={1:True, 2:True, 3:True, 4:True, 5:True, 6:True, 7:True, 8:True, 9:True, 10:True, 11:True}

listaComodines = ['1','2','3','4','5','6','7','8','9','10','11','Ventaja','Barrido','Devolver','Cargar']
comodinesJug = []
contador_comodines=0

cartasBOT=[]
cartasJUGADOR=[]

j=1
finalizar=0

suma1=0
suma2=0

numero1=0

rondas = 1

#----------------------------------------------------------------------------------------------

######  #    #  #     #   ####  #####   ####   #     #  ######   ####                                                   
##      #    #  # #   #  #        #    #    #  # #   #  ##      #                               
####    #    #  #  #  #  #        #    #    #  #  #  #  ####     ####                                    
##      #    #  #   # #  #        #    #    #  #   # #  ##           #                        
##       ####   #     #   ####  #####   ####   #     #  ######   ####                           


#TURNOS
def contador_jugador(): 
	global j
	global contador_comodines

	contador_comodines=0

	if j==1: j=2
	elif j==2: j=1

	if j==1:  # Turno del bot

		lblBot.config(bg="#444449", fg="white")
		lblCB.config(bg="#444449", fg="white")
		lblJugador.config(bg=default, fg="black")
		lblCP.config(bg=default, fg="black")
		
		pedir.grid_forget()
		pasar.grid_forget()
		turnoBOTbutton.grid(row=1,column=1)

		B1.place_forget()
		B2.place_forget()
		B3.place_forget()
		B4.place_forget()
		B5.place_forget()
		B6.place_forget()
		B7.place_forget()
		B8.place_forget()
		B9.place_forget()
		B10.place_forget()
		B11.place_forget()
		BB.place_forget()
		BD.place_forget()
		BV.place_forget()
		BC.place_forget()


	else:  # Turno del jugador

		lblBot.config(bg=default, fg="black")
		lblCB.config(bg=default, fg="black")
		lblJugador.config(bg="#444449", fg="white")
		lblCP.config(bg="#444449", fg="white")
		
		turnoBOTbutton.grid_forget()
		pasar.grid(row=4, column=2, sticky=W, padx=5)
		pedir.grid(row=4, column=1, sticky=E, padx=5) 
		if contar_numeros(2)>20:
			pedir.config(state=DISABLED, bg=default, fg="black")
			
		B1.place(x=10,y=10)
		B2.place(x=55,y=10)
		B3.place(x=100,y=10)
		B4.place(x=10,y=40)
		B5.place(x=55,y=40)
		B6.place(x=100,y=40)
		B7.place(x=10,y=70)
		B8.place(x=55,y=70)
		B9.place(x=100,y=70)
		B10.place(x=10,y=100)
		B11.place(x=55,y=100)
		BB.place(x=10,y=130)
		BD.place(x=75,y=130)
		BV.place(x=10,y=160)
		BC.place(x=75,y=160)

#SUMA EL TOTAL DE PUNTOS DE AMBOS
def contar_numeros(who):  
	global suma1
	global suma2

	suma1=0
	suma2=0

	for i in cartasBOT:
		suma1+=i
	SumB.set("? + " + str(suma1-numero1) + " / 21")  

	for i in cartasJUGADOR:
		suma2+=i
	SP.set(str(suma2) + " / 21")

	# Devuelve la suma de puntos de 1 de los 2 jugadores (si es que se la piden)
	if who==1: 
		return suma1
	elif who==2:
		return suma2


#COMENZAR RONDA
def start():
	global diccCartas, cartasBOT, cartasJUGADOR
	global suma1
	global numero1
	global j

	num1=random.randint(1,11)
	num2=random.randint(1,11)
	num3=random.randint(1,11)
	num4=random.randint(1,11)

	while num2==num1:
		num2=random.randint(1,11)
	while num3==num1 or num3==num2:
		num3=random.randint(1,11)
	while num4==num1 or num4==num2 or num4==num3:
		num4=random.randint(1,11)

	diccCartas[num1]=False
	diccCartas[num2]=False
	diccCartas[num3]=False
	diccCartas[num4]=False

	numero1=num1

	CB.set("[ ? ]" + "[ " + str(num2) + " ]")
	cartasBOT.append(num1)
	cartasBOT.append(num2)

	CP.set("[ " + str(num3) + " ]" + "[ " + str(num4) + " ]")
	cartasJUGADOR.append(num3)
	cartasJUGADOR.append(num4)

	try:
		startbutton.config(state=DISABLED, bg=default, text="jugando...")
		pedir.config(state=NORMAL, bg="#34c51d", fg="white")
		pasar.config(state=NORMAL, bg="#cc1e1e", fg="white")
		turnoBOTbutton.config(state=NORMAL, bg="#e24a63", fg="white")

		RevelaBot.config(bg=default,fg='black')
		sumaBot.config(bg=default,fg='black')
		sumaJugador.config(bg=default,fg='black')
	except:
		pass

	labelBotJugador.place(x=152,y=165)
	puntosBot.place(x=190,y=150)
	puntosJug.place(x=240,y=150)
	texxtoo.place(x=150,y=10)
	scrollbar.place(in_=texxtoo, relx=1, relheight=1)

	contador_jugador()
	contar_numeros(0)


#REINICAR RONDA
def restart():
	global diccCartas
	global cartasBOT
	global cartasJUGADOR
	global j
	global finalizar
	global suma1
	global suma2
	global rondas

	diccCartas={1:True, 2:True, 3:True, 4:True, 5:True, 6:True, 7:True, 8:True, 9:True, 10:True, 11:True}
	cartasBOT=[]
	cartasJUGADOR=[]
		
	finalizar=0

	CB.set("")
	CP.set("")
	SumB.set("0")
	SP.set("0")

	suma1=0
	suma2=0

	RevelaBot.grid_forget()
	sumaBot.grid(row=1, column=4)
	
	rondas+=1

	texxtoo.delete(1.0, END)
	texxtoo.insert(END, 'Ronda N°' + str(rondas) + '\n')

	start()

#REVELA LA SUMA DE CARTAS DEL BOT AL FINAL DE LA RONDA
def vercartasBot():  
	global cartasBOT
	
	sumaaBot=0
	for i in cartasBOT:
		sumaaBot+=i

	RevBot.set(str(sumaaBot) + " / 21")
	RevelaBot.grid(row=1,column=4)

	sumaBot.grid_forget()


#COLOREA LOS PUNTOS DEL GANADOR AL FINAL DE LA RONDA
juegosB=0
juegosJ=0
def ganador(x): 

	global juegosJ, juegosB

	lblJugador.config(bg=default, fg="black")
	lblCP.config(bg=default, fg="black")
	lblBot.config(bg=default, fg="black")
	lblCB.config(bg=default, fg="black")

	if x==1:
		texxtoo.insert(END, 'Perdiste...\n')
		juegosB+=1
		RevelaBot.config(bg='#444449',fg='white')
	elif x==2:
		texxtoo.insert(END, 'GANASTE\n')
		juegosJ+=1
		sumaJugador.config(bg='#444449',fg='white')
	else:
		texxtoo.insert(END, 'Empate\n')

	if juegosJ==10:
		messagebox.showinfo('Fin del Juego','GANASTE LA PARTIDA')
		resetear_partida()
	elif juegosB==10:
		messagebox.showinfo('Fin del Juego','EL BOT GANÓ LA PARTIDA ...')
		resetear_partida()

	StringPuntosBot.set(str(juegosB))
	StringPuntosJug.set(str(juegosJ))


#VERIFICA QUIEN ES EL GANADOR
def quiengana(): 
	global suma1
	global suma2

	pedir.grid_forget()
	pasar.grid_forget()
	turnoBOTbutton.grid_forget()

	startbutton.config(state=NORMAL, bg="#e24a63", fg="white", text="Siguiente", command=restart)

	CB.set("")
	for i in cartasBOT:
		CB.set(CB.get() + "[ " + str(i) + " ]")

	vercartasBot()

	if suma1>21:
		if suma2<=21:
			ganador(2)
		else:
			ganador('e')

	elif suma2>21:
		if suma1<=21:
			ganador(1)
		else:
			ganador('e')
	
	elif suma1<suma2:
		ganador(2)
	elif suma1==suma2:
		ganador('e')
	else:
		ganador(1)


#JUGAR TURNO (PEDIR O PASAR)
def jugar(quehacer):
	global finalizar
	global j
	global cartas
	global numero1
	global contador_comodines

	if j==1:
		whoo="Bot"
	else:
		whoo="Jug"

	if quehacer=="pasar":#----------PASAR
		texxtoo.insert(END, whoo + ": Pasa el turno...\n")
		finalizar+=1
		if finalizar==2:
			texxtoo.insert(END, "\nFIN DEL JUEGO: ")
			quiengana()
		else:
			contador_jugador()
	
	else:#--------------------------PEDIR

		uno_cuatro = random.randint(1,4)
		if j==2 and uno_cuatro==4 and contador_comodines==0:  # 25% posibilidad de que Jug saque un comodín
			contador_comodines=1
			sacarComodin()
			activar_comodines()

		else:
			while True:
				num=random.randint(1,11)  #Se obtiene un número entre 1-11

				if diccCartas[num]:  #Si la carta está en el mazo...
					texxtoo.insert(END, whoo + ": Toma una carta [ " + str(num) + ' ]\n')
					diccCartas[num]=False  #Se elimina la carta del mazo				

					if j==1:
						cartasBOT.append(num)  #Se agrega al mazo de: BOT
						CB.set(CB.get() + "[ " + str(num) + " ]")
								
					elif j==2:
						cartasJUGADOR.append(num)  #Se agrega al mazo de: JUGADOR
						CP.set(CP.get() + "[ " + str(num) + " ]")
						
					if finalizar==0:
						contador_jugador()

					break

	if contar_numeros(2)>=21:
		pedir.config(state=DISABLED, bg=default, fg="black")
	else:
		pedir.config(state=NORMAL, bg="#34c51d", fg="white")

	contar_numeros(0)
	

#TURNO DEL BOT (AUTOMÁTICO)
def turnoBOT():
	if suma1<13:                   #Siempre saca si tiene <13
		jugar(1)
	
	elif suma1<17:
		prob=random.randint(1,5)   #4/5 que saque si tiene 13-16 (80%) 
		if prob==1:
			jugar("pasar")
		else:
			jugar(1)
	
	elif suma1<19: 
		prob=random.randint(1,3)   #1/3 que saque si tiene 17-18 (33%) 
		if prob==1:
			jugar(1)
		else:
			jugar("pasar")
	
	elif suma1<21:
		prob=random.randint(1,5)   #1/5 que saque si tiene 19-20 (20%) 
		if prob==1:
			jugar(1)
		else:
			jugar("pasar")

	else:
		jugar("pasar")             #Si tiene +21 pasa el turno


#RESETEAR PARTIDA
def resetear_partida():
	global juegosJ, juegosB, StringPuntosBot, StringPuntosJug, listaComodines, comodinesJug
	global diccCartas, cartasBOT, cartasJUGADOR, finalizar, rondas

	pedir.grid_forget()
	pasar.grid_forget()
	turnoBOTbutton.grid_forget()

	CB.set('')
	CP.set('')

	lblBot.config(bg=default, fg=default)
	lblCB.config(bg=default, fg=default)
	lblJugador.config(bg=default, fg=default)
	lblCP.config(bg=default, fg=default)

	sumaBot.config(bg=default, fg=default)
	RevelaBot.config(bg=default, fg=default)
	sumaJugador.config(bg=default, fg=default)

	juegosJ = 0
	juegosB = 0
	StringPuntosBot.set('0')
	StringPuntosJug.set('0')

	listaComodines = ['1','2','3','4','5','6','7','8','9','10','11','Ventaja','Barrido','Devolver','Cargar']
	comodinesJug = []

	diccCartas={1:True, 2:True, 3:True, 4:True, 5:True, 6:True, 7:True, 8:True, 9:True, 10:True, 11:True}
	cartasBOT=[]
	cartasJUGADOR=[]
			
	finalizar=0

	startbutton.config(text="JUGAR", bg="#e24a63", fg="white",state=NORMAL)

	B1.place_forget()
	B2.place_forget()
	B3.place_forget()
	B4.place_forget()
	B5.place_forget()
	B6.place_forget()
	B7.place_forget()
	B8.place_forget()
	B9.place_forget()
	B10.place_forget()
	B11.place_forget()
	BB.place_forget()
	BD.place_forget()
	BV.place_forget()
	BC.place_forget()

	labelBotJugador.place_forget()
	puntosBot.place_forget()
	puntosJug.place_forget()
	texxtoo.place_forget()
	scrollbar.place_forget()

	rondas=0
	texxtoo.delete(1.0, END)
	texxtoo.insert(END, 'NUEVA PARTIDA\n')
	texxtoo.insert(END, 'Ronda N°' + str(rondas) + '\n')

	sacarComodin()


def restartButton():
	x = messagebox.askquestion('Reiniciar','¿Reiniciar juego y puntuaciones?')
	if x=='yes':
		resetear_partida()

def infoButton():
	messagebox.showinfo('Información',
		'''Febrero 2020   -   Damian Farrher

_______________________________________________________________


INSTRUCCIONES:

♦️ El juego es a 10 rondas.
♦️ Gana la ronda quien llegue a 21 puntos, o el que más se le acerque sin pasarse.
♦️ Si se excede los 21, gana la ronda el oponente. En caso de que ambos oponentes se pasen, es empate.


COMODINES:

🃏 [numeros]: saca esa carta del mazo si se encuentra disponible*

🃏 Barrido: devuelve la última carta del oponente
🃏 Devolver: devuelve tu última carta
🃏 Ventaja: te entrga la mejor carta disponible en el mazo
🃏 Cargar: obliga al oponente a sacar una carta


* Solo existe una carta de cada número, si un número está en la mesa entonces no está en el mazo. Si se usa el comodín de un número que está en la mesa, se descarta.
''')
		
	
#----------------------------------------------------------------------------------------------

 #####   ####   #     #   ####   ####    #####  #     #  ######   ####                                 
##      #    #  # # # #  #    #  ##   #    #    # #   #  ##      #                              
##      #    #  #  #  #  #    #  ##   #    #    #  #  #  ####     ####                              
##      #    #  #     #  #    #  ##   #    #    #   # #  ##           #                          
 #####   ####   #     #   ####   ####    #####  #     #  ######   ####                           

miFrame2 = Frame(root)
miFrame2.config(bd=10, width=330, height=225)
miFrame2.grid_propagate(False)
miFrame2.pack(side=LEFT,padx=10)



B1 = Button(miFrame2)
B1.config(text='1',command=lambda:funciones_comodines('1'),width=3,state=DISABLED)
B2 = Button(miFrame2)
B2.config(text='2',command=lambda:funciones_comodines('2'),width=3,state=DISABLED)
B3 = Button(miFrame2)
B3.config(text='3',command=lambda:funciones_comodines('3'),width=3,state=DISABLED)
B4 = Button(miFrame2)
B4.config(text='4',command=lambda:funciones_comodines('4'),width=3,state=DISABLED)
B5 = Button(miFrame2)
B5.config(text='5',command=lambda:funciones_comodines('5'),width=3,state=DISABLED)
B6 = Button(miFrame2)
B6.config(text='6',command=lambda:funciones_comodines('6'),width=3,state=DISABLED)
B7 = Button(miFrame2)
B7.config(text='7',command=lambda:funciones_comodines('7'),width=3,state=DISABLED)
B8 = Button(miFrame2)
B8.config(text='8',command=lambda:funciones_comodines('8'),width=3,state=DISABLED)
B9 = Button(miFrame2)
B9.config(text='9',command=lambda:funciones_comodines('9'),width=3,state=DISABLED)
B10 = Button(miFrame2)
B10.config(text='10',command=lambda:funciones_comodines('10'),width=3,state=DISABLED)
B11 = Button(miFrame2)
B11.config(text='11',command=lambda:funciones_comodines('11'),width=3,state=DISABLED)

BB = Button(miFrame2)
BB.config(text='Barrido',command=lambda:funciones_comodines('Barrido'),width=7,state=DISABLED)
BD = Button(miFrame2)
BD.config(text='Devolver',command=lambda:funciones_comodines('Devolver'),width=7,state=DISABLED)

BV = Button(miFrame2)
BV.config(text='Ventaja',command=lambda:funciones_comodines('Ventaja'),width=7,state=DISABLED)
BC = Button(miFrame2)
BC.config(text='Cargar',command=lambda:funciones_comodines('Cargar'),width=7,state=DISABLED)



#TODAS LAS FUNCIONES PARA CADA COMODÍN
def funciones_comodines(c):
	global j
	global comodinesJug

	if c in ['1','2','3','4','5','6','7','8','9','10','11']:
		if diccCartas[int(c)]:

			diccCartas[int(c)]=False  #Se elimina la carta del mazo				
							 
			texxtoo.insert(END, 'Jug: Usa un comodín:\n    [ Toma la carta #' + str(c) +' ]\n')
			cartasJUGADOR.append(int(c))  #Se agrega al mazo de: JUGADOR
			CP.set(CP.get() + "[ " + c + " ]")

			comodinesJug.remove(c)
		else:
			texxtoo.insert(END, 'Esta carta no está en el mazo\n')
			comodinesJug.remove(c)

	

	elif c=='Barrido':

		texxtoo.insert(END, 'Jug: Usa un comodín:\n     [ Barrido ]')

		x = cartasBOT.pop()  #Se le saca la última carta a BOT
			
		y = CB.get().split('[')[1:-1]  
		z=''

		for i in y:
			z += ('[' + i)

		CB.set(z) 

		comodinesJug.remove(c)

		global finalizar
		finalizar=0


	elif c=='Devolver':

		texxtoo.insert(END, 'Jug: Usa un comodín:\n     [ Devolver ]')

		x = cartasJUGADOR.pop()  #Se le saca la última carta a JUGADOR
		diccCartas[x]=True  #Se agrega la carta al mazo
			
		y = CP.get().split('[')[1:-1]  
		z=''

		for i in y:
			z += ('[' + i)

		CP.set(z) 

		comodinesJug.remove(c)


	elif c=='Ventaja':
		
		texxtoo.insert(END, 'Jug: Usa un comodín:\n     [ Ventaja ]')

		x=21

		for i in cartasJUGADOR:  #Se saca el resto (lo que le falta para 21)
			x-=i

		while True:
			if x in diccCartas:  
				if diccCartas[x]==True:  
					texxtoo.insert(END, 'Jug: Toma la carta #' + str(x) + ' del mazo.\n')
					cartasJUGADOR.append(x)  #Se agrega al mazo de: JUGADOR
					CP.set(CP.get() + "[ " + str(x) + " ]")  

					break
				else: x-=1
			else: x-=1  
			if x<=0: break
		comodinesJug.remove(c)

	elif c=='Cargar':

		texxtoo.insert(END, 'Jug: Usa un comodín:\n     [ Cargar ]')

		while True:
			num=random.randint(1,11)  #Se obtiene un número entre 1-11

			if diccCartas[num]:  #Si la carta está en el mazo...
				diccCartas[num]=False  #Se elimina la carta del mazo				

				cartasBOT.append(num)  #Se agrega al mazo de: BOT
				CB.set(CB.get() + "[ " + str(num) + " ]")

				comodinesJug.remove(c)
				break



		comodinesJug.remove(c)

	activar_comodines()  
	contar_numeros(0)
	if contar_numeros(2)>20:
		pedir.config(state=DISABLED, bg=default, fg="black")
	else:
		pedir.config(state=NORMAL, bg="#34c51d", fg="white")


#ACTIVA O DESACTIVA LOS COMODINES CORRESPONDIENTES
def activar_comodines():
	global comodinesJug
	
	if '1' in comodinesJug: B1.config(state=NORMAL,bg='#444449',fg='white')
	else: B1.config(state=DISABLED,bg=default,fg='black')
	if '2' in comodinesJug: B2.config(state=NORMAL,bg='#444449',fg='white')
	else: B2.config(state=DISABLED,bg=default,fg='black')
	if '3' in comodinesJug: B3.config(state=NORMAL,bg='#444449',fg='white')
	else: B3.config(state=DISABLED,bg=default,fg='black')
	if '4' in comodinesJug: B4.config(state=NORMAL,bg='#444449',fg='white')
	else: B4.config(state=DISABLED,bg=default,fg='black')
	if '5' in comodinesJug: B5.config(state=NORMAL,bg='#444449',fg='white')
	else: B5.config(state=DISABLED,bg=default,fg='black')
	if '6' in comodinesJug: B6.config(state=NORMAL,bg='#444449',fg='white')
	else: B6.config(state=DISABLED,bg=default,fg='black')
	if '7' in comodinesJug: B7.config(state=NORMAL,bg='#444449',fg='white')
	else: B7.config(state=DISABLED,bg=default,fg='black')
	if '8' in comodinesJug: B8.config(state=NORMAL,bg='#444449',fg='white')
	else: B8.config(state=DISABLED,bg=default,fg='black')
	if '9' in comodinesJug: B9.config(state=NORMAL,bg='#444449',fg='white')
	else: B9.config(state=DISABLED,bg=default,fg='black')
	if '10' in comodinesJug: B10.config(state=NORMAL,bg='#444449',fg='white')
	else: B10.config(state=DISABLED,bg=default,fg='black')
	if '11' in comodinesJug: B11.config(state=NORMAL,bg='#444449',fg='white')
	else: B11.config(state=DISABLED,bg=default,fg='black')
	if 'Barrido' in comodinesJug: BB.config(state=NORMAL,bg='#444449',fg='white')
	else: BB.config(state=DISABLED,bg=default,fg='black')
	if 'Devolver' in comodinesJug: BD.config(state=NORMAL,bg='#444449',fg='white')
	else: BD.config(state=DISABLED,bg=default,fg='black')
	if 'Ventaja' in comodinesJug: BV.config(state=NORMAL,bg='#444449',fg='white')
	else: BV.config(state=DISABLED,bg=default,fg='black')
	if 'Cargar' in comodinesJug: BV.config(state=NORMAL,bg='#444449',fg='white')
	else: BC.config(state=DISABLED,bg=default,fg='black')


texxtoo = Text(miFrame2)
texxtoo.insert(END, 'NUEVA PARTIDA\n')
texxtoo.insert(END, 'Ronda N°' + str(rondas) + '\n')

#SACA UN COMODIN ALEATORIO 
def sacarComodin():
	global listaComodines, comodinesJug

	if listaComodines!=[]:
		while True:
			num = random.randint(0,13)
			try:
				comodinesJug.append(listaComodines[num])
				listaComodines.remove(listaComodines[num])
				break
			except: pass
		texxtoo.insert(END, 'Jug: Le toca un comodín:\n     [ #' + comodinesJug[-1] + ' ]\n')

	else:
		texxtoo.insert(END, 'No hay más comodines.\n')

	activar_comodines()

sacarComodin()



#----------------------------------------------------------------------------------------------


#####    ####   #     #  #####   ####   ##     ##      ####                             
##  ##  #    #  # #   #    #    #    #  ##     ##     #    #                         
#####   ######  #  #  #    #    ######  ##     ##     ######                                              
##      #    #  #   # #    #    #    #  ##     ##     #    #                             
##      #    #  #     #    #    #    #  #####  #####  #    #                        


#-------------------------------------------BARRA MENU---------------------------------------


barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

barraMenu.add_command(label="Reiniciar", command=restartButton)
barraMenu.add_command(label="Info", command=infoButton)



#-------------------------------------------ROOT---------------------------------------------

#---------------JUGADORES
lblBot=Label(miFrame)
lblBot.config(text="BOT", font=("", 10), fg=default)
lblBot.grid(row=1, column=1, padx=10, pady=5)

lblJugador=Label(miFrame)
lblJugador.config(text="JUGADOR", font=("", 10), fg=default)
lblJugador.grid(row=2, column=1, padx=10, pady=5)

#---------------CARTAS
CB=StringVar()
CP=StringVar()

RevBot=StringVar()
RevBot.set("")

RevelaBot=Label(miFrame)
RevelaBot.config(width=10, anchor=E, textvariable=RevBot)

SumB=StringVar()
SumB.set("")
SP=StringVar()
SP.set("")

lblCB=Label(miFrame)
lblCB.config(width=25, anchor=W, textvariable=CB)
lblCB.grid(row=1, column=2, columnspan=2)
lblCP=Label(miFrame)
lblCP.config(width=25, anchor=W, textvariable=CP)
lblCP.grid(row=2, column=2, columnspan=2)

sumaBot=Label(miFrame)
sumaBot.config(width=10, anchor=E, textvariable=SumB)
sumaBot.grid(row=1, column=4)
sumaJugador=Label(miFrame)
sumaJugador.config(width=10, anchor=E, textvariable=SP)
sumaJugador.grid(row=2, column=4)

#---------------BOTONES
pedir=Button(miFrame, text="Pedir carta", command=lambda:jugar(1))
pedir.config(state=DISABLED)


pasar=Button(miFrame, text="Pasar turno", command=lambda:jugar("pasar"))
pasar.config(state=DISABLED)

startbutton = Button(miFrame, command=start)
startbutton.config(width=9, height=3, text="JUGAR", bg="#e24a63", fg="white")
startbutton.grid(row=4, rowspan=2, column=4, pady=10)

turnoBOTbutton = Button(miFrame, command=turnoBOT)
turnoBOTbutton.config(width=7, height=1, text="BOT", state=DISABLED, font=("", 10))


#-------------miFrame2

StringPuntosBot = StringVar()
StringPuntosBot.set('0')
StringPuntosJug = StringVar()
StringPuntosJug.set('0')



labelBotJugador = Label(miFrame2)
labelBotJugador.config(text='BOT                :                JUGADOR')


puntosBot = Label(miFrame2)
puntosBot.config(textvariable=StringPuntosBot,font=('',25))


puntosJug = Label(miFrame2)
puntosJug.config(textvariable=StringPuntosJug,font=('',25))




texxtoo.config(width=30,height=13,state=NORMAL,font=('consolas',7), bg=default)

scrollbar = Scrollbar(miFrame2)
scrollbar.config(command=texxtoo.yview)

'x=305,y=10'




root.mainloop()
