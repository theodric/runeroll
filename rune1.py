#!/usr/bin/env python3
# so here's the deal

#prefer internet, radio, or quantum entropy source
#use urandom for now

# array of runes listed in canonical Futhark order
# select 9 runes by random roll 
## allow user to push the key to "choose" each rune
# insert selection to 1st output array
# random roll for face up/down fall
# roll for X and Y position on casting cloth (parallel operation)
# random roll for face up/down landing
# if rune already selected, discard roll and reroll 
# //(is this the best way to do it? Shouldn't we somehow update the list to delete the ones already cast so
#    we don't pollute the validity of the cast by disposing of an entire roll?)
# reference look-up table of rune values against associations
# output tabular data
# later: plot casting cloth
# later: plot rune X/Y position on cloth

# Radial
# C
# I
# M
# O
# X
# IM
# OM

# Compass
# N
# NNE
# NE
# ENE
# ENE
# ESE
# SE
# SSE
# S
# SSW
# SW
# WSW
# W
# WNW
# NW
# NNW
