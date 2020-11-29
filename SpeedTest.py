#!/usr/bin/env python3

from numba import jit, njit
from timeit import timeit
from ctypes import *
from time import strftime,localtime

import numpy as np
import numpy.ctypeslib as npct

from calMaCY   import calMaCY
from calMaAOT  import calMaAOT
from calMaPyC  import calMaPyC
from calMaPyCG import calMaPyC as calMaPyCG

loop = 5
subloop = 5
length = 1000000
#length = 10000
data = np.random.randint(1,2000000000,size=(length), dtype=np.int32)

dictTest ={
        'calMa'     : 'Standard Python Numpy',
        'calMaJIT'  : 'Numba JIT',
        'calMaAOT'  : 'Numba AOT',
        'calMaCY'   : 'Cython Module',
        'calMaPyC'  : 'C Module VC',
        'calMaPyCG' : 'C Module GCC',
        'calMaDLL'  : 'ctypes DLL VC',
        'calMaDLLG' : 'ctypes DLL GCC',
        'calMaOMP'  : 'ctypes DLL VC OpenMP',
}

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

def getSysInfo():
    name = ''
    output = ''
    try:
        from SysInfo import sysinfo
        dictInfo = sysinfo()
    except:
        print('Please install wmi using:\npip install wmi\n')
        return name, output
    output = '###### System Information \n'
    output += '||| \n'
    output += '|:---|:---| \n'
    for key in dictInfo:
        if key == 'Name':
            name = dictInfo[key]
            continue
        output += '{}|{} \n'.format(key,dictInfo[key])
    date = strftime("%Y-%m-%d %H:%M:%S", localtime()) 
    output += '{}|{} \n'.format('TIME', date)
    return name, output

def getTestInfo():
    global loop, subloop, length, data
    datatype = type(data[0])
    output = '###### Test Information \n'
    output += '||| \n'
    output += '|:---|:---| \n'
    output += '{}|{} * {}| \n'.format('Loop Number', loop, subloop)
    output += '{}|{:,}| \n'.format('Data Size', length)
    output += '{}|{}| \n'.format('Data Type', str(datatype).lstrip('<class').rstrip('>').strip().strip("'"))
    return output

def saveResult(result, loop):
    output = ''
    name, sysinfo = getSysInfo()
    output += sysinfo
    output += getTestInfo()
    output += '###### Test Result \n'
    t = ''
    for i in range(loop):
        t += '|{}'.format(i+1)
    output += '|Name|Infomation'+t+'|Avg|Faster| \n'
    output += '|:---|:---:'+'|---:'*(loop+2)+'| \n'
    for key in result:
        info = '|{}|{}'.format(key, result[key][0])
        for data in result[key][1:]:
            info += '|{}'.format('%.3f'%data)
        info += '| \n'
        output += info
    if name != '':
        filename ='Result_{}.md'.format(name)
    else:
        filename = 'Result.md'
    f = open(filename, 'w', encoding='utf-8')
    f.write(output)
    f.close()
    return

def main():
    global loop, subloop

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
    
    result = {}
    for key in dictTest:
        result[key] = [dictTest[key]]

    for i in range(loop):
        print('time : ', i+1)

        key = 'calMa'
        ret = timeit("calMa(data,100)", setup="from __main__ import calMa,data", number = subloop)
        print('%.10s : %s '%(key, ret))
        result[key].append(ret)
            
        key = 'calMaJIT'
        ret = timeit("calMaJIT(data,100)", setup="from __main__ import calMaJIT,data", number = subloop)
        print('%.10s : %s '%(key, ret))
        result[key].append(ret)
 
        key = 'calMaAOT'
        ret = timeit("calMaAOT(data,100)", setup="from __main__ import calMaAOT,data", number = subloop)
        print('%.10s : %s '%(key, ret))
        result[key].append(ret)
 
        key = 'calMaCY'
        ret = timeit("calMaCY(data,100)", setup="from __main__ import calMaCY,data", number = subloop)
        print('%.10s : %s '%(key, ret))
        result[key].append(ret)
 
        key = 'calMaPyC'
        ret = timeit("calMaPyC(data,100)", setup="from __main__ import calMaPyC,data", number = subloop)
        print('%.10s : %s '%(key, ret))
        result[key].append(ret)
 
        key = 'calMaPyCG'
        ret = timeit("calMaPyCG(data,100)", setup="from __main__ import calMaPyCG,data", number = subloop)
        print('%.10s : %s '%(key, ret))
        result[key].append(ret)
 
        key = 'calMaDLL'
        ret = timeit("calMaDLL(data,100)", setup="from __main__ import calMaDLL,data", number = subloop)
        print('%.10s : %s '%(key, ret))
        result[key].append(ret)
 
        key = 'calMaDLLG'
        ret = timeit("calMaDLLG(data,100)", setup="from __main__ import calMaDLLG,data", number = subloop)
        print('%.10s : %s '%(key, ret))
        result[key].append(ret)
 
        key = 'calMaOMP'
        ret = timeit("calMaOMP(data,100)", setup="from __main__ import calMaOMP,data", number = subloop)
        print('%.10s : %s '%(key, ret))
        result[key].append(ret)

    avgbase = sum(result['calMa'][1:])/loop
    for key in result:
        avg = sum(result[key][1:])/loop
        faster = avgbase/avg
        result[key].append(avg)
        result[key].append(faster)

    saveResult(result, loop)
    return

if __name__ == '__main__':
    main()
