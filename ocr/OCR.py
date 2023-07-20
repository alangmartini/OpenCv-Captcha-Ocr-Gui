import pytesseract

class ImageRecognition:
    def recognize_captcha(self, image):
      # Apply OCR to the preprocessed image
      text = pytesseract.image_to_string(image)

      return text