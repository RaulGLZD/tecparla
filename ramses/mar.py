import re

def cogeTRN(pathMar):
    reLBO = re.compile(r'LBO:\s*\d*,\s*\d*,\s*\d*,\s*(?P<TRN>.*)')

    with open(pathMar,'rt') as fpMar:
        for linea in fpMar:
            if (match := reLBO.match(linea)):
                #match = reLBO.match(linea)
                return match ['TRN']