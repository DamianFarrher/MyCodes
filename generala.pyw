from tkinter import *
from tkinter import messagebox
import random

root=Tk()
root.title("Juego")
root.geometry("+450+200")
root.config(bd=10)

miFrame = Frame(root).grid(row=0,column=0)

default=root.cget('bg')

num1 = True
num2 = True
num3 = True
num4 = True
num5 = True

cantTurnos=0

primerLugar=0
ganador=''

def GAMEOVER():
	global primerLugar, ganador

	if primerLugar==1:
		ganador=jj1.get()
	elif primerLugar==2:
		ganador=jj2.get()
	elif primerLugar==3:
		ganador=jj3.get()
	elif primerLugar==4:
		ganador=jj4.get()

	tirar.config(text='FINALIZAR', command=GAMEOVER_)

def GAMEOVER_():
	messagebox.showinfo('GAMEOVER', 'La partida ha finalizado.\n\nGANADOR : [ {} ]'.format(ganador))
	root.destroy()





def botones(num):
	global num1
	global num2
	global num3
	global num4
	global num5

	if var1.get()!=0:
		if num==1:
			if num1:
				num1=False
				b1.config(bg="#444449", fg="white")
			else:
				num1=True
				b1.config(bg="white", fg="black")
		if num==2:
			if num2:
				num2=False
				b2.config(bg="#444449", fg="white")
			else:
				num2=True
				b2.config(bg="white", fg="black")
		if num==3:
			if num3:
				num3=False
				b3.config(bg="#444449", fg="white")
			else:
				num3=True
				b3.config(bg="white", fg="black")
		if num==4:
			if num4:
				num4=False
				b4.config(bg="#444449", fg="white")
			else:
				num4=True
				b4.config(bg="white", fg="black")
		if num==5:
			if num5:
				num5=False
				b5.config(bg="#444449", fg="white")
			else:
				num5=True
				b5.config(bg="white", fg="black")


i=0
def contadorTiros():
	global i
	i+=1
	tiros.set("Tiros: " + str(3-i))


def tirar():
	global num1
	global num2
	global num3
	global num4
	global num5
	global i
	global j

	if i!=3:
		if num1:
			var1.set(random.randint(1,6))
		if num2:
			var2.set(random.randint(1,6))
		if num3:
			var3.set(random.randint(1,6))
		if num4:
			var4.set(random.randint(1,6))
		if num5:
			var5.set(random.randint(1,6))

		contadorTiros()

	show_buttons(j)



j=1
def contadorJugador():
	global j, cantJugadores, cantTurnos

	if j<cantJugadores: j+=1
	else: j=1

	if j==1: cantTurnos+=1

	if cantTurnos==11:
		GAMEOVER()
	else:
		if j==1: j1.config(bg="#444449", fg="white")
		else: j1.config(bg=default, fg="black")
		
		if j==2: j2.config(bg="#444449", fg="white")
		else: j2.config(bg=default, fg="black")

		if j==3: j3.config(bg="#444449", fg="white")
		else: j3.config(bg=default, fg="black")

		if j==4: j4.config(bg="#444449", fg="white")
		else: j4.config(bg=default, fg="black")



def pasar():
	global i
	global num1
	global num2
	global num3
	global num4
	global num5

	i=0

	tiros.set("Tiros: 3")

	var1.set(0)
	var2.set(0)
	var3.set(0)
	var4.set(0)
	var5.set(0)
	
	num1=True
	num2=True
	num3=True
	num4=True
	num5=True

	b1.config(bg="white", fg="black")
	b2.config(bg="white", fg="black")
	b3.config(bg="white", fg="black")
	b4.config(bg="white", fg="black")
	b5.config(bg="white", fg="black")

	contadorJugador()
	show_buttons(None)


def limpiaNombres():
	SN=messagebox.askquestion("Borrar", "¿Borrar nombres?")
	if SN=="yes":
		jj1.set("Jugador 1")
		jj2.set("Jugador 2")
		jj3.set("Jugador 3")
		jj4.set("Jugador 4")

def info():
	messagebox.showinfo("Info", '''Generala versión 2.1\n\nFebrero 2020   -   Damian Farrher\n
________________________________________________________________\n

*NO CERRAR LA VENTANA DE PUNTOS PORQUE SINO NO FUNCIONA EL JUEGO. SI SE CIERRA, REINICIAR LA APLICACIÓN*


INSTRUCCIONES:

1️⃣  Seleccinar el número de jugadores. (Se puede nombrar a los jugadores una vez seleccionados [tocar en el nombre para editar])

2️⃣  Tirar los dados con el botón.

3️⃣  Seleccionar los números (de la izquierda) que se quieran conservar, el resto se tiran de nuevo en la próxima jugada.

4️⃣  A la derecha se muestran los puntos que suman la jugada correspondiente. Para pasar el turno al siguiente jugador, en alguna de las 3 tiradas se debe seleccionar una suma de puntos (a la derecha).

5️⃣  Jugar los turnos hasta que no queden jugadas.


JUEGOS / COMBINACIONES:

⭕ Full: 3 iguales y 2 iguales
⭕ Escalera: del 1 al 5, del 2 al 6 o del 3 al 6 y un 1
⭕ Poker: 4 iguales (+10 puntos si son 1s)
⭕ Generala: 5 iguales (+10 puntos si son 1s)

Todos suman +10 puntos si es servido (en el 1er turno)
''')

