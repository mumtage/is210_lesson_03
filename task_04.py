#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""snooooze!"""

import sys
if sys.version[0] == "2" : input = raw_input

DAY = input("What day is it? ")

TIME = int(input("Please input the time as a 4-digit number without a colon ('eg,0605): "))

SNOOZE = True if "sat" in DAY.lower() or "sun" in DAY.lower() or TIME < 600 else False

if not SNOOZE:
    print "Beep! " * 5
