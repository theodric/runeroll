#!/usr/bin/env python3

import matplotlib.pyplot as plt
import random

# Set up the matplotlib chart
fig, ax = plt.subplots()
ax.set_title("Rune Casting")
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Define the compass directions
directions = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]

# Cast 9 random runes
for i in range(9):
    # Choose a random rune and direction
    rune = random.choice(runes)
    direction = random.choice(directions)

    # Display the rune and direction on the chart
    ax.text(random.random(), random.random(), rune, ha="center", va="center")
    ax.text(random.random(), random.random(), direction, ha="center", va="center")

# Show the chart
plt.show()
