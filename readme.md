Simple example of calling c functions from python script.

[ctypes tutorial](https://docs.python.org/3/library/ctypes.html) contains
details and examples.

Briefly,

* For c code side, there is no different from creating a dynamic library to be
  used for any c applications.

* Python side, need to declare wrappers for the c function arguments and return
  types, namely `argtypes` and `restype` respectively. 

* Python data type wrapper for standard c data types are listed
  [here](https://docs.python.org/3/library/ctypes.html#fundamental-data-types)

* Typical numpy array has the same format as c array and it has ctypes attribute
  to get the pointer to be used in c function. Documents is
  [here](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.ctypes.html)
