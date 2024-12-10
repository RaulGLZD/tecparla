import numpy as np
def ceps(x): 
  numCoef = 32
  eps = 10
  ceps = np.fft.ifft(np.log(np.abs(np.fft.fft(x))+eps ))
  return np.real(ceps[1:numCoef])