def exit():
	if messagebox.askquestion("Salir", "¿Salir de la aplicación?")=="yes":
		root.quit()

#------------------------------------------------------------

barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)

Opciones = Menu(barraMenu, tearoff=0)
Opciones.add_command(label="Borrar nombres", command=limpiaNombres)
barraMenu.add_cascade(label="Opciones", menu=Opciones)

barraMenu.add_command(label="Info", command=info)
barraMenu.add_command(label="Salir", command=exit)






#------------------------------------------------------------


var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()

tiros=StringVar()
tiros.set("Tiros: 3")


b1 = Button(miFrame, command=lambda:botones(1))
b1.config(width=5, textvariable=str(var1), bg="white")
b1.grid(row=1,column=1, pady=1)

b2 = Button(miFrame, command=lambda:botones(2))
b2.config(width=5, textvariable=str(var2), bg="white")
b2.grid(row=2,column=1, pady=1)

b3 = Button(miFrame, command=lambda:botones(3))
b3.config(width=5, textvariable=str(var3), bg="white")
b3.grid(row=3,column=1, pady=1)

b4 = Button(miFrame, command=lambda:botones(4))
b4.config(width=5, textvariable=str(var4), bg="white")
b4.grid(row=4,column=1, pady=1)

b5 = Button(miFrame, command=lambda:botones(5))
b5.config(width=5, textvariable=str(var5), bg="white")
b5.grid(row=5,column=1, pady=1)

tirar = Button(miFrame, command=tirar)
tirar.config(width=10, height=2, text='TIRAR', bg="#e24a63", fg="white")

NumJugadores = Label(miFrame, text='Número de jugadores:')
NumJugadores.grid(row=6,column=3, pady=1, columnspan=3)

dos_jugadores = Button(miFrame, text='2', command=lambda:cantidad_de_jugadores(2))
dos_jugadores.grid(row=7,column=3, pady=1, ipadx=10)
tres_jugadores = Button(miFrame, text='3', command=lambda:cantidad_de_jugadores(3))
tres_jugadores.grid(row=7,column=4, pady=1, ipadx=10)
cuatro_jugadores = Button(miFrame, text='4', command=lambda:cantidad_de_jugadores(4))
cuatro_jugadores.grid(row=7,column=5, pady=1, ipadx=10)


jj1=StringVar()
jj1.set("Jugador 1")
j1=Entry(miFrame)
j1.config(textvariable=jj1, bg="#444449", fg="white", justify=RIGHT, state=DISABLED)
j1.grid(row=1, column=3, sticky=E, columnspan=3)

jj2=StringVar()
jj2.set("Jugador 2")
j2=Entry(miFrame)
j2.config(textvariable=jj2, bg=default, justify=RIGHT, state=DISABLED)
j2.grid(row=2, column=3, sticky=E, columnspan=3)

jj3=StringVar()
jj3.set("Jugador 3")
j3=Entry(miFrame)
j3.config(textvariable=jj3, bg=default, justify=RIGHT, state=DISABLED)
j3.grid(row=3, column=3, sticky=E, columnspan=3)

jj4=StringVar()
jj4.set("Jugador 4")
j4=Entry(miFrame)
j4.config(textvariable=jj4, bg=default, justify=RIGHT, state=DISABLED)
j4.grid(row=4, column=3, sticky=E, columnspan=3)

labeltiros=Label(miFrame, textvariable=tiros)
labeltiros.config(fg=default)
labeltiros.grid(row=6, column=2, sticky=E)



#####    ####    ####   ######        ####                                                        
#    #  #    #  #    #    ##         #    #                                                                                                   
#    #  #    #  #    #    ##              #                              
#####   #    #  #    #    ##          ####                                     
#    #  #    #  #    #    ##         #                                         
#    #   ####    ####     ##         ######



otra_ventana = Toplevel(root)
otra_ventana.title("Puntos")
otra_ventana.geometry("+700+200")
otra_ventana.config(bd=10)


# lateral izquierdo 

Label(otra_ventana, text="1", justify=RIGHT, bg="white", width=5).grid(row=1, column=1, sticky=E, pady=3, padx=5)
Label(otra_ventana, text="2", justify=RIGHT, bg="white", width=5).grid(row=2, column=1, sticky=E, pady=3, padx=5)
Label(otra_ventana, text="3", justify=RIGHT, bg="white", width=5).grid(row=3, column=1, sticky=E, pady=3, padx=5)
Label(otra_ventana, text="4", justify=RIGHT, bg="white", width=5).grid(row=4, column=1, sticky=E, pady=3, padx=5)
Label(otra_ventana, text="5", justify=RIGHT, bg="white", width=5).grid(row=5, column=1, sticky=E, pady=3, padx=5)
Label(otra_ventana, text="6", justify=RIGHT, bg="white", width=5).grid(row=6, column=1, sticky=E, pady=3, padx=5)

