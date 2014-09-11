#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""pppppainting!"""

import sys
if sys.version[0] == "2" : input = raw_input

BASE = input("Please choose a color to start: Seattle Gray or Manatee? ")

if "eattle" in BASE:
    ACCENT = input("Now choose an accent color: Ceramic Glaze or Cumulus Nimbus? ")
    if "eramic" in ACCENT:
        HIGHLIGHT = input("Now choose a highlight color: White or Basically White? ")
    else:
        HIGHLIGHT = input("Now choose a highlight color: Off-White or Paper White? ")
else:
    ACCENT = input("Now choose an accent color: Platinum Mist or Spartan Sage? ")
    if "latinum" in ACCENT:
        HIGHLIGHT = input("Now choose a highlight color: Bone White or Just White? ")
    else:
        HIGHLIGHT = input("Now choose a highlight color: Fractal White or Not White? ")
print ("You've chosen a base color of {0}, accented with {1} and highlighted with {2}!".format(BASE, ACCENT, HIGHLIGHT))
