from ctypes import *
from ctypes.wintypes import *
import subprocess
import time

kernel32 = windll.kernel32

SIZE_T = c_size_t

process = subprocess.Popen(["notepad.exe"])
time.sleep(2)

OpenProcess = kernel32.OpenProcess
OpenProcess.argtypes = (DWORD, BOOL, DWORD)
OpenProcess.restype = HANDLE

GetModuleHandleA = kernel32.GetModuleHandleA
GetModuleHandleA.argtypes = (LPCSTR,)
GetModuleHandleA.restype = HANDLE

GetProcAddress = kernel32.GetProcAddress
GetProcAddress.argtypes = (HANDLE, LPCSTR)
GetProcAddress.restype = LPVOID

PROCESS_QUERY_INFORMATION = 0x0400
PROCESS_VM_READ = 0x0010

PID = process.pid

Process_Handle = OpenProcess(
    PROCESS_QUERY_INFORMATION | PROCESS_VM_READ,
    False,
    PID
)

print(f'Process ID => {PID}')
print(f'Process Handle => {Process_Handle}')

Module_Handle = GetModuleHandleA(b'kernel32.dll')
print(f'Kernel32 Module Handle => {hex(Module_Handle)}')

Load_Lib = GetProcAddress(
    Module_Handle,
    b'LoadLibraryA'
)

print(f'LoadLibraryA Address => {hex(Load_Lib)}')

process.terminate()
process.wait()

print('Process closed.')
