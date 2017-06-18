#!/usr/bin/env python3

import bmp
import fractal

FILE_NAME = 'mandel.bmp'

pixels = fractal.mandelbrot(448, 256)
bmp.write_greyscale(FILE_NAME, pixels)
dims = bmp.dimensions(FILE_NAME)
print(dims)
