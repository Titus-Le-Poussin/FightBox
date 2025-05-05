import pygame


def definir_couleurs():
    """Définir les couleurs utilisées dans le jeu."""
    return {
        "white": (255, 255, 255),
        "black": (0, 0, 0),
        "red": (255, 0, 0),
        "green": (0, 255, 0),
        "blue": (0, 0, 255),
        "grey": (200, 200, 200),
        "light_grey": (211, 211, 211),
    }


def Ecran_principal():
    """Créer l'écran principal."""
    pygame.init()
    couleurs = definir_couleurs()
    screen = pygame.display.set_mode((1800, 1000))
    pygame.display.set_caption("Bubble Game")
    screen.fill(couleurs["light_grey"])
    return screen


def fenetre_principale(screen, couleurs):
    """Créer et dessiner la petite fenêtre sur le côté gauche."""
    fenetre_largeur, fenetre_hauteur = 300, screen.get_height()
    fenetre_x, fenetre_y = 0, 0
    petite_fenetre = pygame.Surface((fenetre_largeur, fenetre_hauteur))
    petite_fenetre.fill(couleurs["grey"])
    screen.blit(petite_fenetre, (fenetre_x, fenetre_y))
    return petite_fenetre


def creer_boutons():
    """Créer les boutons et leur contenu associé."""
    return {
        "troops": {"rect": pygame.Rect(10, 10, 80, 40), "content": fenetre_troops_options},
        "props": {"rect": pygame.Rect(10, 60, 80, 40), "content": fenetre_props_options},
        "event": {"rect": pygame.Rect(10, 110, 80, 40), "content": fenetre_event_options},
    }


def dessiner_boutons(petite_fenetre, boutons, couleurs, font):
    """Dessiner les boutons dans la petite fenêtre."""
    for bouton, data in boutons.items():
        # Dessiner le rectangle du bouton
        pygame.draw.rect(petite_fenetre, couleurs["blue"], data["rect"])
        # Ajouter un contour noir pour rendre le bouton plus visible
        pygame.draw.rect(petite_fenetre, couleurs["black"], data["rect"], 2)
        # Dessiner le texte centré dans le bouton
        text = font.render(bouton.capitalize(), True, couleurs["white"])
        text_rect = text.get_rect(center=data["rect"].center)
        petite_fenetre.blit(text, text_rect)


def afficher_contenu(petite_fenetre, boutons, fenetre_active, couleurs, font):
    """Afficher le contenu correspondant au bouton actif."""
    if fenetre_active in boutons:
        contenu = boutons[fenetre_active]["content"]()
        for i, (nom, valeur) in enumerate(contenu.items()):
            text = font.render(f"{nom}: {valeur}", True, couleurs["black"])
            petite_fenetre.blit(text, (20, 160 + i * 30))


def fenetre_troops_options():
    """Contenu de la fenêtre 'Troops'."""
    return {"Barbare": 3, "Archer": 2, "Mage": 5, "Assassin": 1}


def fenetre_props_options():
    """Contenu de la fenêtre 'Props'."""
    return {"Potion": 10, "Piège": 5, "Bouclier": 2}


def fenetre_event_options():
    """Contenu de la fenêtre 'Event'."""
    return {"Invasion": "Active", "Marché": "Ouvert", "Quête": "Disponible"}


def main():
    couleurs = definir_couleurs()
    screen = Ecran_principal()
    font = pygame.font.Font(None, 36)

    # Créer les boutons
    boutons = creer_boutons()

    # État actuel de la petite fenêtre
    fenetre_active = "troops"  # Par défaut, afficher les options "Troops"

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for bouton, data in boutons.items():
                    if data["rect"].collidepoint(event.pos):
                        fenetre_active = bouton

        # Dessiner l'écran principal
        screen.fill(couleurs["light_grey"])

        # Dessiner la petite fenêtre
        petite_fenetre = fenetre_principale(screen, couleurs)

        # Dessiner les boutons
        dessiner_boutons(petite_fenetre, boutons, couleurs, font)

        # Afficher le contenu actif
        afficher_contenu(petite_fenetre, boutons, fenetre_active, couleurs, font)

        # Mettre à jour l'affichage
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()