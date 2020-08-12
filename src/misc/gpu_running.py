#!-*- coding: utf8 -*-
from numba import jit

import datetime
import numpy


def func(a):
    for i in range(len(a)):
        a[i] += 1


@jit
def func2(a):
    for i in range(len(a)):
        a[i] += 1


if __name__ == "__main__":
    n_ = numpy.ones(1000000000, dtype=numpy.float64)

    start = datetime.datetime.now()
    func(n_)
    print("without GPU:", datetime.datetime.now() - start)

    start = datetime.datetime.now()
    func2(n_)
    print("with GPU:", datetime.datetime.now() - start)
