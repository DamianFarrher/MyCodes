import pygame
import numpy as np
import time
import random

pygame.init()
pygame.display.set_caption('Game of Life')

# tamaño pantalla
width, height = 500, 500
screen = pygame.display.set_mode((height, width))

# color de fondo
bg = 65, 75, 85
screen.fill(bg)

# numero de celdas
nxC, nyC = 50, 50
# dimensiones de las celdas
dimCW = width  / nxC
dimCH = height / nyC

# estados de las celdas
gameState = np.zeros((nxC, nyC))



# encender célular aleatoriamente
#for i in range(350):
#	gameState[random.randint(0,49), random.randint(0,49)] = 1



# control de la ejecución
pauseExect = False

# para que ande fluido el mouse, pero que no vaya tan rapido el juego
# si se quiere sacar, ver las '# <---'
count = 0                                                            # <--- eliminar

while True:

	count += 1                                                       # <--- eliminar

	time.sleep(.01)                                                  # <--- cambiar a .1

	screen.fill(bg)
	newGameState = np.copy(gameState)

	ev = pygame.event.get()


	# entradas del usuario
	for event in ev:

		# cerrar ventana al presionar la X
		if event.type == pygame.QUIT:
			exit()

		# pausar programa al tocar una tecla
		if event.type == pygame.KEYDOWN:
			pauseExect = not pauseExect

		# clicks del mouse
		mouseClick = pygame.mouse.get_pressed()
		if sum(mouseClick) > 0:
			posX, posY = pygame.mouse.get_pos()
			celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
			newGameState[celX, celY] = not mouseClick[2]


	# recorre el tablero
	for y in range(0, nxC):
		for x in range(0, nyC):

			if not pauseExect and count%5==0:                        # <--- eliminar 'and count%5==0'
				# calcular la cantidad de vecinos
				n_neigh = gameState[(x-1) % nxC, (y-1) % nyC] + \
						  gameState[ (x)  % nxC, (y-1) % nyC] + \
						  gameState[(x+1) % nxC, (y-1) % nyC] + \
						  gameState[(x-1) % nxC,  (y)  % nyC] + \
						  gameState[(x+1) % nxC,  (y)  % nyC] + \
						  gameState[(x-1) % nxC, (y+1) % nyC] + \
						  gameState[ (x)  % nxC, (y+1) % nyC] + \
						  gameState[(x+1) % nxC, (y+1) % nyC]


				# REGLA 1 : una célula revive con 3 vecinas
				if gameState[x, y]==0 and n_neigh==3:
					newGameState[x, y] = 1

				# REGLA 2 : una célula vive solo con 2 o 3 vecinas
				elif gameState[x, y]==1 and (n_neigh<2 or n_neigh>3):
					newGameState[x, y] = 0


			# crear el polígono a cada celda a dibujar
			poly = [((x)   * dimCW, (y)   * dimCH),
					((x+1) * dimCW, (y)   * dimCH),
					((x+1) * dimCW, (y+1) * dimCH),
					((x)   * dimCW, (y+1) * dimCH)]

			# dibujar cada cuadrado
			if newGameState[x, y] == 0:
				pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
			else:
				pygame.draw.polygon(screen, (225, 225, 225), poly, 0)

	# actualizar el estado del juego
	gameState = np.copy(newGameState)

	# actualizar la pantalla
	pygame.display.flip()




