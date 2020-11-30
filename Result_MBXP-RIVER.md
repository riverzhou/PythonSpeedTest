###### System Information 
||| 
|:---|:---| 
|OS|Microsoft Windows 10 家庭中文版 18363 64 位| 
|CPU|Intel(R) Core(TM) i5-8265U CPU @ 1.60GHz # Threads : 8| 
|GPU 0|NVIDIA GeForce MX250 # 27.21.14.5730| 
|GPU 1|Intel(R) UHD Graphics 620 # 27.20.100.8681| 
|MEM|4096 MB + 4096 MB  = 8192 MB| 
|TIME|2020-11-30 15:37:53| 
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
|calMa|Standard Python Numpy|27.201|28.249|28.570|30.014|30.586|28.924|1.000| 
|calMaCov|Python Numpy Convolve|0.221|0.228|0.229|0.258|0.250|0.237|121.835| 
|calMaJIT|Numba JIT|0.195|0.197|0.205|0.242|0.235|0.215|134.619| 
|calMaAOT|Numba AOT|0.343|0.352|0.356|0.396|0.385|0.366|78.961| 
|calMaCY|Cython Module|27.118|27.531|27.771|30.420|30.067|28.581|1.012| 
|calMaPyC|C Module VC|0.126|0.125|0.124|0.140|0.141|0.131|220.221| 
|calMaPyCG|C Module GCC|0.154|0.157|0.157|0.182|0.179|0.166|174.497| 
|calMaDLL|ctypes DLL VC|0.130|0.125|0.127|0.141|0.144|0.133|216.865| 
|calMaDLLG|ctypes DLL GCC|0.151|0.149|0.141|0.166|0.162|0.154|188.072| 
|calMaOMP|ctypes DLL VC OpenMP|0.052|0.044|0.055|0.052|0.053|0.051|563.897| 