Label(otra_ventana, text="full", justify=RIGHT, bg="white", width=5).grid(row=7, column=1, sticky=E, pady=3, padx=5)
Label(otra_ventana, text="escal.", justify=RIGHT, bg="white", width=5).grid(row=8, column=1, sticky=E, pady=3, padx=5)
Label(otra_ventana, text="poker", justify=RIGHT, bg="white", width=5).grid(row=9, column=1, sticky=E, pady=3, padx=5)

Label(otra_ventana, text="gen.", justify=RIGHT, bg="white", width=5).grid(row=10, column=1, sticky=E, pady=3, padx=5)
Label(otra_ventana, text="gen.2", justify=RIGHT, bg="white", width=5).grid(row=11, column=1, sticky=E, pady=3, padx=5)



#-------------------------------BOTONES----------------------------------

# comprueba la validez de: full / escalera / poker / generala / doble generala

def comprobar_juegos():
	global var1, var2, var3, var4, var5
	global i

	lista = [var1.get(), var2.get(), var3.get(), var4.get(), var5.get()]
	lista.sort()

	cantgeneralas = 0
	juegos = []  # almacena la validez de los distintos juegos mediante el propio número de cada uno

	pts=0

	#FULL
	if ((lista[0]==lista[1]==lista[2] != lista[3]==lista[4]) or (lista[0]==lista[1] != lista[2]==lista[3]==lista[4])):
		juegos.append(7)
		pts=20

		if i==1:
			pts+=10

		fulls.set(pts)
	else:
		fulls.set(pts)

	pts=0

	#ESCALERA
	if lista==[1,2,3,4,5] or lista==[2,3,4,5,6] or lista==[1,3,4,5,6]:
		juegos.append(8)
		pts=30
		
		if i==1:
			pts+=10
		
		escaleras.set(pts)

	else:
		escaleras.set(pts)

	pts=0

	#POKER
	if ((lista[0]==lista[1]==lista[2]==lista[3] != lista[4]) or (lista[0] != lista[1]==lista[2]==lista[3]==lista[4])):
		juegos.append(9)
		pts = 40
		if i==1:
			pts+=10
		if (lista[0]==lista[1]==lista[2]==lista[3]==1) or (1==lista[1]==lista[2]==lista[3]==lista[4]):
			pts+=10
		pokers.set(pts)
	else:
		pokers.set(pts)

	pts=0

	#GENERALA DOBLE
	if (lista[0] == lista[1] == lista[2] == lista[3] == lista[4]) and cantgeneralas==1:
		juegos.append(11)
		pts = 60
		if i==1:
			pts+=10
		if lista[0] == lista[1] == lista[2] == lista[3] == lista[4] == 1:
			pts+=10
		
		Dgeneralas.set(pts)
	else:
		Dgeneralas.set(pts)

	pts=0

	#GENERALA
	if lista[0] == lista[1] == lista[2] == lista[3] == lista[4] and cantgeneralas==0:
		juegos.append(10)
		cantgeneralas+=1
		pts = 60

		if i==1:
			pts+=10
		if lista[0] == lista[1] == lista[2] == lista[3] == lista[4] == 1:
			pts+=10
		
		generalas.set(pts)
	else:
		generalas.set(pts)

	pts = 0
	juegos = []



# suma los números individuales de los dados

def sumar_nums():
	global var1, var2, var3, var4, var5, seiss
	num1=0; num2=0; num3=0; num4=0; num5=0
	
	for i in range(1,7):
		if int(var1.get()) == i: num1=i
		if int(var2.get()) == i: num2=i
		if int(var3.get()) == i: num3=i
		if int(var4.get()) == i: num4=i
		if int(var5.get()) == i: num5=i

		if i == 1: unos.set(str(num1+num2+num3+num4+num5))
		if i == 2: doss.set(str(num1+num2+num3+num4+num5))
		if i == 3: tress.set(str(num1+num2+num3+num4+num5))
		if i == 4: cuatros.set(str(num1+num2+num3+num4+num5))
		if i == 5: cincos.set(str(num1+num2+num3+num4+num5))
		if i == 6: seiss.set(str(num1+num2+num3+num4+num5))

		num1=0; num2=0; num3=0; num4=0; num5=0


# muestra o no los botones según si la casilla esta vacía o no

