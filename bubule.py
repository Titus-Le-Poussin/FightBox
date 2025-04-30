import pygame
import sys
import random

# création de l'écran
pygame.init()
WIDTH, HEIGHT = 1900, 1060
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble Game")

# Couleurs
red = (255, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
black = (0, 0, 0)
grey = (200, 200, 200)

# fenêtre du jeu
fenetre_largeur, fenetre_hauteur = 300, 900 # Dimensions de la fenêtre
fenetre_x, fenetre_y = 50, 100 # Position de la fenêtre
fenetre_de_jeu = pygame.Surface((fenetre_largeur, fenetre_hauteur))
fenetre_de_jeu.fill(grey)



#Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

   

    # couleur de l'écran
    screen.fill(white)
    # Dessiner la fenêtre de jeu
    screen.blit(fenetre_de_jeu, (fenetre_x, fenetre_y))
    # Mettre à jour l'affichage
    pygame.display.flip()

pygame.quit()