# -*- coding: utf-8 -*-

__author__ = 'zhmi'

import cv

import constants
import math

def binarization(image):

    grey = cv.CreateImage((image.width ,image.height),8,1) #8depth, 1 channel so grayscale
    cv.CvtColor(image, grey, cv.CV_RGBA2GRAY) #Convert to gray so act as a filter
    cv.ShowImage('Greyed_pic', grey)

    threshold_picture = cv.CloneImage(grey)
    cv.Threshold(threshold_picture, threshold_picture, 100, 255, cv.CV_THRESH_BINARY)
    cv.ShowImage("Threshold_pic", threshold_picture)

    return threshold_picture

def background_remove(image, background):

    res = cv.CloneImage(image)
    cv.AbsDiff(image, background, res) # Like minus for each pixel im(i) - im2(i)
    cv.ShowImage("AbsDiff", res)
    return res

def edge_detection(image):

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

def extract_pixel(image):
    print "height:", image.height
    print "weight:", image.width
    x = 0
    y = 0
    for i in range(image.height):
        for j in range(image.width):
            if(image[i,j] == 255.0):
                x = x + i
                y = y + j

    print "x:",x
    print "y:",y

    return x, y

def direction_recognize(x1, y1, x2, y2):
    x_offsets = x2 - x1
    y_offsets = y2 - y1
    if(x_offsets < 0):
        print "left"
    else:
        print "right"

    if(y_offsets < 0):
        print "up"
    else:
        print "down"


# test part
picture_path = constants.picture_path
background = cv.LoadImage('%s/background.jpg'%(picture_path))
cv.ShowImage('raw_background', background)
cv.WaitKey(0)

threshold_background = binarization(background)
cv.WaitKey(0)

image_one = cv.LoadImage('%s/1.jpg'%(picture_path))
cv.ShowImage('image_one', image_one)
cv.WaitKey(0)

threshold_image_one = binarization(image_one)
cv.WaitKey(0)

background_removed_pic_one = background_remove(threshold_image_one, threshold_background)
cv.WaitKey(0)

background_removed_pic_one = edge_detection(background_removed_pic_one)

x1, y1 = extract_pixel(background_removed_pic_one)
# picture 2
'''
image_two = cv.LoadImage('%s/2.jpg'%(picture_path))
cv.ShowImage('image_two', image_two)
cv.WaitKey(0)

threshold_image_two = binarization(image_two)
cv.WaitKey(0)

background_removed_pic_two = background_remove(threshold_image_two, threshold_background)
cv.WaitKey(0)

background_removed_pic_two = edge_detection(background_removed_pic_two)

x2, y2 = extract_pixel(background_removed_pic_two)

direction_recognize(x1, y1, x2, y2)
'''