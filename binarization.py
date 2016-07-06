# !/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'zhmi'

import cv

def BinImage(image):

    grey = cv.CreateImage((image.width, image.height),8,1) #8 depth, 1 channel so grayscale
    cv.CvtColor(image, grey, cv.CV_RGBA2GRAY) #Convert to gray so act as a filter
    cv.ShowImage('Greyed_pic', grey)

    threshold_picture = cv.CloneImage(grey)
    cv.Threshold(threshold_picture, threshold_picture, 100, 255, cv.CV_THRESH_BINARY)
    cv.ShowImage("Threshold_pic", threshold_picture)
    return threshold_picture

