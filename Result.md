###### System Information 
||| 
|:---|:---| 
OS|Microsoft Windows 10 家庭中文版 18363 64 位 
CPU|Intel(R) Core(TM) i5-8265U CPU @ 1.60GHz # Threads : 8 
MEM|4096 MB + 4096 MB  = 8192 MB 
TIME|2020-11-29 12:44:44 
###### Test Information 
||| 
|:---|:---| 
Loop Number|5 * 5| 
Data Size|1000000| 
Data Type|numpy.int32| 
###### Test Result 
|Name|Infomation|1|2|3|4|5|Avg|Faster| 
|:---|:---:|---:|---:|---:|---:|---:|---:|---:| 
|calMa|Stand Python Numpy|26.955|27.436|27.337|26.768|28.286|27.356|1.000| 
|calMaJIT|Numba JIT|0.188|0.188|0.188|0.188|0.196|0.190|144.241| 
|calMaAOT|Numba AOT|0.328|0.329|0.331|0.333|0.336|0.332|82.492| 
|calMaCY|Cython Module|26.487|26.682|26.929|26.732|26.676|26.701|1.025| 
|calMaPyC|C Module VC|0.124|0.125|0.125|0.126|0.129|0.126|217.494| 
|calMaPyCG|C Module GCC|0.155|0.153|0.152|0.152|0.156|0.154|177.918| 
|calMaDLL|ctypes DLL VC|0.126|0.126|0.121|0.125|0.121|0.124|221.115| 
|calMaDLLG|ctypes DLL GCC|0.152|0.152|0.146|0.152|0.152|0.151|181.183| 
|calMaOMP|ctypes DLL VC OpenMP|0.049|0.048|0.045|0.049|0.046|0.047|576.300| 