def show_buttons(num):
	sumar_nums()
	comprobar_juegos()
	
	if num == 1:

		if _11.get()=="": bot11.grid(row=1, column=2)
		if _21.get()=="": bot21.grid(row=2, column=2)
		if _31.get()=="": bot31.grid(row=3, column=2)
		if _41.get()=="": bot41.grid(row=4, column=2)
		if _51.get()=="": bot51.grid(row=5, column=2)
		if _61.get()=="": bot61.grid(row=6, column=2)

		if _71.get()=="": botf1.grid(row=7, column=2)
		if _81.get()=="": bote1.grid(row=8, column=2)
		if _91.get()=="": botp1.grid(row=9, column=2)

		if _101.get()=="": botg1.grid(row=10, column=2)
		if _111.get()=="": botgg1.grid(row=11, column=2)

	elif num == 2:
		if _12.get()=="": bot12.grid(row=1, column=3)
		if _22.get()=="": bot22.grid(row=2, column=3)
		if _32.get()=="": bot32.grid(row=3, column=3)
		if _42.get()=="": bot42.grid(row=4, column=3)
		if _52.get()=="": bot52.grid(row=5, column=3)
		if _62.get()=="": bot62.grid(row=6, column=3)

		if _72.get()=="": botf2.grid(row=7, column=3)
		if _82.get()=="": bote2.grid(row=8, column=3)
		if _92.get()=="": botp2.grid(row=9, column=3)

		if _102.get()=="": botg2.grid(row=10, column=3)
		if _112.get()=="": botgg2.grid(row=11, column=3)

	elif num == 3:
		if _13.get()=="": bot13.grid(row=1, column=4)
		if _23.get()=="": bot23.grid(row=2, column=4)
		if _33.get()=="": bot33.grid(row=3, column=4)
		if _43.get()=="": bot43.grid(row=4, column=4)
		if _53.get()=="": bot53.grid(row=5, column=4)
		if _63.get()=="": bot63.grid(row=6, column=4)

		if _73.get()=="": botf3.grid(row=7, column=4)
		if _83.get()=="": bote3.grid(row=8, column=4)
		if _93.get()=="": botp3.grid(row=9, column=4)

		if _103.get()=="": botg3.grid(row=10, column=4)
		if _113.get()=="": botgg3.grid(row=11, column=4)
	
	elif num == 4:
		if _14.get()=="": bot14.grid(row=1, column=5)
		if _24.get()=="": bot24.grid(row=2, column=5)
		if _34.get()=="": bot34.grid(row=3, column=5)
		if _44.get()=="": bot44.grid(row=4, column=5)
		if _54.get()=="": bot54.grid(row=5, column=5)
		if _64.get()=="": bot64.grid(row=6, column=5)

		if _74.get()=="": botf4.grid(row=7, column=5)
		if _84.get()=="": bote4.grid(row=8, column=5)
		if _94.get()=="": botp4.grid(row=9, column=5)

		if _104.get()=="": botg4.grid(row=10, column=5)
		if _114.get()=="": botgg4.grid(row=11, column=5)

	# si no se le pasa un N° de jugador quiere decir que quien llamó la funcion fue la funcion "pass",
	# por lo tanto borra todos los botones que hay en pantalla
	else:
		try:
			bot11.grid_forget()
			bot12.grid_forget()
			bot13.grid_forget()
			bot14.grid_forget()
			bot21.grid_forget()
			bot22.grid_forget()
			bot23.grid_forget()
			bot24.grid_forget()
			bot31.grid_forget()
			bot32.grid_forget()
			bot33.grid_forget()
			bot34.grid_forget()
			bot41.grid_forget()
			bot42.grid_forget()
			bot43.grid_forget()
			bot44.grid_forget()
			bot51.grid_forget()
			bot52.grid_forget()
			bot53.grid_forget()
			bot54.grid_forget()
			bot61.grid_forget()
			bot62.grid_forget()
			bot63.grid_forget()
			bot64.grid_forget()
			botf1.grid_forget()
			botf2.grid_forget()
			botf3.grid_forget()
			botf4.grid_forget()
			bote1.grid_forget()
			bote2.grid_forget()
			bote3.grid_forget()
			bote4.grid_forget()
			botp1.grid_forget()
			botp2.grid_forget()
			botp3.grid_forget()
			botp4.grid_forget()
			botg1.grid_forget()
			botg2.grid_forget()
			botg3.grid_forget()
			botg4.grid_forget()
			botgg1.grid_forget()
			botgg2.grid_forget()
			botgg3.grid_forget()
			botgg4.grid_forget()
		except:
			pass


# al pulsar un boton se queda en pantalla asignando su valor a su label correspondiente

def btn(bot, lbl, num):
	if num==1:
		lbl.set(unos.get())
	if num==2:
		lbl.set(doss.get())
	if num==3:
		lbl.set(tress.get())
	if num==4:
		lbl.set(cuatros.get())
	if num==5:
		lbl.set(cincos.get())
	if num==6:
		lbl.set(seiss.get())
	if num==7:
		lbl.set(fulls.get())
	if num==8:
		lbl.set(escaleras.get())
	if num==9:
		lbl.set(pokers.get())
	if num==10:
		lbl.set(generalas.get())
	if num==11:
		lbl.set(Dgeneralas.get())

	cuenta_puntos()
	pasar()


