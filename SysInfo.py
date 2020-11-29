#!/usr/bin/env python3

import wmi
from multiprocessing import cpu_count

def sysinfo():
    c = wmi.WMI ()
    dictRet = {}
    for sys in c.Win32_OperatingSystem():
        #print('OS  : {} {} {}'.format(sys.Caption,sys.BuildNumber,sys.OSArchitecture))
        dictRet['OS'] = '{} {} {}'.format(sys.Caption,sys.BuildNumber,sys.OSArchitecture)
    for processor in c.Win32_Processor():
        #print('CPU : {} | Threads : {}'.format(processor.Name.strip(), cpu_count()))
        dictRet['CPU'] = '{} # Threads : {}'.format(processor.Name.strip(), cpu_count())
    listGPU = []
    for gpu in c.Win32_VideoController():
        listGPU.append('{} # {}'.format(gpu.Name, gpu.DriverVersion))
    if len(listGPU) == 1:
        dictRet['GPU'] = listGPU[0]
    if len(listGPU) > 1:
        for i in range(len(listGPU)):
            dictRet['GPU {}'.format(i)] = listGPU[i]
    listMemory = []
    for Memory in c.Win32_PhysicalMemory():
        listMemory.append(int(Memory.Capacity))
    output = ''
    for m in listMemory:
        output += '{} MB + '.format(int(m/(1024*1024)))
    output = output.rstrip().rstrip('+') + ' = {} MB'.format(int(sum(listMemory)/(1024*1024)))
    #print('MEM : '+output)
    dictRet['MEM'] = output
    for n in c.Win32_ComputerSystem():
        dictRet['Name'] = n.name.replace(' ','_')
    return dictRet

def main():
    dictInfo = sysinfo()
    for key in dictInfo:
        print('{:6}: {}'.format(key, dictInfo[key]))

if __name__ == '__main__':
    main()

