#! /usr/bin/python3

import numpy as np
from ramses.util import *
from ramses.prm import *
from tqdm import tqdm

def reconoce(dirRec, dirPrm, ficMod, *guiSen):
    modelos = np.load(ficMod, allow_pickle=True).item()
    for sen in tqdm(leeLis(*guiSen)):
        pathPrm = pathName(dirPrm, sen, 'prm')
        prm = leePrm(pathPrm)
        minDist = np.inf
        for unidad in modelos:
            distancia = sum((prm - modelos[unidad])**2)
            if distancia < minDist:
                minDist = distancia
                reconocidi = unidad
        pathRec = pathName(dirRec, sen, 'rec')
        chkPathName(pathRec)
        with open(pathRec, 'wt') as fpRec:
            fpRec.write(f'LBO: , , , {reconocidi}\n')

if __name__ == '__main__':
    from docopt import docopt
    import sys 

    sinopsis = f"""
Evalua el resultado de un experimento de reconocimiento

Usage:
    {sys.argv[0]} [options] <guiSen>...
    {sys.argv[0]} -h | --help
    {sys.argv[0]} --version

Opciones:
    --ficMod, -f PATH   fichero modificado
    --dirRec, -r PATH   directorio con los ficheros resultantes del reconocimiento
    --dirPrm, -p PATH   directorio con las transcripciones de las señales [default: .]

Diccionario:
    <guiSen> fichero/s guia.
    roollo roollo rolololo. :)
"""
    args = docopt(sinopsis, version='tecparla2024 visionario')
    dirRec = args['--dirRec']
    dirPrm = args['--dirPrm']
    ficMod = args['--ficMod']
    guiSen = args['<guiSen>']

    reconoce(dirRec, dirPrm, ficMod, *guiSen)