# variables que almacenan los puntos por número o por juego

unos = StringVar(); unos.set("0")
doss = StringVar(); doss.set("0")
tress = StringVar(); tress.set("0")
cuatros = StringVar(); cuatros.set("0")
cincos = StringVar(); cincos.set("0")
seiss = StringVar(); seiss.set("0")
fulls = StringVar(); fulls.set("0")
escaleras = StringVar(); escaleras.set("0")
pokers = StringVar(); pokers.set("0")
generalas = StringVar(); generalas.set("0")
Dgeneralas = StringVar(); Dgeneralas.set("0")

#1
_11 = StringVar(); _11.set(""); l11 = Label(otra_ventana, textvariable=_11); l11.grid(row=1,column=2)
_12 = StringVar(); _12.set(""); l12 = Label(otra_ventana, textvariable=_12); l12.grid(row=1,column=3)
_13 = StringVar(); _13.set(""); l13 = Label(otra_ventana, textvariable=_13); l13.grid(row=1,column=4)
_14 = StringVar(); _14.set(""); l14 = Label(otra_ventana, textvariable=_14); l14.grid(row=1,column=5)
bot11 = Button(otra_ventana, textvariable=unos, width=4, command=lambda: btn(bot11, _11, 1))
bot12 = Button(otra_ventana, textvariable=unos, width=4, command=lambda: btn(bot12, _12, 1))
bot13 = Button(otra_ventana, textvariable=unos, width=4, command=lambda: btn(bot13, _13, 1))
bot14 = Button(otra_ventana, textvariable=unos, width=4, command=lambda: btn(bot14, _14, 1))

#2
_21 = StringVar(); _21.set(""); l21 = Label(otra_ventana, textvariable=_21); l21.grid(row=2,column=2)
_22 = StringVar(); _22.set(""); l22 = Label(otra_ventana, textvariable=_22); l22.grid(row=2,column=3)
_23 = StringVar(); _23.set(""); l23 = Label(otra_ventana, textvariable=_23); l23.grid(row=2,column=4)
_24 = StringVar(); _24.set(""); l24 = Label(otra_ventana, textvariable=_24); l24.grid(row=2,column=5)
bot21 = Button(otra_ventana, textvariable=doss, width=4, command=lambda: btn(bot21, _21, 2))
bot22 = Button(otra_ventana, textvariable=doss, width=4, command=lambda: btn(bot22, _22, 2))
bot23 = Button(otra_ventana, textvariable=doss, width=4, command=lambda: btn(bot23, _23, 2))
bot24 = Button(otra_ventana, textvariable=doss, width=4, command=lambda: btn(bot24, _24, 2))

#3
_31 = StringVar(); _31.set(""); l31 = Label(otra_ventana, textvariable=_31); l31.grid(row=3,column=2)
_32 = StringVar(); _32.set(""); l32 = Label(otra_ventana, textvariable=_32); l32.grid(row=3,column=3)
_33 = StringVar(); _33.set(""); l33 = Label(otra_ventana, textvariable=_33); l33.grid(row=3,column=4)
_34 = StringVar(); _34.set(""); l34 = Label(otra_ventana, textvariable=_34); l34.grid(row=3,column=5)
bot31 = Button(otra_ventana, textvariable=tress, width=4, command=lambda: btn(bot31, _31, 3))
bot32 = Button(otra_ventana, textvariable=tress, width=4, command=lambda: btn(bot32, _32, 3))
bot33 = Button(otra_ventana, textvariable=tress, width=4, command=lambda: btn(bot33, _33, 3))
bot34 = Button(otra_ventana, textvariable=tress, width=4, command=lambda: btn(bot34, _34, 3))

#4
_41 = StringVar(); _41.set(""); l41 = Label(otra_ventana, textvariable=_41); l41.grid(row=4,column=2)
_42 = StringVar(); _42.set(""); l42 = Label(otra_ventana, textvariable=_42); l42.grid(row=4,column=3)
_43 = StringVar(); _43.set(""); l43 = Label(otra_ventana, textvariable=_43); l43.grid(row=4,column=4)
_44 = StringVar(); _44.set(""); l44 = Label(otra_ventana, textvariable=_44); l44.grid(row=4,column=5)
bot41 = Button(otra_ventana, textvariable=cuatros, width=4, command=lambda: btn(bot41, _41, 4))
bot42 = Button(otra_ventana, textvariable=cuatros, width=4, command=lambda: btn(bot42, _42, 4))
bot43 = Button(otra_ventana, textvariable=cuatros, width=4, command=lambda: btn(bot43, _43, 4))
bot44 = Button(otra_ventana, textvariable=cuatros, width=4, command=lambda: btn(bot44, _44, 4))

