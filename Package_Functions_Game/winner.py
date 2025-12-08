import pygame

screen = pygame.display.set_mode((800, 600))
RED = (255, 0, 0)

def winner(player):
    over_font = pygame.font.Font(None, 64)  # Asignamos la fuente y tamaño del texto
    over_surface = over_font.render(f"{player} WINS", True, RED)
    screen.blit(over_surface, (250, 250)) # Dibujamos el texto sobre la pantalla