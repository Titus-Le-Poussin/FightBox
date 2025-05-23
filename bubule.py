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
        "CHATGPT_Le_NULLOS": (140, 200, 40)

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
    fenetre_x, fenetre_y = 50, 50
    fenetre_de_jeu = pygame.Surface((fenetre_largeur, fenetre_hauteur))
    fenetre_de_jeu.fill(couleurs["grey"])
    pygame.draw.rect(fenetre_de_jeu, couleurs["black"], (0, 0, fenetre_largeur, fenetre_hauteur), 2)  
    screen.blit(fenetre_de_jeu, (fenetre_x, fenetre_y))
    return fenetre_de_jeu, fenetre_x, fenetre_y

def creer_boutons():
    return { 
        "troops": {"rect": pygame.Rect(10, 10, 80, 40), "content": fenetre_troops_options, "color":"blue"},
        "props": {"rect": pygame.Rect(110, 10, 80, 40), "content": fenetre_props_options, "color":"green"},
        "event": {"rect": pygame.Rect(210, 10, 80, 40), "content": fenetre_event_options, "color":"red"},        
    }
    print ("Boutons créés")






    # Dessiner la petite fenêtre sur l'écran principal
    screen.blit(petite_fenetre, (0, 0))

def dessiner_boutons(fenetre_de_jeu, boutons, couleurs, font, offset_x, offset_y):
    for bouton, data in boutons.items():
        rect = data["rect"].move(offset_x, offset_y)  ## Déplacer le rectangle du bouton
        pygame.draw.rect(fenetre_de_jeu, couleurs[data["color"]], rect) ## Dessiner le rectangle du bouton
        pygame.draw.rect(fenetre_de_jeu, couleurs["black"], rect, 2) ## Ajouter un contour noir pour rendre le bouton plus visible
        text = font.render(bouton.capitalize(), True, couleurs["white"]) ## Dessiner le texte centré dans le bouton

        text_rect = text.get_rect(center=rect.center)
        fenetre_de_jeu.blit(text, text_rect) ## Positionner le texte au centre du bouton


def afficher_contenu(fenetre_de_jeu, boutons, fenetre_active, couleurs, font):
    """Afficher le contenu correspondant au bouton actif."""
    if fenetre_active in boutons:
        contenu = boutons[fenetre_active]["content"](fenetre_de_jeu, couleurs, font)
        for i, (nom, valeur) in enumerate(contenu.items()):
            text = font.render(f"{nom}: {valeur}", True, couleurs["black"]) 
            fenetre_de_jeu.blit(text, (10, 150 + i * 50))  # Positionner le texte en dessous des boutons


def spawner_troops(fenetre_de_jeu, couleurs, font):
        rect = pygame.Rect(100, 10, 80, 40)
        pygame.draw.rect(fenetre_de_jeu, couleurs["red"], rect)
        pygame.draw.rect(fenetre_de_jeu, couleurs["black"], rect, 1)
        for i, (nom, valeur) in enumerate(contenu.items()):
            text = font.render("Spawn", True, couleurs["white"])
            fenetre_de_jeu.blit(text, (100, 10 + i * 50))
        return rect

def main_spawn():
    print ("spawn")    

def fenetre_troops_options(fenetre_de_jeu, couleurs, font):
    print ("Fenetre troops options")
    contenu = {
       "Barbares": 0, "Archer": 0, "Mage": 0, "Assassin": 0,  
    }
    spawn_rect = spawner_troops(fenetre_de_jeu, couleurs, font, contenu)  # Passer 'contenu' à spawner_troops
    return spawn_rect
    

def fenetre_props_options():
    print ("Fenetre props options")
    return {"Potion": 10, "Piège": 5, "Bouclier": 2}

def fenetre_event_options():
    print ("Fenetre event options")
    return {"Invasion": "Active", "Marché": "Ouvert", "Quête": "Disponible"}




def main():
    couleur = definir_couleurs()
    screen = Ecran_principal()
    font = pygame.font.Font(None, 36)  

    boutons = creer_boutons()
    fenetre_active = "troops"  
    spawn_rect = None

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if spawn_rect and spawn_rect.collidepoint(event.pos):
                    main_spawn()
                for bouton, data in boutons.items():
                    # Vérifier si un bouton a été cliqué
                    rect = data["rect"].move(offset_x, offset_y)
                    if rect.collidepoint(event.pos):
                        fenetre_active = bouton

        screen.fill(couleur["light_grey"])
        fenetre_de_jeu, offset_x, offset_y = fenetre_principale(screen, couleur)
        dessiner_boutons(fenetre_de_jeu, boutons, couleur, font, 0, 0)
        if fenetre_active == "troops":
            spawn_rect = fenetre_troops_options(fenetre_de_jeu, couleur, font)
        afficher_contenu(fenetre_de_jeu, boutons, fenetre_active, couleur, font)

        screen.blit(fenetre_de_jeu, (offset_x, offset_y))  # 

        pygame.display.flip()

pygame.quit()

if __name__ == "__main__":
    main()