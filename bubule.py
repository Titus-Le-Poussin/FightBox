import pygame
import sys
import random


def definir_couleurs():
    return {
        "white": (255, 255, 255),
        "black": (0, 0, 0),
        "red": (255, 0, 0),
        "green": (0, 255, 0),
        "blue": (0, 0, 255),
        "grey": (200, 200, 200),
        "purple": (128, 0, 128),
        "yellow": (255, 255, 0),
        "orange": (255, 165, 0),
        "pink": (255, 192, 203),
        "cyan": (0, 255, 255),
        "brown": (165, 42, 42),
        "light_blue": (173, 216, 230),
        "light_green": (144, 238, 144),
        "light_grey": (211, 211, 211),

    }
# création de l'écran
def Ecran_principal(): 
    pygame.init()
    WIDTH, HEIGHT = 1900, 1060
    couleur = definir_couleurs()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Bubble Game")
    screen.fill(couleur["light_grey"])
    return screen

def fenetre_principale(screen):# fenêtre du jeu

    fenetre_largeur, fenetre_hauteur = 300, 900 # Dimensions de la fenêtre
    fenetre_x, fenetre_y = 50, 100 # Position de la fenêtre
    fenetre_de_jeu = pygame.Surface((fenetre_largeur, fenetre_hauteur))
    fenetre_de_jeu.fill("grey")
    screen.blit(fenetre_de_jeu, (fenetre_x, fenetre_y))
    dessiner_boutons(fenetre_de_jeu)





    # Dessiner les boutons

def dessiner_boutons(fenetre_de_jeu):
    bouton_largeur, bouton_hauteur, espacement = 80, 40, 20
    bouton_troops = pygame.Rect(10,10, bouton_largeur, bouton_hauteur)
    bouton_props = pygame.Rect(10 + bouton_largeur + espacement, 10, bouton_largeur, bouton_hauteur)
    bouton_event = pygame.Rect(10 + 2 * (bouton_largeur + espacement), 10, bouton_largeur, bouton_hauteur)
    font = pygame.font.Font(None, 36)  # Police par défaut, taille 36
    pygame.draw.rect(fenetre_de_jeu, "blue", bouton_troops)  
    pygame.draw.rect(fenetre_de_jeu, "green", bouton_props)  
    pygame.draw.rect(fenetre_de_jeu, "red", bouton_event)
    font = pygame.font.Font(None, 36)  # Police par défaut, taille 36

    text_troops = font.render("Troops", True, "white")
    text_props = font.render("Props", True, "white")
    text_event = font.render("Event", True, "white")

    # Centrer le texte sur chaque bouton
    text_rect_troops = text_troops.get_rect(center=(bouton_troops.centerx, bouton_troops.centery))
    text_rect_props = text_props.get_rect(center=(bouton_props.centerx, bouton_props.centery))
    text_rect_event = text_event.get_rect(center=(bouton_event.centerx, bouton_event.centery))

    # Dessiner le texte sur les boutons
    fenetre_de_jeu.blit(text_troops, text_rect_troops)
    fenetre_de_jeu.blit(text_props, text_rect_props)
    fenetre_de_jeu.blit(text_event, text_rect_event)

def afficher_fenetre_troops():
    options = ["Barbare", "Archer", "Mage", "Assassin"]
    for i, option in enumerate(options):
        text = font.render(option, True, "black")
        fenetre_de_jeu.blit(text, (100, 100 + i * 50))  # Espacement vertical entre les options

def afficher_fenetre_props():
    text = font.render("Fenêtre Props", True, "black")
    fenetre_de_jeu.blit(text, (100, 100))

def afficher_fenetre_event():
    text = font.render("Fenêtre Event", True, "black")
    fenetre_de_jeu.blit(text, (100, 100))







#Boucle principale //NOTE coucou je suis un commentaire
screen = Ecran_principal()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    fenetre_principale(screen)  

    # Mettre à jour l'affichage
    pygame.display.flip()

pygame.quit()