#5
_51 = StringVar(); _51.set(""); l51 = Label(otra_ventana, textvariable=_51); l51.grid(row=5,column=2)
_52 = StringVar(); _52.set(""); l52 = Label(otra_ventana, textvariable=_52); l52.grid(row=5,column=3)
_53 = StringVar(); _53.set(""); l53 = Label(otra_ventana, textvariable=_53); l53.grid(row=5,column=4)
_54 = StringVar(); _54.set(""); l54 = Label(otra_ventana, textvariable=_54); l54.grid(row=5,column=5)
bot51 = Button(otra_ventana, textvariable=cincos, width=4, command=lambda: btn(bot51, _51, 5))
bot52 = Button(otra_ventana, textvariable=cincos, width=4, command=lambda: btn(bot52, _52, 5))
bot53 = Button(otra_ventana, textvariable=cincos, width=4, command=lambda: btn(bot53, _53, 5))
bot54 = Button(otra_ventana, textvariable=cincos, width=4, command=lambda: btn(bot54, _54, 5))

#6
_61 = StringVar(); _61.set(""); l61 = Label(otra_ventana, textvariable=_61); l61.grid(row=6,column=2)
_62 = StringVar(); _62.set(""); l62 = Label(otra_ventana, textvariable=_62); l62.grid(row=6,column=3)
_63 = StringVar(); _63.set(""); l63 = Label(otra_ventana, textvariable=_63); l63.grid(row=6,column=4)
_64 = StringVar(); _64.set(""); l64 = Label(otra_ventana, textvariable=_64); l64.grid(row=6,column=5)
bot61 = Button(otra_ventana, textvariable=seiss, width=4, command=lambda: btn(bot61, _61, 6))
bot62 = Button(otra_ventana, textvariable=seiss, width=4, command=lambda: btn(bot62, _62, 6))
bot63 = Button(otra_ventana, textvariable=seiss, width=4, command=lambda: btn(bot63, _63, 6))
bot64 = Button(otra_ventana, textvariable=seiss, width=4, command=lambda: btn(bot64, _64, 6))


#ful
_71 = StringVar(); _71.set(""); lf1 = Label(otra_ventana, textvariable=_71); lf1.grid(row=7,column=2)
_72 = StringVar(); _72.set(""); lf2 = Label(otra_ventana, textvariable=_72); lf2.grid(row=7,column=3)
_73 = StringVar(); _73.set(""); lf3 = Label(otra_ventana, textvariable=_73); lf3.grid(row=7,column=4)
_74 = StringVar(); _74.set(""); lf4 = Label(otra_ventana, textvariable=_74); lf4.grid(row=7,column=5)
botf1 = Button(otra_ventana, textvariable=fulls, width=4, command=lambda: btn(botf1, _71, 7))
botf2 = Button(otra_ventana, textvariable=fulls, width=4, command=lambda: btn(botf2, _72, 7))
botf3 = Button(otra_ventana, textvariable=fulls, width=4, command=lambda: btn(botf3, _73, 7))
botf4 = Button(otra_ventana, textvariable=fulls, width=4, command=lambda: btn(botf4, _74, 7))

#escalera
_81 = StringVar(); _81.set(""); le1 = Label(otra_ventana, textvariable=_81); le1.grid(row=8,column=2)
_82 = StringVar(); _82.set(""); le2 = Label(otra_ventana, textvariable=_82); le2.grid(row=8,column=3)
_83 = StringVar(); _83.set(""); le3 = Label(otra_ventana, textvariable=_83); le3.grid(row=8,column=4)
_84 = StringVar(); _84.set(""); le4 = Label(otra_ventana, textvariable=_84); le4.grid(row=8,column=5)
bote1 = Button(otra_ventana, textvariable=escaleras, width=4, command=lambda: btn(bote1, _81, 8))
bote2 = Button(otra_ventana, textvariable=escaleras, width=4, command=lambda: btn(bote2, _82, 8))
bote3 = Button(otra_ventana, textvariable=escaleras, width=4, command=lambda: btn(bote3, _83, 8))
bote4 = Button(otra_ventana, textvariable=escaleras, width=4, command=lambda: btn(bote4, _84, 8))

#poker
_91 = StringVar(); _91.set(""); lp1 = Label(otra_ventana, textvariable=_91); lp1.grid(row=9,column=2)
_92 = StringVar(); _92.set(""); lp2 = Label(otra_ventana, textvariable=_92); lp2.grid(row=9,column=3)
_93 = StringVar(); _93.set(""); lp3 = Label(otra_ventana, textvariable=_93); lp3.grid(row=9,column=4)
_94 = StringVar(); _94.set(""); lp4 = Label(otra_ventana, textvariable=_94); lp4.grid(row=9,column=5)
botp1 = Button(otra_ventana, textvariable=pokers, width=4, command=lambda: btn(botp1, _91, 9))
botp2 = Button(otra_ventana, textvariable=pokers, width=4, command=lambda: btn(botp2, _92, 9))
botp3 = Button(otra_ventana, textvariable=pokers, width=4, command=lambda: btn(botp3, _93, 9))
botp4 = Button(otra_ventana, textvariable=pokers, width=4, command=lambda: btn(botp4, _94, 9))

