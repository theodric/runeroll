# runeroll
Python CLI 9-rune cast tool

(*See [Arith Härger's blog](https://arithharger.wordpress.com/2014/07/06/divination-with-runes-the-nine-rune-cast-method/) for more detail on the process. 
*)

* Uses an Internet-based entropy source for casts
* Eventually with an Urwid TUI
* Eventually with sick vector graphics
* Maybe

Anyway, you'll figure it out.

# so here's the deal

#prefer internet, radio, or quantum entropy source
#use urandom for now

# array of runes listed in canonical Futhark order
# select 9 runes by random roll 
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