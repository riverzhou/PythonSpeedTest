#!/usr/bin/env python3

from numba.pycc import CC
from numba import jit, njit
import numpy as np
 
cc = CC('calMaAOT')

cc.verbose = True

@cc.export('calMaAOT','f8[:](i4[:],i4)')
def calMaAOT(d, window):
    adjust = int(window/2)

    m = np.zeros(len(d),dtype=np.float64)
    for i in range(len(d)-window):
        m[i+adjust] = np.sum(d[i:i+window])/window
    return m


if __name__ == "__main__":
    cc.compile() 
