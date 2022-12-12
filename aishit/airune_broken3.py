#!/usr/bin/env python3

import pygame
import random

# Initialize pygame
pygame.init()

# Set up the window
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Rune Casting")

# Define the compass directions
directions = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]

# Define the list of runes
runes = ["Kaunan", "Thurisaz", "Haglaz", "Mannaz", "Sowilō", "Raido", "Ansuz", "Wunjô", "Tiwaz", "Algiz", "Laguz", "Gyfu", "Jēran", "Ehwaz", "Ingwaz", "Othala", "Oss", "Kauna", "Urr", "Yngvi"]

# Cast 9 random runes
for i in range(9):
    # Choose a random rune and direction
    rune = random.choice(runes)
    direction = random.choice(directions)

    # Choose whether the rune lands face up or face down
    face = random.choice(["up", "down"])

    # Display the rune and direction on the window
    font = pygame.font.Font(None, 36)
    text = font.render(rune, 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = random.randint(0, 800)
    textpos.centery = random.randint