#generala
_101 = StringVar(); _101.set(""); lg1 = Label(otra_ventana, textvariable=_101); lg1.grid(row=10,column=2)
_102 = StringVar(); _102.set(""); lg2 = Label(otra_ventana, textvariable=_102); lg2.grid(row=10,column=3)
_103 = StringVar(); _103.set(""); lg3 = Label(otra_ventana, textvariable=_103); lg3.grid(row=10,column=4)
_104 = StringVar(); _104.set(""); lg4 = Label(otra_ventana, textvariable=_104); lg4.grid(row=10,column=5)
botg1 = Button(otra_ventana, textvariable=generalas, width=4, command=lambda: btn(botg1, _101, 10))
botg2 = Button(otra_ventana, textvariable=generalas, width=4, command=lambda: btn(botg2, _102, 10))
botg3 = Button(otra_ventana, textvariable=generalas, width=4, command=lambda: btn(botg3, _103, 10))
botg4 = Button(otra_ventana, textvariable=generalas, width=4, command=lambda: btn(botg4, _104, 10))

#generala2
_111 = StringVar(); _111.set(""); lgg1 = Label(otra_ventana, textvariable=_111); lgg1.grid(row=11,column=2)
_112 = StringVar(); _112.set(""); lgg2 = Label(otra_ventana, textvariable=_112); lgg2.grid(row=11,column=3)
_113 = StringVar(); _113.set(""); lgg3 = Label(otra_ventana, textvariable=_113); lgg3.grid(row=11,column=4)
_114 = StringVar(); _114.set(""); lgg4 = Label(otra_ventana, textvariable=_114); lgg4.grid(row=11,column=5)
botgg1 = Button(otra_ventana, textvariable=Dgeneralas, width=4, command=lambda: btn(botgg1, _111, 11))
botgg2 = Button(otra_ventana, textvariable=Dgeneralas, width=4, command=lambda: btn(botgg2, _112, 11))
botgg3 = Button(otra_ventana, textvariable=Dgeneralas, width=4, command=lambda: btn(botgg3, _113, 11))
botgg4 = Button(otra_ventana, textvariable=Dgeneralas, width=4, command=lambda: btn(botgg4, _114, 11))

#----------------------------------------------------------

# NOMBRES DE JUGADORES

Label(otra_ventana, textvariable=jj1, justify=RIGHT, width=7).grid(row=0, column=2, padx=3, pady=2)

Label(otra_ventana, textvariable=jj2, justify=RIGHT, width=7).grid(row=0, column=3, padx=3, pady=2)

nombre_jugador3 = Label(otra_ventana, textvariable=jj3, justify=RIGHT, width=7)
nombre_jugador3.grid(row=0, column=4, padx=3, pady=2)

nombre_jugador4 = Label(otra_ventana, textvariable=jj4, justify=RIGHT, width=7)
nombre_jugador4.grid(row=0, column=5, padx=3, pady=2)

#-------------------

# variables que almacenan el total de puntos por jugador

jjj1 = StringVar(); jjj1.set("0")
jjj2 = StringVar(); jjj2.set("0")
jjj3 = StringVar(); jjj3.set("0")
jjj4 = StringVar(); jjj4.set("0")

suma1=0; suma2=0; suma3=0; suma4=0

