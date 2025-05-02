import pygame


def definir_couleurs():
    return {
        "white": (255, 255, 255),
        "black": (0, 0, 0),
        "red": (255, 0, 0),
        "green": (0, 255, 0),
        "blue": (0, 0, 255),
        "grey": (200, 200, 200),
        "light_grey": (211, 211, 211),
    }


def creer_boutons():
    """Créer les rectangles des boutons."""
    bouton_largeur, bouton_hauteur, espacement = 80, 40, 20
    boutons = {
        "troops": pygame.Rect(10, 10, bouton_largeur, bouton_hauteur),
        "props": pygame.Rect(10, 60, bouton_largeur, bouton_hauteur),
        "event": pygame.Rect(10, 110, bouton_largeur, bouton_hauteur),
    }
    return boutons


def dessiner_petite_fenetre(screen, fenetre_active, boutons, couleurs, font):
    """Dessiner la petite fenêtre avec les boutons et le contenu actif."""
    # Créer une surface pour la petite fenêtre
    fenetre_largeur, fenetre_hauteur = 300, screen.get_height()
    petite_fenetre = pygame.Surface((fenetre_largeur, fenetre_hauteur))
    petite_fenetre.fill(couleurs["grey"])

    # Dessiner les boutons (toujours visibles)
    pygame.draw.rect(petite_fenetre, couleurs["blue"], boutons["troops"])
    pygame.draw.rect(petite_fenetre, couleurs["green"], boutons["props"])
    pygame.draw.rect(petite_fenetre, couleurs["red"], boutons["event"])

    # Ajouter du texte centré sur chaque bouton
    petite_fenetre.blit(font.render("Troops", True, couleurs["white"]), boutons["troops"].move(10, 10).topleft)
    petite_fenetre.blit(font.render("Props", True, couleurs["white"]), boutons["props"].move(10, 10).topleft)
    petite_fenetre.blit(font.render("Event", True, couleurs["white"]), boutons["event"].move(10, 10).topleft)

    # Afficher le contenu spécifique en dessous des boutons
    if fenetre_active == "troops":
        options = ["Barbare", "Archer", "Mage", "Assassin"]
        for i, option in enumerate(options):
            text = font.render(option, True, couleurs["black"])
            petite_fenetre.blit(text, (20, 160 + i * 40))  # Positionner sous les boutons
    elif fenetre_active == "props":
        text = font.render("Fenêtre Props", True, couleurs["black"])
        petite_fenetre.blit(text, (20, 160))  # Positionner sous les boutons
    elif fenetre_active == "event":
        text = font.render("Fenêtre Event", True, couleurs["black"])
        petite_fenetre.blit(text, (20, 160))  # Positionner sous les boutons

    # Dessiner la petite fenêtre sur l'écran principal
    screen.blit(petite_fenetre, (0, 0))


def main():
    pygame.init()
    couleurs = definir_couleurs()
    screen = pygame.display.set_mode((1800, 1000))
    pygame.display.set_caption("Bubble Game")
    font = pygame.font.Font(None, 36)

    # Créer les boutons
    boutons = creer_boutons()

    # État actuel du jeu
    fenetre_active = "principal"  # Par défaut, afficher les boutons
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if boutons["troops"].collidepoint(event.pos):
                    fenetre_active = "troops"
                elif boutons["props"].collidepoint(event.pos):
                    fenetre_active = "props"
                elif boutons["event"].collidepoint(event.pos):
                    fenetre_active = "event"

        # Dessiner l'écran principal
        screen.fill(couleurs["light_grey"])

        # Dessiner la petite fenêtre
        dessiner_petite_fenetre(screen, fenetre_active, boutons, couleurs, font)

        # Mettre à jour l'affichage
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()