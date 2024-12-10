#! /usr/bin/env python3

import soundfile as sf
import numpy as np
from ramses.util import *
from ramses.prm import *
from tqdm import tqdm


def parametriza(dirPrm, dirSen, *guiSen, funcPrm=np.array):
    for fichero in tqdm(leeLis(*guiSen)):
        pathSen = pathName(dirSen, fichero, 'wav')
        sen, fm = sf.read(pathSen)
        prm = funcPrm(sen)
        pathPrm = pathName(dirPrm, fichero, 'prm')
        chkPathName(pathPrm)
        escrPrm(pathPrm, prm)
    
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
    --dirPrm, -p PATH   directorio con las señales parametrizadas
    --dirSen, -s PATH   directorio con las señales de entrada
    --execPre,-x SCRIPTS  scripts a ejecutar antes de la parametrizacion
    --funcPrm,-f EXPR   Expresion que proporciona la funcion de parametrizacion [default: np.array]
Diccionario:
    <guiSen> fichero/s guia.
    roollo roollo rolololo. :)
"""
    args = docopt(sinopsis, version='tecparla2024 visionario')
    dirPrm = args['--dirPrm']
    dirSen = args['--dirSen']
    guiSen = args['<guiSen>']
    
    scripts = args['--execPre']
    if scripts:
        for script in scripts.split(','):
            exec(open(script).read())
    
    funcPrm =eval(args['--funcPrm'])

    parametriza(dirPrm, dirSen, *guiSen, funcPrm=funcPrm)