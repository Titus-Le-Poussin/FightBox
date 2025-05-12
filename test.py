import pygame
import sys

def definir_couleurs():
    return {
        "white": (255, 255, 255),
        "red": (255, 0, 0),
        "blue": (0, 0, 255),
        "black": (0, 0, 0),
    }

def main():
    # Initialisation de Pygame
    pygame.init()
    couleurs = definir_couleurs()

    # Création de la fenêtre
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Boutons Rouge et Bleu")

    # Définir les boutons
    bouton_rouge = pygame.Rect(350, 250, 100, 50)  # Bouton rouge au centre
    bouton_bleu = pygame.Rect(700, 10, 80, 40)  # Bouton bleu dans le coin supérieur droit
    bouton_bleu_visible = False  # Le bouton bleu est caché au départ
    bouton_rouge_visible = True  
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if bouton_rouge.collidepoint(event.pos):
                    bouton_bleu_visible = True 
                if bouton_bleu_visible and bouton_bleu.collidepoint(event.pos):
                    print("nan")
                    bouton_rouge_visible = False # Afficher le bouton bleu si le bouton rouge est cliqué

        # Remplir l'écran avec du blanc
        screen.fill(couleurs["white"])

        # Dessiner le bouton rouge
        pygame.draw.rect(screen, couleurs["red"], bouton_rouge)
        pygame.draw.rect(screen, couleurs["black"], bouton_rouge, 2)  # Contour noir

        # Dessiner le bouton bleu s'il est visible
        if bouton_bleu_visible:
            pygame.draw.rect(screen, couleurs["blue"], bouton_bleu)
            pygame.draw.rect(screen, couleurs["black"], bouton_bleu, 2)  # Contour noir

        # Mettre à jour l'affichage
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()