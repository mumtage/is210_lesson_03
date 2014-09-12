#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""usury"""


from decimal import Decimal

NAME = raw_input("What is your name? ")

while True:
    PRINCIPAL = raw_input("What is the amount of your principal "
                          "(the amount being borrowed)? ")
    try:
        PRINCIPAL = int(PRINCIPAL)
    except ValueError:
        print "Please enter the amount as a integer..."
    else:
        break

while True:
    YEARS = raw_input("For how many years is this loan being borrowed? ")
    try:
        YEARS = int(YEARS)
    except ValueError:
        print "Please enter in the form of an integer..."
    else:
        break

while True:
    QUALIFIED = raw_input("Are you pre-qualified for this loan? ").lower()
    if QUALIFIED not in ['yes', 'y', 'no', 'n']:
        print "Sorry, please answer 'yes' or 'no'. "
    else:
        break

TOTAL = True

if 0 < PRINCIPAL < 200000:
    if YEARS < 16:
        if "y" in QUALIFIED:
            R = .0363
        else:
            R = .0465
    elif YEARS < 21:
        if "y" in QUALIFIED:
            R = .0404
        else:
            R = .0498
    elif YEARS <= 30:
        if "y" in QUALIFIED:
            R = .0577
        else:
            R = .0639
    else:
        TOTAL = None
        R = 1
elif 200000 <= PRINCIPAL < 1000000:
    if YEARS < 16:
        if "y" in QUALIFIED:
            R = .0302
        else:
            R = .0398
    elif YEARS < 21:
        if "y" in QUALIFIED:
            R = .0327
        else:
            R = .0408
    elif YEARS <= 30:
        if "y" in QUALIFIED:
            R = .0466
        else:
            TOTAL = None
            R = 1
    else:
        TOTAL = None
        R = 1
elif PRINCIPAL >= 1000000:
    if YEARS < 16:
        if "y" in QUALIFIED:
            R = .0205
        else:
            TOTAL = None
            R = 1
    elif YEARS < 21:
        if "y" in QUALIFIED:
            R = .0262
        else:
            TOTAL = None
            R = 1
    else:
        TOTAL = None
        R = 1
else:
    TOTAL = None

if TOTAL:
    TOTAL = int(
        round(PRINCIPAL * (1 + (Decimal('{0}'.format(R))/12))**(12 * YEARS)))


REPORT = """
Loan Report for: {0}
---------------------------------------------------------------------
    Principal:          {1}
    Duration:           {2}
    Pre-qualified?:     {3}

    Total:              {4}"""

WIDTH = 20

if TOTAL:
    print REPORT.format(NAME.title(),
                        ('$' + str('{:,}'.format(PRINCIPAL))).rjust(WIDTH),
                        (str(YEARS) + 'yrs').rjust(WIDTH),
                        QUALIFIED.title().rjust(WIDTH),
                        ('$' + str('{:,}'.format(TOTAL))).rjust(WIDTH))
else:
    print REPORT.format(NAME.title(),
                        ('$' + str('{:,}'.format(PRINCIPAL))).rjust(WIDTH),
                        (str(YEARS) + 'yrs').rjust(WIDTH),
                        QUALIFIED.title().rjust(WIDTH),
                        'None'.rjust(WIDTH))
