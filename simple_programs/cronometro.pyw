from tkinter import *

proceso = 0
tiempoActual=0

def iniciar(contador=0):
	global proceso, tiempoActual

	btnIniciar.config(text='Intervalo', command=lambda:intervalo(tiempoActual))
	btnParar.config(text='Parar', state=NORMAL, command=parar)

	time.config(text=contador/10, fg='white')
	tiempoActual=contador
	proceso = time.after(94, iniciar, (contador+1))





def parar():
	global proceso, tiempoActual

	btnIniciar.config(text='Reanudar', command=lambda:iniciar(contador=tiempoActual)) 

	btnParar.config(text='REINICIAR', command=reiniciar)

	time.after_cancel(proceso)
	time.config(fg='#ac80e8')


def reiniciar():
	global proceso, tiempoActual, tiempoAnterior

	time.config(fg='white', text=0.0)
	time.after_cancel(proceso)
	tiempoActual = 0

	Intervalos.set('INTERVALOS\n')

	btnIniciar.config(text="INICIAR", command=iniciar)
	btnParar.config(text="Parar", command=parar, state=DISABLED)  

	tiempoAnterior = 0


tiempoAnterior = 0
def intervalo(t):
	global tiempoAnterior

	tiempoAnterior = t - tiempoAnterior

	Intervalos.set(Intervalos.get() + '\n' + str(t/10) + '   + ' + str(tiempoAnterior/10))

	tiempoAnterior = t





root = Tk()
root.title("Cronómetro")
root.geometry("+450+200")
root.config(bd=10, bg='#444449')


proceso = 0

time = Label(root, font=('consolas',30), text=0.0, bg='#444449', fg='white',  width=8)
time.grid(row=0, column=2, rowspan=2)

btnIniciar = Button(root)
btnIniciar.config(fg="#88e22b", bg='#444449',text="INICIAR", width=10, command=iniciar, font=('Bahnschrift', 10))
btnIniciar.grid(row=0, column=1, padx=3, ipadx=3, ipady=3)

btnParar = Button(root)
btnParar.config(fg="#e32472", bg='#444449', text="Parar", width=10, command=parar, font=('Bahnschrift', 10), state=DISABLED)  
btnParar.grid(row=1, column=1, padx=3, ipadx=3, ipady=3)



root_intervalo = Toplevel(root)
root_intervalo.geometry("+300+200")
root_intervalo.config(bd=10, bg='#444449')

Intervalos=StringVar()
Intervalos.set('INTERVALOS\n')

label_intervalos = Label(root_intervalo, textvariable=Intervalos, bg='#444449', fg='white', font=('consolas', 10)).pack()


root.mainloop()
