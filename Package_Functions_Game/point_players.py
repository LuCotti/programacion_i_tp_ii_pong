import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
match_point_txt = "¡MATCH POINT!"
font_match_point = pygame.font.Font(None, 32)
RED = (255, 0, 0)

# Sonido cuando se consigue un punto
point_sound = pygame.mixer.Sound("Package_Sounds/point.mp3")
point_sound.set_volume(1)

def point_player_1(ball_x):
    if ball_x >= 780: # Cuando la pelota llega al borde de la pantalla derecha es punto del jugador 1
        pygame.mixer.Sound.play(point_sound)
        return True

def point_player_2(ball_x):
    if ball_x <= 0: # Cuando la pelota llega al borde de la pantalla izquierda es punto del jugador 2
        pygame.mixer.Sound.play(point_sound)
        return True

# En el caso de que uno de los jugadores consiga 9 puntos se mostrará el texto: "¡MATCH POINT!" y se reproducirá un audio
def match_point(player_1_score, player_2_score):
    if (player_1_score == 9 or player_2_score == 9): # Si cualquiera de los dos jugadores llega a 9 puntos
        match_point_surface = font_match_point.render(f"{match_point_txt}", True, RED)
        screen.blit(match_point_surface, (screen.get_width() / 2 - match_point_surface.get_width() / 2 - 2, 85)) # Ajustamos dónde aparece el cartel en X e Y
        return True