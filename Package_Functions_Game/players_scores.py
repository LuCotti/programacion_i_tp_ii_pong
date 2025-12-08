import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
font_players = pygame.font.Font(None, 32)
font_score = pygame.font.Font(None, 64)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

def players_scores(player_1_score, player_2_score):
    player_1_surface = font_players.render("PLAYER 1", True, RED)
    player_2_surface = font_players.render("PLAYER 2", True, RED)

    score_surface_p1 = font_score.render(f"{player_1_score}", True, WHITE)
    score_surface_p2 = font_score.render(f"{player_2_score}", True, WHITE)

    screen.blit(player_1_surface, (screen.get_width() / 2 - player_1_surface.get_width() - 10, 10))
    screen.blit(player_2_surface, (screen.get_width() / 2 + 10, 10))

    screen.blit(score_surface_p1, (screen.get_width() / 2 - score_surface_p1.get_width() - player_1_surface.get_width() / 2, 40))  
    screen.blit(score_surface_p2, (screen.get_width() / 2 + player_2_surface.get_width() / 2, 40))