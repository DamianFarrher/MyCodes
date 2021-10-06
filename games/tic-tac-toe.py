from tkinter import *

#VARIABLES
root = Tk()
root.config(bd=10)
root.title('Tik-Tak-Toe')
default=root.cget('bg')
botones = []
turno = 'x'
#Color oscuro: #444449


#FUNCIONES
def click(boton):
	global turno
	if boton['text'] != '':
		pass
	else:
		if turno=='x': 
			boton.config(bg='#ffb1b1', text='X')
			turno='o'
		elif turno=='o': 
			boton.config(bg='#b1baff', text='O')
			turno='x'
	revisar()

def revisar():
	
	if   (botones[0]['text'] == botones[4]['text'] == botones[8]['text']): ganador(botones[0], botones[4], botones[8])
	elif (botones[2]['text'] == botones[4]['text'] == botones[6]['text']): ganador(botones[2], botones[4], botones[6])
	elif (botones[0]['text'] == botones[1]['text'] == botones[2]['text']): ganador(botones[0], botones[1], botones[2])
	elif (botones[3]['text'] == botones[4]['text'] == botones[5]['text']): ganador(botones[3], botones[4], botones[5])
	elif (botones[6]['text'] == botones[7]['text'] == botones[8]['text']): ganador(botones[6], botones[7], botones[8])
	else:
		for i in range(3):
			if (botones[i]['text'] == botones[i+3]['text'] == botones[i+6]['text']):ganador(botones[i], botones[i+3], botones[i+6])

def ganador(b1,b2,b3):
	if b1['text']=='':
		pass
	else:
		print('GANADOR: ' + b1['text'])
		for i in range(9):
			botones[i].config(state=DISABLED)

def reiniciar():
	for i in range(9):
		botones[i].config(text='', bg=default, state=NORMAL)


#INTERFAZ
'''
miFrame = Frame(root)
miFrame.pack()

marcadorX = Label(miFrame)
marcadorX.config(text='X', font=('consolas', 12))
marcadorX.place(relx = 0, rely = 0, anchor = CENTER)

marcador = Label(miFrame)
marcador.config(text='0 : 0', font=('consolas', 20))
marcador.place(relx = 0.5, rely = 0.5, anchor = CENTER)

marcadorO = Label(miFrame)
marcadorO.config(text='O', font=('consolas', 12))
marcadorX.place(relx = 0.5, rely = 0.5, anchor = CENTER)
'''

miFrame2 = Frame(root)
miFrame2.pack()

boton1 = Button(miFrame2)
boton1.config(width=5, height=2, font = ('Berlin Sans FB Demi', 12) ,command=lambda:click(boton1))
boton1.grid(row=1, column=0)
boton2 = Button(miFrame2)
boton2.config(width=5, height=2, font = ('Berlin Sans FB Demi', 12) ,command=lambda:click(boton2))
boton2.grid(row=1, column=1)
boton3 = Button(miFrame2)
boton3.config(width=5, height=2, font = ('Berlin Sans FB Demi', 12) ,command=lambda:click(boton3))
boton3.grid(row=1, column=2)
boton4 = Button(miFrame2)
boton4.config(width=5, height=2, font = ('Berlin Sans FB Demi', 12) ,command=lambda:click(boton4))
boton4.grid(row=2, column=0)
boton5 = Button(miFrame2)
boton5.config(width=5, height=2, font = ('Berlin Sans FB Demi', 12) ,command=lambda:click(boton5))
boton5.grid(row=2, column=1)
boton6 = Button(miFrame2)
boton6.config(width=5, height=2, font = ('Berlin Sans FB Demi', 12) ,command=lambda:click(boton6))
boton6.grid(row=2, column=2)
boton7 = Button(miFrame2)
boton7.config(width=5, height=2, font = ('Berlin Sans FB Demi', 12) ,command=lambda:click(boton7))
boton7.grid(row=3, column=0)
boton8 = Button(miFrame2)
boton8.config(width=5, height=2, font = ('Berlin Sans FB Demi', 12) ,command=lambda:click(boton8))
boton8.grid(row=3, column=1)
boton9 = Button(miFrame2)
boton9.config(width=5, height=2, font = ('Berlin Sans FB Demi', 12) ,command=lambda:click(boton9))
boton9.grid(row=3, column=2)
Button(miFrame2, text='REINICIAR', font=('Bahnschrift SemiBold', 11), bg="#e24a63", fg="white", command=reiniciar).grid(row=4, column=0, columnspan=3, pady=10, ipadx=5, ipady=1)

botones = [boton1, boton2, boton3, boton4, boton5, boton6, boton7, boton8, boton9]

root.mainloop()



