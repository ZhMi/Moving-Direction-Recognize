# !/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'zhmi'

def DirRecognize(x1, y1, x2, y2):
    x_offsets = x2 - x1
    y_offsets = y2 - y1
    if(x_offsets < 0):
        print "left"
    else:
        if(x_offsets == 0):
            print "Not moving in horizontal direction"
        else:
            print "right"

    if(y_offsets < 0):
        print "up"
    else:
        if(x_offsets == 0):
            print "Not moving in vertical direction"
        else:
            print "down"

    return 0

