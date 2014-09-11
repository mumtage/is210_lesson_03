#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""pppppainting!"""


BASE = raw_input("Please choose a color to start: Seattle Gray or Manatee? ")

if "eattle" in BASE:
    ACCENT = raw_input("Now choose an accent color: "
                       "Ceramic Glaze or Cumulus Nimbus? ")
    if "ceramic" in ACCENT:
        HIGHLIGHT = raw_input("Now choose a highlight color: "
                              "White or Basically White? ")
    else:
        HIGHLIGHT = raw_input("Now choose a highlight color: "
                              "Off-White or Paper White? ")
else:
    ACCENT = raw_input("Now choose an accent color: "
                       "Platinum Mist or Spartan Sage? ")
    if "latinum" in ACCENT:
        HIGHLIGHT = raw_input("Now choose a highlight color: "
                              "Bone White or Just White? ")
    else:
        HIGHLIGHT = raw_input("Now choose a highlight color: "
                              "Fractal White or Not White? ")
print ("You've chosen a base color of {0}, "
      "accented with {1} "
      "and highlighted with {2}!".format(BASE, ACCENT, HIGHLIGHT))
