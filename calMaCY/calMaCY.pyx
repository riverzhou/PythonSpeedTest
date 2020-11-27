# cython: language_level=3

import numpy as np
cimport numpy as np
cimport cython

@cython.boundscheck(False)
@cython.wraparound(False)
cdef np.ndarray[double, ndim=1] _calMaCY(np.ndarray[long, ndim=1] d, long window):
    cdef int adjust
    cdef np.ndarray[double, ndim=1] m

    adjust = int(window/2)
    m = np.zeros(len(d),dtype=np.float64)
    for i in range(len(d)-window):
        m[i+adjust] = np.sum(d[i:i+window], dtype=np.int64)/window
    return m

def calMaCY(d, window):
    return _calMaCY(d, window)
