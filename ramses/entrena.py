#! /usr/bin/env python3

import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
from ramses.util import *
from ramses.mar import *
from ramses.prm import *
from euclideo import Euclidi
from tqdm import tqdm

def entrena(dirPrm, dirMar, lisFon, ficMod, *figGui):
    #CONSTRUIMOS el modelo inical
    modelo = Euclidi(lisFon)
    #INICIALIZAMOS las estructuras iniciales para el entrenamiento
    modelo.inicMod()

    #BUCLE para todas las señales
    for señal in tqdm(leeLis(*figGui)):
        pathMar = pathName(dirMar, señal, 'mar')
        unidad = cogeTRN(pathMar)
        pathPrm = pathName(dirPrm, señal, 'prm')
        prm = leePrm(pathPrm)
        #INCORPORAMOS la informacion de la señal al modelo
        modelo.addPrm(prm, unidad)
    #RECALCULAMOS el modelo
    modelo.recaMod()
    #MOSTRAMOS en pantalla la evolucion del entrenamiento
    modelo.printEvo()

    #ESCRIBIMOS el modelo generado
    modelo.escMod(ficMod)

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