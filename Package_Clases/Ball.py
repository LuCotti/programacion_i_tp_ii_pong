import pygame
import random
import pygame.mixer as mixer

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

mixer.init()

screen = pygame.display.set_mode((800, 600)) # Tupla que define el tamaño de la ventana, con 800 píxeles de ancho y 600 píxeles de alto.

# Sonido colisión entre la pelota y la paleta
collision_paddle_sound = pygame.mixer.Sound("Package_Sounds/against_paddle.mp3")
collision_paddle_sound.set_volume(1)

# Sonido cuando choca contra los bordes
collision_boundaries_sound = pygame.mixer.Sound("Package_Sounds/against_boundarie.mp3")
collision_boundaries_sound.set_volume(1)

class Ball:
    def __init__(self):
        self.rect = pygame.Rect(400 - 10, 300 - 10, 20, 20)
        self.x_change = 0.2 * random.choice([-1, 1])
        self.y_change = 0.2 * random.choice([-1, 1])
        self.state = "waiting"
        # Pasamos a float las posiciones de X e Y, ya que es un Rect y esta es una forma de que se mueva a una velocidad en números con coma
        self.x_float = float(self.rect.x) # Aseguramos que sea un flotante desde el principio
        self.y_float = float(self.rect.y) # Aseguramos que sea un flotante desde el principio
        
    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)

    def move(self, left_paddle, right_paddle):
        # Si el jugador aprieta el espacio
        if self.state == "start":
            self.x_float += self.x_change # Modificamos la posición a partir de la velocidad
            self.y_float += self.y_change

            self.rect.x = self.x_float # Modificamos la posición actual para que realice
            self.rect.y = self.y_float # La ejecución a una Velocidad en números con coma
        
        # Si rebota en los bordes superiores e inferiores
        if self.rect.y <= 0 or self.rect.y >= screen.get_height() - self.rect.height:
            pygame.mixer.Sound.play(collision_boundaries_sound)
            self.y_change = -self.y_change
        
        # Si colisiona con una de las paletas, cambia la dirección
        if self.rect.colliderect(left_paddle) or self.rect.colliderect(right_paddle):
            pygame.mixer.Sound.play(collision_paddle_sound)
            self.x_change *= 1.1 # Aumenta la velocidad un 10% cada vez que la pelota hace un rebote.
            self.y_change *= 1.1 # Aumenta la velocidad un 10% en el eje Y también.
            self.x_change = -self.x_change # Cambia de lado
    
    def reset(self):
        self.rect.x = screen.get_width() / 2 - self.rect.width / 2 # Establecemos la posición en X de reset
        self.rect.y = screen.get_height() / 2 - self.rect.height / 2 # Establecemos la posición en Y de reset

        self.x_float = self.rect.x # Modificamos la posición actual en X a la posición de reset
        self.y_float = self.rect.y # Modificamos la posición actual en Y a la posición de reset

        self.x_change = 0.2 * random.choice([-1, 1]) # Volvemos a elegir un inicio aleatorio en X
        self.y_change = 0.2 * random.choice([-1, 1]) # Volvemos a elegir un inicio aleatorio en Y

        self.state = "waiting"