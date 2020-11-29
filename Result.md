###### System Information 
||| 
|:---|:---| 
|OS|Microsoft Windows 10 家庭中文版 18363 64 位| 
|CPU|Intel(R) Core(TM) i5-10210U CPU @ 1.60GHz # Threads : 8| 
|GPU 0|NVIDIA GeForce MX350 # 27.21.14.5730| 
|GPU 1|Intel(R) UHD Graphics # 27.20.100.8935| 
|MEM|8192 MB + 8192 MB  = 16384 MB| 
|TIME|2020-11-29 20:28:01| 
###### Test Information 
||| 
|:---|:---| 
|Loop Number|5 * 5| 
|Data Size|1,000,000| 
|Data Type|numpy.int32| 
###### Test Result 
|Name|Infomation|1|2|3|4|5|Avg|Faster| 
|:---|:---:|---:|---:|---:|---:|---:|---:|---:| 
|calMa|Standard Python Numpy|25.075|24.789|24.982|24.824|24.915|24.917|1.000| 
|calMaJIT|Numba JIT|0.172|0.172|0.170|0.170|0.176|0.172|144.953| 
|calMaAOT|Numba AOT|0.471|0.467|0.467|0.469|0.471|0.469|53.130| 
|calMaCY|Cython Module|24.374|24.179|24.759|24.178|25.163|24.531|1.016| 
|calMaPyC|C Module VC|0.105|0.104|0.107|0.103|0.109|0.106|235.672| 
|calMaPyCG|C Module GCC|0.147|0.142|0.141|0.141|0.141|0.143|174.733| 
|calMaDLL|ctypes DLL VC|0.106|0.104|0.108|0.103|0.106|0.105|236.188| 
|calMaDLLG|ctypes DLL GCC|0.119|0.122|0.114|0.124|0.121|0.120|207.944| 
|calMaOMP|ctypes DLL VC OpenMP|0.033|0.034|0.029|0.029|0.030|0.031|802.367| 
