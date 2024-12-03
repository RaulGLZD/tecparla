import numpy as np

def escrPrm(pathPrm, prm):
    with open(pathPrm, 'wb') as fpPrm:
        np.save(fpPrm, prm)

def leePrm(pathPrm):
    with open(pathPrm, 'rb') as fpPrm:
        prm = np.load(fpPrm)
        return prm 