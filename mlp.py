import torch

class Mlp_3(torch.nn.Module):
    def __init__(self, dimini = 32, dimint=128, dimsal=5):
        super().__init__()
        self.capa1