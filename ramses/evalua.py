#! /usr/bin/env python3

import numpy as np
from mar import *
from util import *
from tqdm import tqdm

def evalua(dirRec, dirMar, *guiSen):
    matConf={}
    listPal = set()
    for sen in tqdm(leeLis(*guiSen)):
        patRec = pathName(dirRec, sen, 'rec')
        reconocidi = cogeTRN(patRec)
        patMar = pathName(dirMar, sen, 'mar')
        unidad = cogeTRN(patMar)
        if unidad not in matConf:
            matConf[unidad] = {}
        if reconocidi not in matConf [unidad]:
            matConf[unidad][reconocidi] = 0
        matConf[unidad][reconocidi] += 1
        listPal = listPal | {unidad, reconocidi}
    for unidad in sorted(listPal):
        print(f'\t{unidad}', end='')
    print()

    for unidad in sorted(listPal):
        print(unidad, end = '')
        for reconocidi in sorted(listPal):
            conf = matConf[unidad][reconocidi] if reconocidi in matConf[unidad] else 0
            print(f'\t{conf}', end = '')
        print()
    
    correctas = 0
    total = 0
    for unidad in matConf:
        for reconocidi in matConf[unidad]:
            total += matConf[unidad][reconocidi]
            if unidad == reconocidi:
                correctas += matConf[unidad][reconocidi]
    
    print(f'Porcentaje de acierto = {correctas/total:.2%}')

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
    --dirRec, -r PATH   directorio con los ficheros resultantes del reconocimiento
    --dirMar, -m PATH   directorio con las transcripciones de las señales [default: .]

Diccionario:
    <guiSen> fichero/s guia.
    roollo roollo rolololo. :)
"""
    args = docopt(sinopsis, version='tecparla2024 visionario')
    dirRec = args['--dirRec']
    dirMar = args['--dirMar']
    guiSen = args['<guiSen>']

    evalua(dirRec, dirMar, *guiSen)