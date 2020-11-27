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

data = np.random.randint(1,2000000000,size=(1000000), dtype=np.int32)

dlllib = npct.load_library("calMaDLL",".")
dlllib.calMaDLL.argtypes = [npct.ndpointer(dtype=np.int, ndim=1, flags="C_CONTIGUOUS"), npct.ndpointer(dtype=np.float64, ndim=1, flags="C_CONTIGUOUS"), c_int, c_int]

dlllib_gcc = npct.load_library("calMaDLL_gcc",".")
dlllib_gcc.calMaDLL.argtypes = [npct.ndpointer(dtype=np.int, ndim=1, flags="C_CONTIGUOUS"), npct.ndpointer(dtype=np.float64, ndim=1, flags="C_CONTIGUOUS"), c_int, c_int]

omplib = npct.load_library("calMaOMP",".")
omplib.calMaDLL.argtypes = [npct.ndpointer(dtype=np.int, ndim=1, flags="C_CONTIGUOUS"), npct.ndpointer(dtype=np.float64, ndim=1, flags="C_CONTIGUOUS"), c_int, c_int]

def calMaOMP(d, window):
    global omplib
    n = d.size
    #m = np.zeros(n, dtype=np.float64)
    m = np.empty((n,), dtype=np.float64)
    omplib.calMaDLL(data, m, n, window)
    return m
    
def calMaDLLG(d, window):
    global dlllib_gcc
    n = d.size
    #m = np.zeros(n, dtype=np.float64)
    m = np.empty((n,), dtype=np.float64)
    dlllib_gcc.calMaDLL(data, m, n, window)
    return m

def calMaDLL(d, window):
    global dlllib
    n = d.size
    #m = np.zeros(n, dtype=np.float64)
    m = np.empty((n,), dtype=np.float64)
    dlllib.calMaDLL(data, m, n, window)
    return m

@njit
def calMaJIT(d, window):
    adjust = int(window/2)

    n = d.size
    m = np.zeros(n, dtype=np.float64)
    for i in range(n-window):
        m[i+adjust] = np.sum(d[i:i+window],dtype=np.int64)/window
    return m

def calMa(d, window):
    adjust = int(window/2)

    n = d.size
    m = np.zeros(n, dtype=np.float64)
    for i in range(n-window):
        m[i+adjust] = np.sum(d[i:i+window],dtype=np.int64)/window
    return m

def printDiff(d1,d2):
    n = d1.size
    for i in range(n):
        if d1[i] != d2[i]:
            print(i,d1[i],d2[i])
            
def checkRet(data):
    number = len(data)
    for i in range(number-1):
        for n in range(i+1,number):
            if (data[i].size != data[n].size):
                print('checkRet size difference')
                return False
    print('checkRet size', data[0].size)
    for i in range(number-1):
        for n in range(i+1,number):
            if ((data[i]==data[n]).all() != True):            
                print('checkRet result False:', i, n)
                print(type(data[i][0]), type(data[n][0]))
                printDiff(data[i], data[n])
                return False
    print('checkRet result True')
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
    ret_calMaOMP  = calMaOMP(data,100)

    ret = checkRet([ret_calMa, ret_calMaJIT, ret_calMaAOT, ret_calMaCY, ret_calMaPyC, ret_calMaPyCG, ret_calMaDLL, ret_calMaDLLG, ret_calMaOMP])
    if ret != True:
        return
    
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
        print('calMaOMP ', timeit("calMaOMP(data,100)", setup="from __main__ import calMaOMP,data", number = 5))
    return

if __name__ == '__main__':
    main()
