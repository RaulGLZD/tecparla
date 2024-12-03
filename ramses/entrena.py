#! /usr/bin/python3

import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
from ramses.util import *
from ramses.mar import *
from ramses.prm import *
from tqdm import tqdm

def entrena(dirPrm, dirMar, lisFon, ficMod, *figGui):
    unidades = leeLis(lisFon)
    total = {unidad : 0 for unidad in unidades}
    numFon = {unidad : 0 for unidad in unidades}
    modelo = {}
    for señal in tqdm(leeLis(*figGui)):
        pathMar = pathName(dirMar, señal, 'mar')
        unidad = cogeTRN(pathMar)
        pathPrm = pathName(dirPrm, señal, 'prm')
        prm = leePrm(pathPrm)
        total[unidad] += prm
        numFon[unidad] += 1
    for unidad in unidades: 
        modelo[unidad] = total[unidad] / numFon[unidad]
    chkPathName(ficMod)
    with open(ficMod, 'wb' ) as fpMod:
        np.save(fpMod, modelo)

if __name__ == '__main__':
    from docopt import docopt
    import sys 

    sinopsis = f"""
Evalua el resultado de un experimento de reconocimiento

Usage:
    {sys.argv[0]} [options] <figGui>...
    {sys.argv[0]} -h | --help
    {sys.argv[0]} --version

Opciones:
    --ficMod, -f PATH   fichero modificado
    --dirPrm, -p PATH   directorio con los ficheros resultantes del reconocimiento
    --dirMar, -m PATH   directorio con las transcripciones de las señales [default: .]
    --lisFon, -l PATH  blablabla
    

Diccionario:
    <figGui> fichero/s guia.
    roollo roollo rolololo. :)
"""
    args = docopt(sinopsis, version='tecparla2024 visionario')
    dirPrm = args['--dirPrm']
    lisFon = args['--lisFon']
    dirMar = args['--dirMar']
    ficMod = args['--ficMod']
    figGui = args['<figGui>']

    entrena(dirPrm, dirMar,lisFon, ficMod, *figGui)