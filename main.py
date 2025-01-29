import pygame
from constants import *
from player import Player
def main():
	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2
	player = Player(x, y)
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0 
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	gameExit = False
	while not gameExit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
		screen.fill((0,0,0)) 
		player.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60) / 1000
if __name__ == "__main__":
    main()
