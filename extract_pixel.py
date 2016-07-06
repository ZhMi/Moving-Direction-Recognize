# !/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'zhmi'

def ExtrPixel(image):

    print "height:", image.height
    print "weight:", image.width
    x = 0
    y = 0
    for i in range(image.height):
        for j in range(image.width):
            if(image[i,j] == 0):
                x = x + i
                y = y + j

    print "x:",x
    print "y:",y

    return x, y