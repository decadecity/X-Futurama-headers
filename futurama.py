import csv, os, random, sys

"""
Returns a tuple containing a header and a quote.

This code is placed in the public domain.
"""

def get_header():
    quote_list = []
    for quote in csv.reader(open(os.path.dirname(__file__)+'/futurama.csv')):
        if len(quote) == 2:
            quote_list.append(quote)
    if len(quote_list) == 0:
        quote_list.append(('Bender','Well, we\'re boned!'))
    quote = quote_list[random.randrange(0,len(quote_list))]
    return ('X-%s' % quote[0].replace(' ','-'),quote[1])

if __name__ == '__main__':
    print get_header()
