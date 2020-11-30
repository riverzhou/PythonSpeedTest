###### System Information 
||| 
|:---|:---| 
|OS|Microsoft Windows 10 家庭中文版 18363 64 位| 
|CPU|Intel(R) Core(TM) i5-10210U CPU @ 1.60GHz # Threads : 8| 
|GPU 0|NVIDIA GeForce MX350 # 27.21.14.5730| 
|GPU 1|Intel(R) UHD Graphics # 27.20.100.8935| 
|MEM|8192 MB + 8192 MB  = 16384 MB| 
|TIME|2020-11-30 22:27:05| 
###### Test Information 
||| 
|:---|:---| 
|Loop Number|5 * 5| 
|Data Size|1,000,000| 
|Window Size|100| 
|Data Type|numpy.int32| 
###### Test Result 
|Name|Infomation|1|2|3|4|5|Avg|Faster| 
|:---|:---:|---:|---:|---:|---:|---:|---:|---:| 
|calMa|Standard Python Numpy|24.500|24.966|24.126|24.108|24.134|24.367|1.000| 
|calMaCov|Python Numpy Convolve|0.183|0.182|0.186|0.185|0.182|0.184|132.772| 
|calMaOpt|Numpy Optimized Ma|5.372|5.299|5.385|5.481|5.248|5.357|4.548| 
|calMaJIT|Numba JIT|0.169|0.169|0.170|0.171|0.171|0.170|143.386| 
|calMaAOT|Numba AOT|0.470|0.467|0.469|0.468|0.470|0.469|51.970| 
|calMaCY|Cython Module|23.951|24.144|23.920|23.799|23.845|23.932|1.018| 
|calMaPyC|C Module VC|0.103|0.105|0.106|0.103|0.106|0.105|233.026| 
|calMaPyCG|C Module GCC|0.130|0.130|0.131|0.130|0.130|0.130|187.001| 
|calMaDLL|ctypes DLL VC|0.104|0.104|0.107|0.102|0.099|0.103|236.446| 
|calMaDLLG|ctypes DLL GCC|0.130|0.131|0.130|0.136|0.135|0.133|183.864| 
|calMaOMP|ctypes DLL VC OpenMP|0.027|0.027|0.027|0.028|0.028|0.027|888.457| 
