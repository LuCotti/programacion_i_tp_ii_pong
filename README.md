# Pong – Juego de Tenis Clásico

Juego de tenis clásico (Pong) desarrollado en Python utilizando la librería Pygame.  
Dos jugadores controlan paletas y compiten para evitar que la pelota cruce su lado de la pantalla.

## Descripción

El juego se ejecuta en una ventana gráfica donde una pelota se mueve de forma continua rebotando contra las paredes y las paletas de los jugadores.  
Cada vez que la pelota atraviesa el límite de una paleta, el jugador contrario suma un punto.  
El primer jugador en alcanzar los 10 puntos gana la partida.

## Funcionalidades

- Ventana de juego de 800x600 píxeles
- Fondo negro
- Pelota con movimiento diagonal y rebotes:
  - Rebote en paredes superiores e inferiores
  - Rebote al colisionar con las paletas
- Paletas controladas por teclado:
  - Jugador 1: teclas **W** (arriba) y **S** (abajo)
  - Jugador 2: flechas **↑** (arriba) y **↓** (abajo)
- Sistema de puntuación visible en pantalla
- Detección de victoria al alcanzar 10 puntos
- Mensaje de ganador al finalizar la partida
- Posibilidad de reiniciar el juego presionando la tecla **R**

## Tecnologías

- Python
- Pygame

## Controles

- **Jugador 1**
  - W: mover paleta hacia arriba
  - S: mover paleta hacia abajo
- **Jugador 2**
  - ↑: mover paleta hacia arriba
  - ↓: mover paleta hacia abajo
- **R**: reiniciar el juego

## Ejecución

1. Clonar el repositorio
2. Instalar las dependencias necesarias:
```bash
pip install pygame
```
3. Ejecutar el archivo principal del juego:
```bash
python main.py
```