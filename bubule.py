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
    couleur = definir_couleurs()
    screen = pygame.display.set_mode((1800, 1000))
    pygame.display.set_caption("Bubble Game")
    screen.fill(couleur["light_grey"])
    return screen

def fenetre_principale(screen, couleurs):
    fenetre_largeur, fenetre_hauteur = 300, 900 
    fenetre_x, fenetre_y = 50, 100
    fenetre_de_jeu = pygame.Surface((fenetre_largeur, fenetre_hauteur))
    fenetre_de_jeu.fill(couleurs["grey"])
    screen.blit(fenetre_de_jeu, (fenetre_x, fenetre_y))
    return fenetre_de_jeu

def creer_boutons():
    return { 
        "troops": {"rect": pygame.Rect(10, 10, 80, 40), "content": fenetre_troops_options},
        "props": {"rect": pygame.Rect(10, 60, 80, 40), "content": fenetre_props_options},
        "event": {"rect": pygame.Rect(10, 110, 80, 40), "content": fenetre_event_options},
    }






    # Dessiner la petite fenêtre sur l'écran principal
    screen.blit(petite_fenetre, (0, 0))

def dessiner_boutons(fenetre_de_jeu, boutons, couleurs, font):
    for bouton, data in boutons.items():
        pygame.draw.rect(fenetre_de_jeu, couleurs["blue"], data["rect"])
        pygame.draw.rect(fenetre_de_jeu, couleurs["black"], data["rect"], 2)
        text = font.render(bouton.capitalize(), True, couleurs["white"])
        fenetre_de_jeu.blit(text, data["rect"].move(10, 10).topleft)


def afficher_contenu(fenetre_de_jeu, boutons, fenetre_active, couleurs, font):
    if fenetre_active in boutons:
        contenu = boutons[fenetre_active]["content"]()
        for i, (nom, valeur) in enumerate(contenu.items()):
            text = font.render(f"{nom}: {valeur}", True, couleurs["black"])
            fenetre_de_jeu.blit(text, (10, 150 + i * 50)) # Positionner le texte en dessous des boutons


def fenetre_troops_options():
    return {"Barbare": 3, "Archer": 2, "Mage": 5, "Assassin": 1} 

def fenetre_props_options():
    return {"Potion": 10, "Piège": 5, "Bouclier": 2}

def fenetre_event_options():
    return {"Invasion": "Active", "Marché": "Ouvert", "Quête": "Disponible"}




def main():
    couleur = definir_couleurs()
    screen = Ecran_principal()
    font = pygame.font.Font(None, 36)  

    boutons = creer_boutons()
    fenetre_active = "troops"  

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for bouton, data in boutons.items():
                    if data["rect"].collidepoint(event.pos):
                        fenetre_active = bouton

        screen.fill(couleur["light_grey"])
        fenetre_principale(screen, couleur)
        dessiner_boutons(screen, boutons, couleur, font)
        afficher_contenu(screen, boutons, fenetre_active, couleur, font)

        pygame.display.flip()

pygame.quit()

if __name__ == "__main__":
    main()