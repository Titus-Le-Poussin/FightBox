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
bouton_largeur, bouton_hauteur, espacement = 80, 40, 20
bouton_troops = pygame.Rect(10,10, bouton_largeur, bouton_hauteur)
bouton_props = pygame.Rect(10 + bouton_largeur + espacement, 10, bouton_largeur, bouton_hauteur)
bouton_event = pygame.Rect(10 + 2 * (bouton_largeur + espacement), 10, bouton_largeur, bouton_hauteur)
font = pygame.font.Font(None, 36)  # Police par défaut, taille 36







#Boucle principale //NOTE coucou je suis un commentaire
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
    # couleur de l'écran
    screen.fill(white)
    # Dessiner la fenêtre de jeu
    screen.blit(fenetre_de_jeu, (fenetre_x, fenetre_y))

    # Dessiner les boutons
    pygame.draw.rect(fenetre_de_jeu, blue, bouton_troops)  # Bouton "Troops"
    pygame.draw.rect(fenetre_de_jeu, green, bouton_props)  # Bouton "Props"
    pygame.draw.rect(fenetre_de_jeu, red, bouton_event)  # Bouton "Event"
    # Ajouter du texte sur les boutons
    font = pygame.font.Font(None, 36)  # Police par défaut, taille 36
    screen.blit(font.render("Troops", True, black), bouton_troops.move(10, 10).topleft)
    screen.blit(font.render("Props", True, black), bouton_props.move(10, 10).topleft)
    screen.blit(font.render("Event", True, black), bouton_event.move(10, 10).topleft)


    # Mettre à jour l'affichage
    pygame.display.flip()

pygame.quit()