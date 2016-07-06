# !/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'zhmi'

import cv

def EdgeDetect(image):

    sobx = cv.CreateImage(cv.GetSize(image), cv.IPL_DEPTH_16S, 1)
    cv.Sobel(image, sobx, 1, 0, 3) #Sobel with x-order=1

    soby = cv.CreateImage(cv.GetSize(image), cv.IPL_DEPTH_16S, 1)
    cv.Sobel(image, soby, 0, 1, 3) #Sobel withy-oder=1

    cv.Abs(sobx, sobx)
    cv.Abs(soby, soby)

    result = cv.CloneImage(image)
    cv.Add(sobx, soby, result) #Add the two results together.

    cv.Threshold(result, result, 100, 255, cv.CV_THRESH_BINARY_INV)

    cv.ShowImage('raw Image', image)
    cv.ShowImage('edge detection Result', result)

    cv.WaitKey(0)
    return result