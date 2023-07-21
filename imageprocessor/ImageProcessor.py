import cv2
from PIL import Image
import os


class ImageProcessor:
    color_conversion_codes = [cv2.COLOR_BGR2GRAY, cv2.COLOR_BGR2HSV, cv2.COLOR_BGR2HLS, cv2.COLOR_BGR2RGB, cv2.COLOR_BGR2YUV, cv2.COLOR_RGB2GRAY, cv2.COLOR_RGB2HSV, cv2.COLOR_RGB2HLS, cv2.COLOR_RGB2BGR, cv2.COLOR_RGB2YUV]

    def __init__(self, image_path) -> None:
        self.image_path = image_path
        self.cv_img = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2GRAY)
        self.raw_img = self.cv_img
        
    def cvt_color(self, method):
        self.cv_img = cv2.cvtColor(self.cv_img, method)

    def threshold_image(self, mini, maxi, method):
        self.cv_img = cv2.threshold(self.cv_img, mini, maxi, method)[1]

    def resize_image(self, width, height):
        self.cv_img = cv2.resize(self.cv_img, (width, height))

    def gaussian_blur(self, size, sigma):
        self.cv_img = cv2.GaussianBlur(self.cv_img, (size, size), sigma)

    def find_contours(self, retr_method, approx_method):
        contours, _ = cv2.findContours(self.cv_img, retr_method, approx_method)
        self.cv_img = cv2.cvtColor(self.cv_img, cv2.COLOR_GRAY2RGB)
        self.cv_img = cv2.drawContours(self.cv_img, contours, -1, (255, 0, 0), 3)

    def preprocess_image(self, image_path):
        # Load the image from file
        image = cv2.imread(image_path)

        # Convert the image to grayscale
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Apply a blur to the image (this can help remove noise)
        image = cv2.GaussianBlur(image, (5, 5), 0)

        # Apply thresholding (this can help make the text more clear)
        _, image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        # Get the output directory and filename
        output_dir = os.path.dirname(image_path)
        output_filename = "processed.png"

        # Save the processed image
        output_path = os.path.join(output_dir, output_filename)
        cv2.imwrite(output_path, image)

        return Image.open(output_path)
    
    def reset_image(self):
        self.cv_img = self.raw_img

    def blur_image(self, image, blur_amount):
        self.cv_img = cv2.GaussianBlur(image, (blur_amount, blur_amount), 0)
    
