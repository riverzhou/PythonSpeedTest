###### Test Information 
||| 
|:---|:---| 
Loop Number|5 * 5| 
Data Size|1000000| 
Data Type|numpy.int32| 
###### Test Result 
|Name|Infomation|1|2|3|4|5|Avg|Faster| 
|:---|:---:|---:|---:|---:|---:|---:|---:|---:| 
|calMa|Stand Python Numpy|25.689|27.178|29.007|26.948|28.332|27.431|1.000| 
|calMaJIT|Numba JIT|0.180|0.179|0.189|0.182|0.185|0.183|149.923| 
|calMaAOT|Numba AOT|0.484|0.493|0.497|0.488|0.499|0.492|55.724| 
|calMaCY|Cython Module|28.843|27.569|27.298|26.312|29.308|27.866|0.984| 
|calMaPyC|C Module VC|0.119|0.114|0.113|0.110|0.121|0.115|237.594| 
|calMaPyCG|C Module GCC|0.152|0.150|0.146|0.149|0.167|0.153|179.624| 
|calMaDLL|ctypes DLL VC|0.115|0.116|0.108|0.109|0.121|0.114|241.226| 
|calMaDLLG|ctypes DLL GCC|0.128|0.135|0.125|0.125|0.141|0.131|209.277| 
|calMaOMP|ctypes DLL VC OpenMP|0.039|0.033|0.033|0.048|0.038|0.038|721.621| 
