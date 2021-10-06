import turtle
import time
import random

# MARCADOR
score = 0
high_score = 0

# VENTANA
wn = turtle.Screen()
wn.title('Snake')
wn.bgcolor('black')
wn.setup(width=600,height=600)
wn.tracer(0)


# SERPIENTE
snake = turtle.Turtle()
snake.speed(0)
snake.shape('square')
snake.color('white')
snake.penup()
snake.goto(0,0)
snake.direction = 'stop'


# CUERPO SERPIENTE
segments = []


# COMIDA
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(0,100)


# UBICACIONES COMIDA
uibcation = list(range(-280,280,20))


# TEXTO
version = turtle.Turtle()
version.speed(0)
version.color('white')
version.penup()
version.hideturtle()
version.goto(230,-280)
version.write('Snake v1.0')

text = turtle.Turtle()
text.speed(0)
text.color('white')
text.penup()
text.hideturtle()
text.goto(0,260)
text.write('Score: {}         High Score: {}'.format(score,high_score), align='center', font=('consolas',15,'normal'))


# FUNCIONES
def arriba():
	snake.direction = 'up'
def abajo():
	snake.direction = 'down'
def izquierda():
	snake.direction = 'left'
def derecha():
	snake.direction = 'right'


def mov():
	if snake.direction=='up':
		y = snake.ycor()
		snake.sety(y + 20)
	
	if snake.direction=='down':
		y = snake.ycor()
		snake.sety(y - 20)
	
	if snake.direction=='left':
		x = snake.xcor()
		snake.setx(x - 20)
	
	if snake.direction=='right':
		x = snake.xcor()
		snake.setx(x + 20)

def game_over():
	global score, high_score

	time.sleep(.5)
	snake.goto(0,0)
	snake.direction = 'stop'

	# econder segmentos
	for i in segments:
		i.goto(1000,1000)
	segments.clear()

	# poner high score
	if score>high_score:
		high_score=score
	text.clear()
	text.write('Score: {}         High Score: {}'.format(score,high_score), align='center', font=('consolas',15,'normal'))

	# reiniciar puntuacion
	score=0
	text.clear()
	text.write('Score: {}         High Score: {}'.format(score,high_score), align='center', font=('consolas',15,'normal'))



# TECLADO
wn.listen()
wn.onkeypress(arriba, 'Up')
wn.onkeypress(abajo, 'Down')
wn.onkeypress(izquierda, 'Left')
wn.onkeypress(derecha, 'Right')


# JUEGO
while True:
	wn.update()


	# colision bordes
	if snake.xcor()>280 or snake.xcor()<-280 or snake.ycor()>280 or snake.ycor()<-280:
		game_over()

	# colisiones cuerpo
	for i in segments:
		if i.distance(snake)<20:
			game_over()


	# colision comida
	if snake.distance(food)<20:
		x=random.randint(0,27)
		y=random.randint(0,27)
		food.goto(uibcation[x],uibcation[y])

		new_segment = turtle.Turtle()
		new_segment.speed(0)
		new_segment.shape('square')
		new_segment.color('grey')
		new_segment.penup()
		segments.append(new_segment)

		# aumentar marcador
		score+=1
		text.clear()
		text.write('Score: {}         High Score: {}'.format(score,high_score), align='center', font=('consolas',15,'normal'))


	# mover cuerpo serpiente
	totalSeg = len(segments)
	for i in range(totalSeg-1,0,-1):
		x = segments[i-1].xcor()
		y = segments[i-1].ycor()
		segments[i].goto(x,y)

	if totalSeg > 0:
		x = snake.xcor()
		y = snake.ycor()
		segments[0].goto(x,y)


	mov()
	time.sleep(.1)

	


