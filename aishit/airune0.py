#!/usr/bin/env python3

import random

# List of runes
runes = ["Kaunan", "Thurisaz", "Haglaz", "Mannaz", "Sowilō", "Raido", "Ansuz", "Wunjô", "Tiwaz", "Algiz", "Laguz", "Gyfu", "Jēran", "Ehwaz", "Ingwaz", "Othala", "Oss", "Kauna", "Urr", "Yngvi"]

# List of directions
directions = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]

# Set the number of runes to cast
n_runes = 9

# List of cast runes
cast_runes = []

# Cast the runes
for i in range(n_runes):
    # Randomly select a rune
    rune = random.choice(runes)
    
    # Randomly determine if the rune lands face up or face down
    face_up = random.choice([True, False])
    
    # Randomly select a direction
    direction = random.choice(directions)
    
    # Add the cast rune to the list
    cast_runes.append((rune, direction, face_up))

# Print the results
print("Rune casting results:")
for rune, direction, face_up in cast_runes:
    face = "face up" if face_up else "face down"
    print(f"{rune} - {direction} - {face}")
