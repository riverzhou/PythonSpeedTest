###### System Information 
||| 
|:---|:---| 
OS|Microsoft Windows 10 家庭中文版 18363 64 位 
CPU|Intel(R) Core(TM) i5-10210U CPU @ 1.60GHz # Threads : 8 
GPU 0|NVIDIA GeForce MX350 # 27.21.14.5730 
GPU 1|Intel(R) UHD Graphics # 27.20.100.8935 
MEM|8192 MB + 8192 MB  = 16384 MB 
TIME|2020-11-29 19:46:21 
###### Test Information 
||| 
|:---|:---| 
Loop Number|5 * 5| 
Data Size|1,000,000| 
Data Type|numpy.int32| 
###### Test Result 
|Name|Infomation|1|2|3|4|5|Avg|Faster| 
|:---|:---:|---:|---:|---:|---:|---:|---:|---:| 
|calMa|Standard Python Numpy|24.126|23.933|24.144|24.602|24.707|24.302|1.000| 
|calMaJIT|Numba JIT|0.172|0.174|0.171|0.178|0.174|0.174|140.027| 
|calMaAOT|Numba AOT|0.470|0.470|0.468|0.481|0.470|0.472|51.521| 
|calMaCY|Cython Module|24.193|23.953|23.930|24.946|25.860|24.576|0.989| 
|calMaPyC|C Module VC|0.103|0.104|0.107|0.106|0.105|0.105|230.919| 
|calMaPyCG|C Module GCC|0.142|0.148|0.141|0.145|0.145|0.144|168.438| 
|calMaDLL|ctypes DLL VC|0.103|0.104|0.102|0.110|0.103|0.105|232.214| 
|calMaDLLG|ctypes DLL GCC|0.119|0.118|0.119|0.117|0.114|0.117|207.009| 
|calMaOMP|ctypes DLL VC OpenMP|0.033|0.036|0.030|0.033|0.032|0.033|736.860| 
