# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 20:31:56 2025
Segmentasi Kontur dengan Gaussian Blur
@author: Lenovo
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def segmentasi_kontur(image_path):
    # Baca gambar
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Lakukan Gaussian Blur untuk mengurangi noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Lakukan thresholding dengan Otsu's Binarization
    _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    # Morfologi operasi untuk memperbaiki kontur
    kernel = np.ones((3, 3), np.uint8)
    morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)
    
    # Temukan kontur
    contours, hierarchy = cv2.findContours(morph, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Gambar kontur pada gambar asli
    image_contour = image.copy()
    cv2.drawContours(image_contour, contours, -1, (0, 255, 0), 2)
    
    # Tampilkan hasil
    plt.figure(figsize=(15, 5))
    
    plt.subplot(1, 3, 1)
    plt.imshow(gray, cmap='gray')
    plt.title('Grayscale Image')
    
    plt.subplot(1, 3, 2)
    plt.imshow(thresh, cmap='gray')
    plt.title("Threshold Image (Otsu's Binarization)")
    
    plt.subplot(1, 3, 3)
    plt.imshow(cv2.cvtColor(image_contour, cv2.COLOR_BGR2RGB))
    plt.title('Contour Detection')
    
    plt.show()

# Contoh penggunaan
segmentasi_kontur('gambar.jpg')