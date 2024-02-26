import numpy as np
import cv2

def enhance_contrast_rgb(image: np.ndarray) -> np.ndarray:
    """Enhances the contrast of an RGB image by applying CLAHE to each channel separately."""
    clahe = cv2.createCLAHE(clipLimit=8.0, tileGridSize=(8, 8))
    r_channel, g_channel, b_channel = cv2.split(image)
    clahe_r = clahe.apply(r_channel)
    clahe_g = clahe.apply(g_channel)
    clahe_b = clahe.apply(b_channel)
    enhanced_image = cv2.merge([clahe_r, clahe_g, clahe_b])
    return enhanced_image

def unblur(img, ne: int=9):
    """sharpens image"""
    kernel_sharp = np.array([[-1,-1,-1], [-1,ne,-1], [-1,-1,-1]])
    return cv2.filter2D(img, -1, kernel_sharp)

def apply_noise_reduction(image):
    blurred_image = cv2.GaussianBlur(image, (3, 3), cv2.BORDER_DEFAULT)
    return blurred_image

def enhance_contrast(image, clipLimit: int=8.0):
    clahe = cv2.createCLAHE(clipLimit, tileGridSize=(8, 8))
    enhanced_image = clahe.apply(image)
    return enhanced_image

