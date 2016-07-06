# !/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'zhmi'

import cv

def BackgRemove(image, background):

    res = cv.CloneImage(image)
    cv.AbsDiff(image, background, res)# Like minus for each pixel im(i) - im2(i)
    cv.ShowImage("AbsDiff", res)
    return res


