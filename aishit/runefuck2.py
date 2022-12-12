
import pygame
import random

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize pygame
pygame.init()

# Set up the window
width = 500
height = 500
window = pygame.display.set_mode((width, height))
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
    font = pygame.font.Font(None, 24)
    text = font.render(rune, True, WHITE)
    text_rect = text.get_rect()
    text_rect.center = (random.randint(0, width), random.randint(0, height))
    window.blit(text, text_rect)
    text = font.render(direction, True, WHITE)
    text_rect = text.get_rect()
    text_rect.center = (random.randint(0, width), random.randint(0, height))
    window.blit(text, text_rect)

    # Display whether the rune landed face up or face down
    text = font
