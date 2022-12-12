#!/usr/bin/env python3

import random
import pygame

# List of runes
runes = ["Kaunan", "Thurisaz", "Haglaz", "Mannaz", "Sowilō", "Raido", "Ansuz", "Wunjô", "Tiwaz",
         "Algiz", "Laguz", "Gyfu", "Jēran", "Ehwaz", "Ingwaz", "Othala", "Oss", "Kauna", "Urr", "Yngvi"]

# List of directions
directions = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]

# Initialize pygame
pygame.init()

# Create a screen with a size of 600x600 pixels
screen = pygame.display.set_mode((600, 600))

# Set the title of the screen
pygame.display.set_caption("Rune casting")

# Set the font to be used for the text
font = pygame.font.Font(None, 36)

# Cast 9 random runes
for i in range(9):
    # Choose a random rune and direction
    rune = random.choice(runes)
    direction = random.choice(directions)

    # Choose a random position for the rune on the screen
    x = random.randint(100, 500)
    y = random.randint(100, 500)

    # Choose a random orientation for the rune (face up or face down)
    orientation = random.choice(["face up", "face down"])

    # Display the rune and its position on the screen
    text = font.render(f"{rune} ({direction}, {orientation})", True, (0, 0, 0))
    screen.blit(text, (x, y))

    # Update the screen
    pygame.display.flip()

# Wait until the user closes the window
#while True:
#    for event
