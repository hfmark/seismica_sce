import numpy as np
import biblib.bib as bbl
import sys

####
# run through a bibfile item by item and try to parse each; this will break at the point where an
# item is unparseable by biblib and will print the item that's causing problems so you can go find
# and fix it.
####

ifile = input('path to bibfile [./refs_better.bib]: ') or 'refs_better.bib'

f = open(ifile,'r')
text = f.read()
f.close()

items = text.split('@')[1:]

for bibitem in items:
    parser = bbl.Parser()
    try:
        parser.parse('@' + bibitem)
    except:
        print(bibitem)
        print('check your commas, brackets, parens, keys, etc')
        sys.exit()

print('all good!')
