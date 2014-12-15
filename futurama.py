# -*- coding: utf-8 -*-
import csv
import os
import random

import logging

"""
Returns a tuple containing a header and a quote.

This code is placed in the public domain.
"""

quote_list = []
with open(os.path.dirname(__file__) + '/futurama.csv') as quotes:
    for quote in csv.reader(quotes):
        if len(quote) == 2:
            quote_list.append(quote)
if len(quote_list) == 0:
    quote_list.append(('Bender', "Well, we're boned!"))

def get_header():
    quote = quote_list[random.randrange(0,len(quote_list))]
    return ('X-%s' % quote[0].replace(' ', '-'), quote[1])

if __name__ == '__main__':
    print(get_header())
