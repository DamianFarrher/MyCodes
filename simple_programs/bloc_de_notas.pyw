from tkinter import *
from tkinter import filedialog as FileDialog
from io import open
from tkinter import messagebox



root=Tk()
root.geometry('600x400')
root.minsize(250, 100)
root.title("Mi editor")

ruta=""

LF=StringVar()
LF.set("consolas")

TF=IntVar()
TF.set(10)


#-----------------------------------------------FUNCIONES

def nuevo():
	global ruta

	ruta=""
	mensaje.set("Nuevo fichero")
	texto.delete(1.0,END)


def abrir(): 
	global ruta

	mensaje.set("Abrir fichero")
	ruta = FileDialog.askopenfilename(title="Abrir", initialdir="C:", filetypes=(("Archivos de texto", "*.txt"),))

	if ruta!="":
		fichero=open(ruta,"r")
		contenido=fichero.read()
		texto.delete(1.0,END)
		texto.insert("insert", contenido)
		fichero.close()
		root.title(ruta + " - Mi editor")

	mensaje.set("Edición de texto")


def guardar():
	global ruta
	
	if ruta != "": 
		contenido=texto.get(1.0,'end-1c')
		fichero.open(ruta,"w")
		fichero.write(contenido)
		fichero.close()
		mensaje.set("Fichero guardado correctamente.")
	else:
		guardar_como()


def guardar_como():
    global ruta
    mensaje.set("Guardar fichero como")

    fichero = FileDialog.asksaveasfile(title="Guardar fichero", 
        mode="w", defaultextension=".txt")

    if fichero is not None:
        ruta = fichero.name
        contenido = texto.get(1.0,'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardado correctamente")
    else:
        mensaje.set("Guardado cancelado")
        ruta = ""


def cerrar():
	global ruta
	mensaje.set("Cerrar documento.")
	valor=messagebox.askquestion("Cerrar", "¿Cerrar documento?\nLos datos no guardados se perderán.")
	if valor=="yes":
		nuevo()	
	else:
		mensaje.set("Edición de texto")


		



MO=IntVar()

def modo_oscuro():
	if MO.get()==0:
		texto.config(insertbackground="black", bg="white", fg="black")
	else:
		texto.config(insertbackground="white", bg="#282923", fg="white")

def letraFuente():
	if LF.get()=="consolas":
		texto.config(font=("consolas", TF.get()))
	elif LF.get()=="arial":
		texto.config(font=("arial", TF.get()))
	elif LF.get()=="calibri":
		texto.config(font=("calibri", TF.get()))
	elif LF.get()=="times new roman":
		texto.config(font=("times new roman", TF.get()))

def tamañoFuente():
	if TF.get()==8:
		texto.config(font=(LF.get(), 8))
	elif TF.get()==10:
		texto.config(font=(LF.get(), 10))
	elif TF.get()==12:
		texto.config(font=(LF.get(), 12))
	elif TF.get()==16:
		texto.config(font=(LF.get(), 16))
	elif TF.get()==22:
		texto.config(font=(LF.get(), 22))


def acerca_de():
	messagebox.showinfo("Info", "Bloc de notas.\nCreado: 27.01.2020")

def salir():
	mensaje.set("Salir")
	s=messagebox.askquestion("Salir", "¿Salir de la aplicacón?")
	if s=="yes":
		root.quit()
	else:
		mensaje.set("Edición de texto")




#---------------------------------------------CREAR MENUS

barraMenu = Menu(root)
root.config(menu=barraMenu)


Archivo = Menu(barraMenu, tearoff=0)
Archivo.add_command(label="Nuevo", command=nuevo)
Archivo.add_command(label="Abrir...", command=abrir)
Archivo.add_command(label="Guardar", command=guardar)
Archivo.add_command(label="Guardar como...", command=guardar_como)
Archivo.add_separator()
Archivo.add_command(label="Cerrar", command=cerrar)
Archivo.add_command(label="Salir", command=salir)


Editar = Menu(barraMenu, tearoff=0)
Editar.add_command(label="")


Herramientas = Menu(barraMenu, tearoff=0)
Herramientas.add_radiobutton(label="Modo claro", variable=MO, command=modo_oscuro, value=0)
Herramientas.add_radiobutton(label="Modo oscuro", variable=MO, command=modo_oscuro, value=1)
Herramientas.add_separator()

Letra = Menu(Herramientas, tearoff=0)
Letra.add_radiobutton(label="Consolas", variable=LF, command=letraFuente, value="consolas")
Letra.add_radiobutton(label="Arial", variable=LF, command=letraFuente, value="arial")
Letra.add_radiobutton(label="Calibri", variable=LF, command=letraFuente, value="calibri")
Letra.add_radiobutton(label="Times New Roman", variable=LF, command=letraFuente, value="times new roman")

Tamaño = Menu(Herramientas, tearoff=0)
Tamaño.add_radiobutton(label="Muy pequeño", variable=TF, command=tamañoFuente, value=8)
Tamaño.add_radiobutton(label="Pequeño", variable=TF, command=tamañoFuente, value=10)
Tamaño.add_radiobutton(label="Mediano", variable=TF, command=tamañoFuente, value=12)
Tamaño.add_radiobutton(label="Grande", variable=TF, command=tamañoFuente, value=16)
Tamaño.add_radiobutton(label="Muy Grande", variable=TF, command=tamañoFuente, value=22)


Ayuda = Menu(barraMenu, tearoff=0)
Ayuda.add_command(label="Acerca de...", command=acerca_de)





#--------------------------------------------AÑADIR MENUS

barraMenu.add_cascade(label="Archivo", menu=Archivo)
barraMenu.add_cascade(label="Editar", menu=Editar)
barraMenu.add_cascade(label="Herramientas", menu=Herramientas)
Herramientas.add_cascade(label="Fuente", menu=Letra)
Herramientas.add_cascade(label="Tamaño", menu=Tamaño)
barraMenu.add_cascade(label="Ayuda", menu=Ayuda)


#------------------------------------------------INTERFAZ

texto=Text(root)
texto.pack(fill='both', expand=1)
#texto.config(pady=5, padx=5, font=("consolas", 10))
texto.config(pady=5, padx=5, height=0, wrap=WORD, font=("consolas", 10), relief=None)

mensaje = StringVar()
mensaje.set('Nuevo fichero')
monitor = Label(root, textvar=mensaje, justify='right')
monitor.pack(side='left')



root.mainloop()
