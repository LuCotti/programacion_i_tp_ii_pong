import pygame
import pygame.mixer as mixer
from Package_Clases import *
from Package_Functions_Game.point_players import point_player_1, point_player_2, match_point
from Package_Functions_Game.winner import winner
from Package_Functions_Game.players_scores import players_scores

pygame.init()
mixer.init()
screen = pygame.display.set_mode((800, 600)) # Tupla que define el tamaño de la ventana, con 800 píxeles de ancho y 600 píxeles de alto
pygame.display.set_caption("Pong") # Título de la ventana del juego

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Inicializamos los puntajes
player_1_score = 0
player_2_score = 0

status = "playing"

# Inicializamos los jugadores
player_1 = Player(20, 300)
player_2 = Player(760, 300)

# Inicializamos la pelota
ball = Ball()

# Inicializamos el audio y la bandera del match point
flag_match_point = False # Para evitar un loop infinito de audio
match_point_sound = pygame.mixer.Sound("Package_Sounds/match_point.mp3")
match_point_sound.set_volume(1)

# Bandera
running = True

while running:
    # Establecemos el fondo de pantalla
    screen.fill(BLACK)

    # Detección de eventos
    for event in pygame.event.get():
        match event.type:
            # Detecta si sale del juego
            case pygame.QUIT:
                running = False
            # Detección de eventos cuanto se aprieta una tecla
            case pygame.KEYDOWN:
                match event.key:
                    # Player 1
                    case pygame.K_w: 
                        player_1.y_change = -0.3
                    case pygame.K_s: 
                        player_1.y_change = 0.3

                    # Player 2
                    case pygame.K_DOWN:
                        player_2.y_change = 0.3 
                    case pygame.K_UP:
                        player_2.y_change = -0.3

                    # Si aprieta el espacio inicia el partido
                    case pygame.K_SPACE: 
                        if ball.state == "waiting": 
                            ball.state = "start"
                    
                    # Si aprieta la "r" vuelve al inicio
                    case pygame.K_r:
                        ball.reset()
                        player_1_score = 0
                        player_2_score = 0
                        status = "playing"

            # Detectar si se SUELTA la tecla
            case pygame.KEYUP:
                match event.key:
                    # Player 1
                    case pygame.K_w:
                        player_1.y_change = 0
                    case pygame.K_s:
                        player_1.y_change = 0

                    # Player 2
                    case pygame.K_UP:
                        player_2.y_change = 0
                    case pygame.K_DOWN:
                        player_2.y_change = 0
    
    # Mientras que la partida esté en proceso
    if status == "playing":
        pygame.draw.line(screen, WHITE, (400, 0), (400, 600), 2) # Línea vertical en el centro de la pantalla

        # Si y quien consiguió un punto
        if point_player_1(ball.rect.x):
            player_1_score += 1
            ball.reset()
        elif point_player_2(ball.rect.x):
            player_2_score += 1
            ball.reset()

        # Mover y dibujar a los jugadores
        player_1.move()
        player_1.draw()
        
        player_2.move()
        player_2.draw()

        # Mover y dibujar la pelota
        ball.move(player_1, player_2)
        ball.draw()

        # Mostramos por pantalla los puntajes
        players_scores(player_1_score, player_2_score)

        # Verificamos si están en match point e invertimos la flag para evitar un loop infinito
        if match_point(player_1_score, player_2_score):
            if not flag_match_point:
                flag_match_point = True
                pygame.mixer.Sound.play(match_point_sound)

        # Cuando uno de los jugadores logra 10 puntos, se termina el juego
        if player_1_score == 10 or player_2_score == 10:
            status = "finished"
    
    # Si el juego esta terminado
    elif status == "finished":
        # Si el player 1 fue quien consiguió los 10 puntos
        if player_1_score == 10:
            winner("PLAYER 1")
            pygame.display.flip() # Actualizamos la pantalla
            pygame.time.delay(3500) # Una vez terminado el juego, dejamos la venta abierta unos segundos
            running = False # Terminó el juego

        # Si el player 2 fue quien consiguió los 10 puntos
        elif player_2_score == 10:
            winner("PLAYER 2")
            pygame.display.flip()   
            pygame.time.delay(3500) 
            running = False         

    # Actualizar la pantalla
    pygame.display.flip()

pygame.quit()  # Se rompe el ciclo y se realiza el quit del juego