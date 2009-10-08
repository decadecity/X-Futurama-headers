import csv, os, random, sys

def get_header():
    quote_list = []
    for quote in csv.reader(open(sys.path[0]+'/futurama.csv')):
        if len(quote) == 2:
            quote_list.append(quote)
    quote = quote_list[random.randrange(0,len(quote_list))]
    return ('X-%s' % quote[0].replace(' ','-'),quote[1])

if __name__ == '__main__':
    print get_header()
