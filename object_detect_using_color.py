#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 15:05:21 2020

@author: rjn
"""
## Rotate images (correctly) with OpenCV in Python

# import the necessary packages
# NumPy for numerical processing
import numpy as np
# cv2  for our OpenCV bindings
import cv2

cap = cv2.VideoCapture(0) 
def nothing(x):
    pass

cv2.namedWindow('image')
# create trackbars for color change
cv2.createTrackbar('low_H','image',0, 179,nothing)
cv2.createTrackbar('high_H','image',179, 179,nothing)
cv2.createTrackbar('low_s','image',0,255,nothing)
cv2.createTrackbar('low_v','image',0,255,nothing)

try:
    while(True):
        _, frame = cap.read()    
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # get current positions of four trackbars
        low_h = cv2.getTrackbarPos('low_H','image')
        high_h = cv2.getTrackbarPos('high_H','image')
        low_s = cv2.getTrackbarPos('low_s','image')
        low_v = cv2.getTrackbarPos('low_v','image')

        lower = (low_h,low_s,low_v)
        upper = (high_h,255,255)
        # find the colors within the specified boundaries and apply
        #the mask
        mask = cv2.inRange(hsv, lower, upper)
        output = cv2.bitwise_and(frame, frame, mask = mask)
          
        cv2.imshow('mask',mask)
        cv2.imshow('output',output)
       
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
finally:
    cap.release()
    cv2.destroyAllWindows()