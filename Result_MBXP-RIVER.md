###### System Information 
||| 
|:---|:---| 
|OS|Microsoft Windows 10 家庭中文版 18363 64 位| 
|CPU|Intel(R) Core(TM) i5-8265U CPU @ 1.60GHz # Threads : 8| 
|GPU 0|NVIDIA GeForce MX250 # 27.21.14.5730| 
|GPU 1|Intel(R) UHD Graphics 620 # 27.20.100.8681| 
|MEM|4096 MB + 4096 MB  = 8192 MB| 
|TIME|2020-11-30 10:51:42| 
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
|calMa|Standard Python Numpy|26.578|27.738|28.411|28.063|29.183|27.995|1.000| 
|calMaJIT|Numba JIT|0.189|0.201|0.199|0.193|0.203|0.197|142.223| 
|calMaAOT|Numba AOT|0.327|0.338|0.342|0.342|0.353|0.341|82.194| 
|calMaCY|Cython Module|26.779|27.553|27.794|27.904|28.130|27.632|1.013| 
|calMaPyC|C Module VC|0.128|0.120|0.123|0.125|0.129|0.125|224.040| 
|calMaPyCG|C Module GCC|0.154|0.154|0.152|0.158|0.158|0.155|180.519| 
|calMaDLL|ctypes DLL VC|0.126|0.122|0.124|0.125|0.127|0.125|224.090| 
|calMaDLLG|ctypes DLL GCC|0.155|0.152|0.155|0.155|0.158|0.155|180.667| 
|calMaOMP|ctypes DLL VC OpenMP|0.038|0.047|0.047|0.045|0.060|0.047|591.918| 