def cuenta_puntos():
	global suma1, suma2, suma3, suma4

	suma1=0; suma2=0; suma3=0; suma4=0

	if _11.get()=="": pass
	else: suma1+=int(_11.get())
	if _21.get()=="": pass
	else: suma1+=int(_21.get())
	if _31.get()=="": pass
	else: suma1+=int(_31.get())
	if _41.get()=="": pass
	else: suma1+=int(_41.get())
	if _51.get()=="": pass
	else: suma1+=int(_51.get())
	if _61.get()=="": pass
	else: suma1+=int(_61.get())
	if _71.get()=="": pass
	else: suma1+=int(_71.get())
	if _81.get()=="": pass
	else: suma1+=int(_81.get())
	if _91.get()=="": pass
	else: suma1+=int(_91.get())
	if _101.get()=="": pass
	else: suma1+=int(_101.get())
	if _111.get()=="": pass
	else: suma1+=int(_111.get())

	if _12.get()=="": pass
	else: suma2+=int(_12.get())
	if _22.get()=="": pass
	else: suma2+=int(_22.get())
	if _32.get()=="": pass
	else: suma2+=int(_32.get())
	if _42.get()=="": pass
	else: suma2+=int(_42.get())
	if _52.get()=="": pass
	else: suma2+=int(_52.get())
	if _62.get()=="": pass
	else: suma2+=int(_62.get())
	if _72.get()=="": pass
	else: suma2+=int(_72.get())
	if _82.get()=="": pass
	else: suma2+=int(_82.get())
	if _92.get()=="": pass
	else: suma2+=int(_92.get())
	if _102.get()=="": pass
	else: suma2+=int(_102.get())
	if _112.get()=="": pass
	else: suma2+=int(_112.get())

	if _13.get()=="": pass
	else: suma3+=int(_13.get())
	if _23.get()=="": pass
	else: suma3+=int(_23.get())
	if _33.get()=="": pass
	else: suma3+=int(_33.get())
	if _43.get()=="": pass
	else: suma3+=int(_43.get())
	if _53.get()=="": pass
	else: suma3+=int(_53.get())
	if _63.get()=="": pass
	else: suma3+=int(_63.get())
	if _73.get()=="": pass
	else: suma3+=int(_73.get())
	if _83.get()=="": pass
	else: suma3+=int(_83.get())
	if _93.get()=="": pass
	else: suma3+=int(_93.get())
	if _103.get()=="": pass
	else: suma3+=int(_103.get())
	if _113.get()=="": pass
	else: suma3+=int(_113.get())
	
	if _14.get()=="": pass
	else: suma4+=int(_14.get())
	if _24.get()=="": pass
	else: suma4+=int(_24.get())
	if _34.get()=="": pass
	else: suma4+=int(_34.get())
	if _44.get()=="": pass
	else: suma4+=int(_44.get())
	if _54.get()=="": pass
	else: suma4+=int(_54.get())
	if _64.get()=="": pass
	else: suma4+=int(_64.get())
	if _74.get()=="": pass
	else: suma4+=int(_74.get())
	if _84.get()=="": pass
	else: suma4+=int(_84.get())
	if _94.get()=="": pass
	else: suma4+=int(_94.get())
	if _104.get()=="": pass
	else: suma4+=int(_104.get())
	if _114.get()=="": pass
	else: suma4+=int(_114.get())

	jjj1.set(suma1)
	jjj2.set(suma2)
	jjj3.set(suma3)
	jjj4.set(suma4)

	quien_va_primero()


def quien_va_primero():
	global primerLugar
	
	if int(jjj1.get())>int(jjj2.get()) and int(jjj1.get())>int(jjj3.get()) and int(jjj1.get())>int(jjj4.get()):
		J1.config(bg="#f6d228", fg="black")
		primerLugar=1
	else:
		J1.config(bg="#444449", fg="white")

	if int(jjj2.get())>int(jjj1.get()) and int(jjj2.get())>int(jjj3.get()) and int(jjj2.get())>int(jjj4.get()):
		J2.config(bg="#f6d228", fg="black")
		primerLugar=2
	else:
		J2.config(bg="#444449", fg="white")
	
	if int(jjj3.get())>int(jjj2.get()) and int(jjj3.get())>int(jjj1.get()) and int(jjj3.get())>int(jjj4.get()):
		J3.config(bg="#f6d228", fg="black")
		primerLugar=3
	else:
		J3.config(bg="#444449", fg="white")
	
	if int(jjj4.get())>int(jjj2.get()) and int(jjj4.get())>int(jjj3.get()) and int(jjj4.get())>int(jjj1.get()):
		J4.config(bg="#f6d228", fg="black")
		primerLugar=4
	else:
		J4.config(bg="#444449", fg="white")


# PUNTOS TOTALES

J1 = Label(otra_ventana)
J1.config(textvariable=jjj1, justify=RIGHT, width=7, bg="#444449", fg="white")
J1.grid(row=12, column=2, padx=3, pady=2)

J2 = Label(otra_ventana)
J2.config(textvariable=jjj2, justify=RIGHT, width=7, bg="#444449", fg="white")
J2.grid(row=12, column=3, padx=3, pady=2)

J3 = Label(otra_ventana)
J3.config(textvariable=jjj3, justify=RIGHT, width=7, bg="#444449", fg="white")
J3.grid(row=12, column=4, padx=3, pady=2)

J4 = Label(otra_ventana)
J4.config(textvariable=jjj4, justify=RIGHT, width=7, bg="#444449", fg="white")
J4.grid(row=12, column=5, padx=3, pady=2)

#####

cantJugadores=4

def cantidad_de_jugadores(cant):
	global cantJugadores, nombre_jugador3, nombre_jugador4, J3, J4

	cantJugadores=cant

	if cant==2:
		j3.grid_forget()
		j4.grid_forget()

		nombre_jugador3.grid_forget()
		nombre_jugador4.grid_forget()

		J3.grid_forget()
		J4.grid_forget()

		j3.grid_forget()
		j4.grid_forget()
	
	if cant==3:
		j4.grid_forget()

		nombre_jugador4.grid_forget()

		J4.grid_forget()

		j4.grid_forget()

	tirar.grid(row=6, column=3, pady=1, columnspan=3)
	labeltiros.config(fg='black')

	NumJugadores.grid_forget()
	dos_jugadores.grid_forget()
	tres_jugadores.grid_forget()
	cuatro_jugadores.grid_forget()

	j1.config(state=NORMAL)
	j2.config(state=NORMAL)
	j3.config(state=NORMAL)
	j4.config(state=NORMAL)

#####



root.mainloop()