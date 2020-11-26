#!/usr/bin/env python3

from numba import jit, njit
from timeit import timeit
from ctypes import *

import numpy as np
import numpy.ctypeslib as npct

from calMaCY   import calMaCY
from calMaAOT  import calMaAOT
from calMaPyC  import calMaPyC
from calMaPyCG import calMaPyC as calMaPyCG

data = np.random.randint(1,10000,size=(100000), dtype=np.int32)

dlllib = npct.load_library("calMaDLL",".")
dlllib.calMaDLL.argtypes = [npct.ndpointer(dtype=np.int, ndim=1, flags="C_CONTIGUOUS"), npct.ndpointer(dtype=np.float64, ndim=1, flags="C_CONTIGUOUS"), c_int, c_int]

dlllib_gcc = npct.load_library("calMaDLL_gcc",".")
dlllib_gcc.calMaDLL.argtypes = [npct.ndpointer(dtype=np.int, ndim=1, flags="C_CONTIGUOUS"), npct.ndpointer(dtype=np.float64, ndim=1, flags="C_CONTIGUOUS"), c_int, c_int]

def calMaDLLG(d, window):
    global dlllib_gcc
    n = len(d)
    #m = np.zeros(n, dtype=np.float64)
    m = np.empty((n,), dtype=np.float64)
    dlllib_gcc.calMaDLL(data, m, n, window)
    return m

def calMaDLL(d, window):
    global dlllib
    n = len(d)
    #m = np.zeros(n, dtype=np.float64)
    m = np.empty((n,), dtype=np.float64)
    dlllib.calMaDLL(data, m, n, window)
    return m

@njit
def calMaJIT(d, window):
    adjust = int(window/2)

    m = np.zeros(len(d), dtype=np.float64)
    for i in range(len(d)-window):
        m[i+adjust] = np.sum(d[i:i+window])/window
    return m

def calMa(d, window):
    adjust = int(window/2)

    m = np.zeros(len(d), dtype=np.float64)
    for i in range(len(d)-window):
        m[i+adjust] = np.sum(d[i:i+window])/window
    return m

def checkRet(data):
    number = len(data)
    for i in range(number-1):
        for n in range(i+1,number):
            if ((data[i]==data[n]).all() != True):
                return False
    return True

def main():
    ret_calMa     = calMa(data,100)
    ret_calMaJIT  = calMaJIT(data,100)
    ret_calMaAOT  = calMaAOT(data,100)
    ret_calMaCY   = calMaCY(data,100)
    ret_calMaPyC  = calMaPyC(data,100)
    ret_calMaPyCG = calMaPyCG(data,100)
    ret_calMaDLL  = calMaDLL(data,100)
    ret_calMaDLLG = calMaDLLG(data,100)

    print(ret_calMa.shape, ret_calMaJIT.shape, ret_calMaAOT.shape, ret_calMaCY.shape, ret_calMaPyC.shape, ret_calMaPyCG.shape, ret_calMaDLL.shape, ret_calMaDLLG.shape)
    ret = checkRet([ret_calMa, ret_calMaJIT, ret_calMaAOT, ret_calMaCY, ret_calMaPyC, ret_calMaPyCG, ret_calMaDLL, ret_calMaDLLG])
    print('check ret : ', ret)

    #return
    
    for i in range(3):
        print('time:', i+1)
        print('calMa    ', timeit("calMa(data,100)", setup="from __main__ import calMa,data", number = 5))
        print('calMaJIT ', timeit("calMaJIT(data,100)", setup="from __main__ import calMaJIT,data", number = 5))
        print('calMaAOT ', timeit("calMaAOT(data,100)", setup="from __main__ import calMaAOT,data", number = 5))
        print('calMaCY  ', timeit("calMaCY(data,100)", setup="from __main__ import calMaCY,data", number = 5))
        print('calMaPyC ', timeit("calMaPyC(data,100)", setup="from __main__ import calMaPyC,data", number = 5))
        print('calMaPyCG', timeit("calMaPyCG(data,100)", setup="from __main__ import calMaPyCG,data", number = 5))
        print('calMaDLL ', timeit("calMaDLL(data,100)", setup="from __main__ import calMaDLL,data", number = 5))
        print('calMaDLLG', timeit("calMaDLLG(data,100)", setup="from __main__ import calMaDLLG,data", number = 5))
    return

if __name__ == '__main__':
    main()
