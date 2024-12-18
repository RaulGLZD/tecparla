import numpy as np
import torch
from util import *
from torch.nn.functional import nll_loss
from torch.optim import SGD


class RedPT:
    def __init__(self, * , lisFon=None, ficMod=None, red=None, funcLoss=nll_loss,
                 Optim=lambda params: SGD(params, lr=1e-5) ):
        if lisFon and ficMod or not (lisFon or ficMod):
            raise("ERROR: lisFon o ficMod han de ser distintos de None")
        if lisFon: 
            self.unidades = leeLis(lisFon)
            self.red = red
            self.red.unidades = self.unidades


        else:
            self.leeMod(ficMod)
        self.funcLoss = funcLoss
        self.optim = Optim(self.red.parameters())

    def leeMod(self, ficMod):
        self.red = torch.jit.load(ficMod)

    def escMod(self, ficMod):
        chkPathName(ficMod)
        torch.jit.script(self.red).save(ficMod)

    def inicMod(self):
        self.optim.zero_grad()
    
    def addPrm(self, prm, unidad):
        # print(f"{prm=}")
        salida = self.red(prm).swapdims(1,2)
        loss = self.funcLoss(salida, torch.tensor([self.unidades.index(unidad)]))
        loss.backward()
        return self

    def recaMod(self):
        self.optim.step()

    def printEvo(self):
        print()


    def __call__(self, prm):
        return self.red.unidades[self.red(prm).argmax()]
        