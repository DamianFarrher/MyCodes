#------------------- LEBRERÍAS -------------------
import turtle 
import time
import random

#------------------- ELEMENTOS -------------------

# PUNTOS
Puntos1 = 0
Puntos2 = 0

# VENTANA
wn = turtle.Screen()
wn.title('Pong')
wn.bgcolor('black')
wn.setup(width=600, height=600)
wn.tracer(0)

# LINEA DEL MEDIO
medio = turtle.Turtle()
medio.hideturtle()
medio.goto(0,300)
for i in range(30):
	medio.pencolor('gray')
	medio.sety(medio.ycor()-15)
	medio.pencolor('black')
	medio.sety(medio.ycor()-30)

# TEXTO PUNTOS
text = turtle.Turtle()
text.color('white')
text.penup()
text.hideturtle()
text.goto(0,240)
text.write('{}     {}'.format(Puntos1,Puntos2), align='center', font=('consolas',25,'normal'))

# PELOTA
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0,0)


# BARRA IZQUIERDA
pongl1 = turtle.Turtle()
pongl1.speed(0)
pongl1.shape('square')
pongl1.color('white')
pongl1.penup()
pongl1.goto(-250,40)
pongl2 = turtle.Turtle()
pongl2.speed(0)
pongl2.shape('square')
pongl2.color('white')
pongl2.penup()
pongl2.goto(-250,20)
pongl3 = turtle.Turtle()
pongl3.speed(0)
pongl3.shape('square')
pongl3.color('white')
pongl3.penup()
pongl3.goto(-250,0)
pongl4 = turtle.Turtle()
pongl4.speed(0)
pongl4.shape('square')
pongl4.color('white')
pongl4.penup()
pongl4.goto(-250,-20)
pongl5 = turtle.Turtle()
pongl5.speed(0)
pongl5.shape('square')
pongl5.color('white')
pongl5.penup()
pongl5.goto(-250,-40)


# BARRA DERECHA
pongr1 = turtle.Turtle()
pongr1.speed(0)
pongr1.shape('square')
pongr1.color('white')
pongr1.penup()
pongr1.goto(250,40)
pongr2 = turtle.Turtle()
pongr2.speed(0)
pongr2.shape('square')
pongr2.color('white')
pongr2.penup()
pongr2.goto(250,20)
pongr3 = turtle.Turtle()
pongr3.speed(0)
pongr3.shape('square')
pongr3.color('white')
pongr3.penup()
pongr3.goto(250,0)
pongr4 = turtle.Turtle()
pongr4.speed(0)
pongr4.shape('square')
pongr4.color('white')
pongr4.penup()
pongr4.goto(250,-20)
pongr5 = turtle.Turtle()
pongr5.speed(0)
pongr5.shape('square')
pongr5.color('white')
pongr5.penup()
pongr5.goto(250,-40)


#------------------- FUNCIONES -------------------

# subir y bajar pongl
def arriba_L(): 
	if pongl1.ycor() < 280:
		pongl1.sety(pongl1.ycor() + 20)
		pongl2.sety(pongl2.ycor() + 20)
		pongl3.sety(pongl3.ycor() + 20)
		pongl4.sety(pongl4.ycor() + 20)
		pongl5.sety(pongl5.ycor() + 20)
def abajo_L():
	if pongl5.ycor() > -280:
		pongl1.sety(pongl1.ycor() - 20)
		pongl2.sety(pongl2.ycor() - 20)
		pongl3.sety(pongl3.ycor() - 20)
		pongl4.sety(pongl4.ycor() - 20)
		pongl5.sety(pongl5.ycor() - 20)

# subir y bajar pongr
def arriba_R():
	if pongr1.ycor() < 280:
		pongr1.sety(pongr1.ycor() + 20)
		pongr2.sety(pongr2.ycor() + 20)
		pongr3.sety(pongr3.ycor() + 20)
		pongr4.sety(pongr4.ycor() + 20)
		pongr5.sety(pongr5.ycor() + 20)
