#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""snooooze!"""


DAY = raw_input("What day is it? ")

TIME = int(raw_input(
    "Please input the time as a 4-digit number without a colon ('eg,0605): "))

WEEKEND = "sat" in DAY.lower() or "sun" in DAY.lower()

SNOOZE = True if WEEKEND or TIME < 600 else False

if not SNOOZE:
    print "Beep! " * 5
