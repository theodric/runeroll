#!/usr/bin/env python3

import random
import pygame

# Define the colors we will use
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define the dimensions of the window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Define the size of the runes
RUNE_SIZE = 50

# Define the names of the runes
runes = ['Kaunan', 'Thurisaz', 'Haglaz', 'Mannaz', 'Sowilō', 'Raido', 'Ansuz', 'Wunjô', 'Tiwaz', 'Algiz', 'Laguz', 'Gyfu', 'Jēran', 'Ehwaz', 'Ingwaz', 'Othala', 'Oss', 'Kauna', 'Urr', 'Yngvi']

# Define the directions of the compass
directions = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']

# Initialize pygame
pygame.init()

# Set the window title
pygame.display.set_caption('Rune Casting')

# Create the window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Run the game loop
running = True
while running:
    # Clear the screen
    screen.fill(BLACK)

    # Cast 9 runes
    for i in range(9):
        # Choose a random rune
        rune = random.choice(runes)

        # Choose a random direction
        direction = random.choice(directions)

        # Choose a random orientation (face up or face down)
        orientation = random.choice(['face up', 'face down'])

        # Draw the rune
        x = WINDOW_WIDTH / 2 + WINDOW_WIDTH / 2 * math.cos(math.radians(22.5 * i))
        y = WINDOW_HEIGHT / 2 + WINDOW_HEIGHT / 2 * math.sin(math.radians(22.5 * i))
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), RUNE_SIZE)

        # Draw the direction
        font = pygame.font.Font(None, 24)
        text = font.render(direction, True, WHITE)
        text_rect = text.get_rect()
        text_rect.center = (int(x), int(y))
        screen.blit(text, text_rect)

        # Draw the orientation
        font = pygame.font.Font(None, 16)
        text = font.render(orientation, True, WHITE)
        text_rect = text.get_rect()
        text_rect.center = (int(x), int(y) + RUNE_SIZE + 10)
        screen.blit(text, text_rect)

        # Draw the name of the rune
        font = pygame.font.Font(None, 16)
        text = font.render(rune, True, WHITE)
        text_rect = text.get_rect()
        text_rect.center = (int(x), int(y) - RUNE_SIZE - 10)
        screen.blit(text, text_rect)

    # Update the screen
    pygame.display.flip()

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit pygame
pygame.quit()