def abajo_R():
	if pongr5.ycor() > -280:
		pongr1.sety(pongr1.ycor() - 20)
		pongr2.sety(pongr2.ycor() - 20)
		pongr3.sety(pongr3.ycor() - 20)
		pongr4.sety(pongr4.ycor() - 20)
		pongr5.sety(pongr5.ycor() - 20)


mov_y = 0
contador_toques = 0

# direccion de la pelota tras impactar en un pong
def direccion_pelota(num):
	global mov_y, mov_x, contador_toques
	mov_y=0

	if num==1:
		mov_y = random.randint(3,5)
	if num==2:
		mov_y = random.randint(2,3)
	if num==3:
		mov_y = random.randint(-2,2)
	if num==4:
		mov_y = random.randint(-3,-2)
	if num==5:
		mov_y = random.randint(-5,-3)

	contador_toques+=1

	if contador_toques==4:
		mov_x+=1
		contador_toques=0



sentido = 'R'
mov_x = 3

# direccion de la pelota
def mover_pelota():
	global mov_y, mov_x, sentido

	if sentido == 'R':
		ball.sety(ball.ycor() + mov_y)
		ball.setx(ball.xcor() + mov_x)
	if sentido == 'L':
		ball.sety(ball.ycor() + mov_y)
		ball.setx(ball.xcor() - mov_x)


ronda_win = 0

# al terminar la ronda
def finalizar():
	global sentido, mov_y, mov_x, contador_toques, ronda_win

	ball.goto(0,0)
	pongl1.goto(-250,40)
	pongl2.goto(-250,20)
	pongl3.goto(-250,0)
	pongl4.goto(-250,-20)
	pongl5.goto(-250,-40)
	pongr1.goto(250,40)
	pongr2.goto(250,20)
	pongr3.goto(250,0)
	pongr4.goto(250,-20)
	pongr5.goto(250,-40)


	if ronda_win==2:
		sentido='R'
	else:
		sentido='L'
	mov_y=0
	mov_x=3
	contador_toques=0

	time.sleep(1)



#-------------------- TECLADO --------------------

wn.listen()
wn.onkeypress(arriba_L, 'w')
wn.onkeypress(abajo_L, 's')
wn.onkeypress(arriba_R, 'Up')
wn.onkeypress(abajo_R, 'Down')



#--------------------- JUEGO ---------------------
while True:
	wn.update()

	# colision con techo / suelo
	if ball.ycor()>280 or ball.ycor()<-260:
		mov_y = mov_y * -1

	# colision borde Izq - gana Jugador de la Derecha
	if ball.xcor()<-300:
		Puntos2+=1
		ronda_win=2
		text.clear()
		text.write('{}     {}'.format(Puntos1,Puntos2), align='center', font=('consolas',25,'normal'))
		finalizar()

	# colision borde Der - gana Jugador de la Izquierda
	if ball.xcor()>300:
		Puntos1+=1
		ronda_win=1
		text.clear()
		text.write('{}     {}'.format(Puntos1,Puntos2), align='center', font=('consolas',25,'normal'))
		finalizar()

	# colision con pongl
	if ball.distance(pongl1)<20:
		direccion_pelota(1)
		sentido = 'R'
	if ball.distance(pongl2)<20:
		direccion_pelota(2)
		sentido = 'R'
	if ball.distance(pongl3)<20:
		direccion_pelota(3)
		sentido = 'R'
	if ball.distance(pongl4)<20:
		direccion_pelota(4)
		sentido = 'R'
	if ball.distance(pongl5)<20:
		direccion_pelota(5)
		sentido = 'R'

	# colision con pongr
	if ball.distance(pongr1)<20:
		direccion_pelota(1)
		sentido = 'L'
	if ball.distance(pongr2)<20:
		direccion_pelota(2)
		sentido = 'L'
	if ball.distance(pongr3)<20:
		direccion_pelota(3)
		sentido = 'L'
	if ball.distance(pongr4)<20:
		direccion_pelota(4)
		sentido = 'L'
	if ball.distance(pongr5)<20:
		direccion_pelota(5)
		sentido = 'L'


	mover_pelota()
	time.sleep(.01)
