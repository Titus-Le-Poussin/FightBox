import pygame
import sys
import random

# Initialiser pygame
pygame.init()

# Dimensions de la fenêtre
WIDTH, HEIGHT = 1900, 1000
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Petit point rouge dans une boîte")

# Couleurs
red_barbar = (255, 0, 0)
WHITE_box = (255, 255, 255)
visionChamp = (250, 0, 0)
trail_color = (200, 200, 200)

# Classe pour la fenêtre bougeable
class MovableWindow:
    def __init__(self, x, y, width, height, title, font, text_color, bg_color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.title = title
        self.font = font
        self.text_color = text_color
        self.bg_color = bg_color
        self.dragging = False
        self.offset_x = 0
        self.offset_y = 0
        self.input_text = ""  # Texte saisi par l'utilisateur
        self.active = False  # Indique si la zone de texte est active

    def draw(self, surface):
        # Dessiner le fond de la fenêtre
        pygame.draw.rect(surface, self.bg_color, (self.x, self.y, self.width, self.height))
        # Dessiner le titre
        title_surface = self.font.render(self.title, True, self.text_color)
        surface.blit(title_surface, (self.x + 10, self.y + 10))
        # Dessiner la bordure de la fenêtre
        pygame.draw.rect(surface, (0, 0, 0), (self.x, self.y, self.width, self.height), 2)

         # Dessiner la zone de texte
        input_box = pygame.Rect(self.x + 10, self.y + 50, self.width - 20, 30)
        pygame.draw.rect(surface, (255, 255, 255), input_box)  # Fond blanc
        pygame.draw.rect(surface, (0, 0, 0), input_box, 2)  # Bordure noire
        input_surface = self.font.render(self.input_text, True, (0, 0, 0))
        surface.blit(input_surface, (input_box.x + 5, input_box.y + 5))


    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Clic gauche
                if self.x <= event.pos[0] <= self.x + self.width and    self.y <= event.pos[1] <= self.y + self.height:
                    self.dragging = True
                    self.offset_x = self.x - event.pos[0]
                    self.offset_y = self.y - event.pos[1]
                # Activer la zone de texte si on clique dessus
                    input_box = pygame.Rect(self.x + 10, self.y + 50, self.width - 20, 30)
                if input_box.collidepoint(event.pos):
                    self.active = True
                else:
                    self.active = False
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Relâcher le clic gauche
                self.dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                self.x = event.pos[0] + self.offset_x
                self.y = event.pos[1] + self.offset_y
        elif event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.input_text = self.input_text[:-1]  # Supprimer le dernier caractère
            else:
                self.input_text += event.unicode  # Ajouter le caractère saisi

# Initialiser la fenêtre bougeable
font = pygame.font.Font(None, 36)  # Police pour le texte
movable_window = MovableWindow(50, 50, 300, 100, "Nombre de barbares", font, (0, 0, 0), (200, 200, 200))

# Position et vitesse initiales du point rouge
x, y = WIDTH // 2, HEIGHT // 2
velocity = 2
radius = 10
vision_radius = radius * 5

# Stocker les positions pour le trajet
trail = []
show_trail = False  # Par défaut, la trainée est masquée
show_vision = False  # Par défaut, le champ de vision est masqué

# Charger l'image
image = pygame.image.load("Bubblexxxhdpi.png")  
image = pygame.transform.scale(image, (radius * 3, radius * 3))  # Adapter à la taille de la boule

# Générer une direction aléatoire avec des valeurs entre -1 et 1
def generate_random_direction():
    dx = random.uniform(-1, 1)  # Valeur aléatoire entre -1 et 1
    dy = random.uniform(-1, 1)  # Valeur aléatoire entre -1 et 1
    return dx, dy

# Initialiser la direction actuelle
current_direction = generate_random_direction()

# arrêts
steps = 0
max_steps = random.randint(50, 100)

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Basculer l'état de la trainée avec "Espace"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                show_trail = not show_trail  # Basculer l'état

            if event.key == pygame.K_ESCAPE:
                running = False # Quitter le programme

            # Basculer l'état du champ de vision avec "Shift"
            if event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT:
                show_vision = not show_vision  # Basculer l'état

        # Gérer les événements de la fenêtre bougeable
        movable_window.handle_event(event)

    # Déplacer le point rouge dans la direction actuelle
    if steps < max_steps:
        dx, dy = current_direction
        new_x, new_y = x + dx * velocity, y + dy * velocity

        # champ de vision
        if (
            x - vision_radius <= new_x <= x + vision_radius
            and y - vision_radius <= new_y <= y + vision_radius
            and radius <= new_x <= WIDTH - radius
            and radius <= new_y <= HEIGHT - radius
        ):
            x, y = new_x, new_y
            trail.append((x, y))  # Ajouter la position au trajet
        else:
            # Changer de direction si une limite est atteinte
            current_direction = generate_random_direction()
            steps = 0
            max_steps = random.randint(50, 100)
        steps += 1
    else:
        # S'arrêter pendant un moment avant de reprendre
        pygame.time.delay(500)
        current_direction = generate_random_direction()
        steps = 0
        max_steps = random.randint(50, 100)

    # Effacer la fenêtre
    WINDOW.fill(WHITE_box)

    # Dessiner le trajet si "Espace" a été activé
    if show_trail:
        for pos in trail:
            pygame.draw.circle(WINDOW, trail_color, pos, 2)

    # Afficher le champ de vision si "Shift" a été activé
    if show_vision:
        pygame.draw.circle(WINDOW, visionChamp, (x, y), vision_radius, 1)

    # Dessiner l'image à la place de la boule
    WINDOW.blit(image, (x - radius, y - radius))

    # Dessiner la fenêtre bougeable
    movable_window.draw(WINDOW)

    # Mettre à jour l'affichage
    pygame.display.flip()

    # Limiter la vitesse de la boucle
    pygame.time.Clock().tick(60)

# Quitter pygame
pygame.quit()
sys.exit()