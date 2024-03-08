#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 16:08:26 2024

@author: vishnureddy
"""

# Run "pip install pyqrcode" before running this program
import pyqrcode

data = input("Enter the text or link to generate QR code: ")

# Using pyqrcode.create() to create a qr code of the input data 
qr = pyqrcode.create(data)

# Using .svg method to save the qr code as SVG file of provided name & scale 
qr.svg('qr_code.svg', scale = 8)