# -*- coding: utf-8 -*-
import math


def bounding_box(b, h, error=0.05):
    h = h - (error * 2)
    area = b * h
    internal_box = math.pow((14/28.346), 2)

    return area/internal_box


if __name__ == '__main__':
    print(bounding_box(10, 5))
