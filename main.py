# !/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'zhmi'

import cv
import constants
import binarization
import background_remove
import edge_detection
import extract_pixel
import direction_recognize

if __name__ == "__main__":

    picture_path = constants.picture_path
    background = cv.LoadImage('%s/background.jpg'%(picture_path))
    cv.ShowImage('raw_background', background)
    cv.WaitKey(0)

    threshold_background = binarization.BinImage(background)
    cv.WaitKey(0)

    # picture one
    image_one = cv.LoadImage('%s/2.jpg'%(picture_path))
    cv.ShowImage('image_one', image_one)
    cv.WaitKey(0)

    threshold_image_one = binarization.BinImage(image_one)
    cv.WaitKey(0)

    background_removed_pic_one = background_remove.BackgRemove(threshold_image_one, threshold_background)
    cv.WaitKey(0)

    background_removed_pic_one = edge_detection.EdgeDetect(background_removed_pic_one)

    x1, y1 = extract_pixel.ExtrPixel(background_removed_pic_one)

    # picture 2

    image_two = cv.LoadImage('%s/1.jpg'%(picture_path))
    cv.ShowImage('image_two', image_two)
    cv.WaitKey(0)

    threshold_image_two = binarization.BinImage(image_two)
    cv.WaitKey(0)

    background_removed_pic_two = background_remove.BackgRemove(threshold_image_two, threshold_background)
    cv.WaitKey(0)

    background_removed_pic_two = edge_detection.EdgeDetect(background_removed_pic_two)

    x2, y2 = extract_pixel.ExtrPixel(background_removed_pic_two)

    direction_recognize.DirRecognize(x1, y1, x2, y2)
