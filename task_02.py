#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""pppppressure!"""


BP = int(raw_input("What's your blood pressure eh? "))

if BP < 90:
    BP_STATUS = "Low"
elif BP < 120:
    BP_STATUS = "Ideal"
elif BP < 140:
    BP_STATUS = "Warning"
elif BP < 160:
    BP_STATUS = "High"
else:
    BP_STATUS = "Emergency"

print "Your blood pressure is at {0} levels!".format(BP_STATUS)
