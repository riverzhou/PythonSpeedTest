# PythonSpeedTest
 Python Speed Test: Numpy Numba(JIT,AOT) Cython C_mod ctypes OpenMP

Test Result (input len 1M np.int32 and size 100 window calculate Ma):

calMa     28.118967800000007  
calMaJIT  0.18587259999999617  
calMaAOT  0.3405309000000045  
calMaCY   26.882370500000007  
calMaPyC  0.12137590000000387  
calMaPyCG 0.14699559999999678  
calMaDLL  0.12071720000000141  
calMaDLLG 0.1485512  
calMaOMP  0.03555489999999395  

