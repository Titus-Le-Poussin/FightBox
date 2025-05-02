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
    WIDTH, HEIGHT = 1800, 1000
    couleur = definir_couleurs()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Bubble Game")
    screen.fill(couleur["light_grey"])
    return screen

def fenetre_principale(screen, fenetre_active, boutons, couleurs, font):
    fenetre_largeur, fenetre_hauteur = 300, 900 
    fenetre_x, fenetre_y = 50, 100
    fenetre_de_jeu = pygame.Surface((fenetre_largeur, fenetre_hauteur))
    fenetre_de_jeu.fill(couleurs["grey"])
    
    

    screen.blit(fenetre_de_jeu, (fenetre_x, fenetre_y))
    





    # Dessiner les boutons

def creer_boutons():
    bouton_largeur, bouton_hauteur, espacement = 80, 40, 20
    boutons = {
    "troops": pygame.Rect(10,10, bouton_largeur, bouton_hauteur),
    "props": pygame.Rect(10 + bouton_largeur + espacement, 10, bouton_largeur, bouton_hauteur),
    "event": pygame.Rect(10 + 2 * (bouton_largeur + espacement), 10, bouton_largeur, bouton_hauteur),
    }
    return boutons



def afficher_fenetre_troops():
    couleur = definir_couleurs()
    options = ["Barbare", "Archer", "Mage", "Assassin"]
    for i, option in enumerate(options):
        text = font.render(option, True, couleur["black"])
        fenetre_de_jeu.blit(text, (100, 100 + i * 50))  

def afficher_fenetre_props():
    text = font.render("Fenêtre Props", True, "black")
    fenetre_de_jeu.blit(text, (100, 100))

def afficher_fenetre_event():
    text = font.render("Fenêtre Event", True, "black")
    fenetre_de_jeu.blit(text, (100, 100))







#Boucle principale //NOTE coucou je suis un commentaire
screen = Ecran_principal()
current_screen = "principal"  
running = True
while running:
    for event in pygame.event.get():
        couleurs = definir_couleurs()
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
#        elif event.type == pygame.MOUSEBUTTONDOWN:
#            if bouton_troops.collidepoint(event.pos):
#                current_screen = "troops"
#            elif bouton_props.collidepoint(event.pos):
#                current_screen = "props"
#            elif bouton_event.collidepoint(event.pos):
#                current_screen = "event"

        

                

            

    fenetre_principale(screen)  

    # Mettre à jour l'affichage
    pygame.display.flip()

pygame.quit()