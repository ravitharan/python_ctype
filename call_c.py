import ctypes
import numpy as np
from multiprocessing import shared_memory
import pprint

FILE_PATH_LEN = 256

DATA_COUNT = 100

class Parameter(ctypes.Structure):
    _fields_ = [
        ("shm_file", ctypes.c_char * FILE_PATH_LEN),
        ("count", ctypes.c_int),
        ("multiplier", ctypes.c_float),
    ]

in_size     = DATA_COUNT * np.dtype('int32').itemsize
out_size    = DATA_COUNT * np.dtype('float32').itemsize
total_size  = in_size + out_size

shm = shared_memory.SharedMemory(create=True, size=total_size)

print(f'shm name {shm.name}')

in_data     = np.frombuffer(shm.buf, dtype=np.int32, offset=0)
out_data    = np.frombuffer(shm.buf, dtype=np.float32, offset=in_size)

# Fill input data
for i in range(len(in_data)):
    in_data[i] = i

lib = ctypes.cdll.LoadLibrary('./c/libfoo.so')

foo             = lib.foo
foo.argtypes    = [ctypes.POINTER(Parameter)]
foo.restype     = ctypes.c_int

shm_name = ctypes.create_string_buffer(shm.name.encode(), FILE_PATH_LEN)
param = Parameter(shm_name.raw, DATA_COUNT, 0.0)
ret = foo(ctypes.byref(param))
if (ret != 0):
    print('Error in calling foo()')
    exit(1)
pprint.pprint(out_data)

param.multiplier = 0.1
ret = foo(ctypes.byref(param))
pprint.pprint(out_data)

param.multiplier = 0.5
ret = foo(ctypes.byref(param))
pprint.pprint(out_data)

shm.close()
shm.unlink()




