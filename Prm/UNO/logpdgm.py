import numpy as np
def logpdgm(x): 
  eps = 10
  return np.log(np.abs(np.fft.fft(x))+eps )
