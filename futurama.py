# -*- coding: utf-8 -*-
from csv import reader as csv_reader
from os.path import join as path_join, dirname as path_dirname
from random import randrange as random_randrange

"""
Returns a tuple containing a header and a quote.

This code is placed in the public domain.
"""

quote_list = []
try:
    for quote in csv_reader(open(path_join(path_dirname(__file__), 'futurama.csv'))):
        if len(quote) == 2:
            quote_list.append(quote)
except IOError:
    pass
if len(quote_list) == 0:
    quote_list.append(('Bender', "Well, we're boned!"))

def get_header():
    quote = quote_list[random_randrange(0,len(quote_list))]
    return ('X-%s' % quote[0].replace(' ', '-'), quote[1])

if __name__ == '__main__':
    print(get_header())

