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

# Position et vitesse initiales du point rouge
x, y = WIDTH // 2, HEIGHT // 2
velocity = 2
radius = 10
vision_radius = radius * 5

# Directions possibles
directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # Haut, Bas, Gauche, Droite
current_direction = random.choice(directions)

# arrêts
steps = 0
max_steps = random.randint(50, 100)  

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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
        else:
            #change de direction si une limite est atteinte
            current_direction = random.choice(directions)
            steps = 0
            max_steps = random.randint(50, 100)
        steps += 1
    else:
        # s'arrêter pendant un moment avant de reprendre
        pygame.time.delay(500)
        current_direction = random.choice(directions)
        steps = 0
        max_steps = random.randint(50, 100)
    
    
    # Vérifier les limites de la boîte
    if radius <= new_x <= WIDTH - radius and radius <= new_y <= HEIGHT - radius:
        x, y = new_x, new_y
    else:
        # Changer de direction si une limite est atteinte
        current_direction = random.choice(directions)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RSHIFT] or keys[pygame.K_LSHIFT]:
        pygame.draw.circle(WINDOW, visionChamp, (x, y), vision_radius, 1)
    if keys[pygame.K_ESCAPE]:
        running = False

    # Dessiner la boîte et le point rouge
    WINDOW.fill(WHITE_box)
    pygame.draw.circle(WINDOW, red_barbar, (x, y), radius)
    pygame.display.flip()

    # Limiter la vitesse de la boucle
    pygame.time.Clock().tick(60)

# Quitter pygame
pygame.quit()
sys.exit()