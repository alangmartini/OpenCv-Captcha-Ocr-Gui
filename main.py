import time
import threading
import cv2
from imageprocessor.ImageProcessor import ImageProcessor
from guicreator.Gui import Gui
from chains import BlurChain, ThresholdChain
from ocr.Ocr import ImageRecognition

class Main:
    methods_mapping = {
        # "Blur": BlurChain.BlurChain,
        "Threshold": ThresholdChain.ThresholdChain
    }

    def __init__(self) -> None:
        self.thread_gui = None
        self.thread_image_show_loop = None
        self.gui = None
        self.ocr: ImageRecognition = ImageRecognition()
        self.image_processor = ImageProcessor(r'./captchas/1.png')

        cv2.namedWindow('Result')

    def process_image(self, teste=None):
        self.image_processor.reset_image()
        
        methods_to_apply = self.gui.methods_listbox.listbox.get()

        for method in methods_to_apply:
            Main.methods_mapping[method].process_image(self.image_processor, self.gui)

    
    def ocr_image(self):
        self.ocr.recognize_captcha(self.image_processor.cv_img)

    def start_gui_loop(self):
        # self.gui = Gui(list(Main.methods_mapping.keys()), self.process_image)
        self.gui = Gui(
            list(Main.methods_mapping.keys()),
            process_image_function=self.process_image,
            ocr_function=self.ocr_image
        )

        self.gui.start()

    def start_thread_gui_loop(self):
        self.thread_gui = threading.Thread(target=self.start_gui_loop)
        self.thread_gui.start()

    def image_show_loop(self):
        while True:
            time.sleep(0.1)

            cv2.imshow('Result', self.image_processor.cv_img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        cv2.destroyAllWindows()
            
    def start(self):
        self.start_thread_gui_loop()
        self.image_show_loop()
      
if __name__ == "__main__":
  new_gui = Main()
    
  new_gui.start()