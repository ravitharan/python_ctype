import ctypes
import numpy as np
import pprint

class Parameter(ctypes.Structure):
    _fields_ = [
        ("count", ctypes.c_int),
        ("input", ctypes.c_void_p),
        ("output", ctypes.c_void_p),
    ]

lib = ctypes.cdll.LoadLibrary('./c/libfoo.so')

foo             = lib.foo
foo.argtypes    = [ctypes.POINTER(Parameter)]
foo.restype     = ctypes.c_int

count = 100

in_data = np.arange(count, dtype=np.int32)
in_ptr = in_data.ctypes.data_as(ctypes.c_void_p)

out_data = np.zeros(count, dtype=np.single)
out_ptr = out_data.ctypes.data_as(ctypes.c_void_p)


param = Parameter(count, in_ptr, out_ptr)

a = foo(ctypes.byref(param))

pprint.pprint(out_data)


