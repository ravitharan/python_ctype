import numpy as np
from ctypes import *
import matplotlib.pyplot as plt
from matplotlib.backend_bases import MouseButton

def onclick(event):
    if event.button is MouseButton.RIGHT:
        print(f'{round(event.xdata)} {round(event.ydata)}')

angle = np.arange(0, 4 * np.pi, np.pi / 256)
sin = np.zeros(len(angle))
cos = np.zeros(len(angle))

lib = cdll.LoadLibrary('./c/libfoo.so')
foo = lib.foo

foo.argtypes    = [POINTER(c_double), c_int, POINTER(c_double), POINTER(c_double)]
foo.restype     = c_int

ret = foo(angle.ctypes.data_as(POINTER(c_double)), len(angle),
          sin.ctypes.data_as(POINTER(c_double)),
          cos.ctypes.data_as(POINTER(c_double)))

fig, axe = plt.subplots()
fig.canvas.mpl_connect('button_press_event', onclick)

axe.plot(angle, sin, label='sin', marker='')
axe.plot(angle, cos, label='cos', marker='')

axe.legend(loc='upper right')
axe.set_title('plot')
axe.grid(True)
plt.show()
