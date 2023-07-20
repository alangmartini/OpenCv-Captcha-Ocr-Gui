import pytesseract


class ImageRecognition:
    def __init__(self) -> None:
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    def recognize_captcha(self, image):
        # Apply OCR to the preprocessed image
        # text = pytesseract.image_to_string(image)

        for psm in range(0, 14):
            for oem in range(0, 4):
                try:
                    config = f'--oem {oem} --psm {psm}'
                    result = pytesseract.image_to_string(image, config=config)
                    print(f"config (oem {oem}, psm {psm}) result is:", result)
                except Exception as e:
                    continue
