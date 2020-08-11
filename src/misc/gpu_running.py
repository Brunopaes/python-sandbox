#!-*- coding: utf8 -*-
from numba import jit, vectorize, cuda

import datetime
import numpy


def func(a):
    for i in range(10000000):
        a[i] += 1


@jit(target="cuda")
def func2(a):
    for i in range(10000000):
        a[i] += 1


if __name__ == "__main__":
    n = 10000000
    a = numpy.ones(n, dtype=numpy.float64)
    b = numpy.ones(n, dtype=numpy.float32)

    start = datetime.datetime.now()
    func(a)
    print("without GPU:", datetime.datetime.now() - start)

    start = datetime.datetime.now()
    func2(a)
    print("with GPU:", datetime.datetime.now() - start)
