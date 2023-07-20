from imageprocessor.ImageProcessor import ImageProcessor
from guicreator.Gui import Gui
from imageprocessor.ThresholdMethodsPossibilites import ThresholdMethodsPossibilites
import cv2
import threading
import tkinter as tk
import queue
import time

class BlurChain:
    def process_image(image_processor: ImageProcessor, gui: Gui):
        if not gui.blur_check.get():
            return
        
        blur_amount = gui.blur_scale.get()

        image_processor.blur_image(blur_amount)
    
class ThresholdChain:
    def process_image(image_processor: ImageProcessor, gui: Gui):
        if not gui.threshold_check.get():
            print("falhou")
            return
        
        min = gui.threshold_min.get()
        max = gui.threshold_max.get()
        method = gui.threshold_method.get()

        use_auxiliary = gui.threshold_auxiliary_check
        auxiliary_method = gui.threshold_auxiliary_method.get()

        method_to_use = ThresholdMethodsPossibilites.threshold_methods[method]

        if use_auxiliary.get():
            if auxiliary_method == 'THRESH_OTSU':
                method_to_use = ThresholdMethodsPossibilites.threshold_otsu_join[method]

            elif auxiliary_method == 'THRESH_TRIANGLE':
                method_to_use = ThresholdMethodsPossibilites.threshold_triangle_join[method]

        image_processor.threshold_image(min, max, method_to_use)
      
class Main:
    methods_mapping = {
        "Blur": BlurChain,
        "Threshold": ThresholdChain
    }

    def __init__(self) -> None:
        self.thread_gui = None
        self.thread_image_show_loop = None
        self.queue = queue.Queue()
        self.gui = None
        self.image_processor = ImageProcessor(r'./captchas/1.png')

        cv2.namedWindow('Result')

    def process_image(self, x):
        self.image_processor.reset_image()
        
        methods_to_apply = self.gui.get_listbox()

        for method in methods_to_apply:
            Main.methods_mapping[method].process_image(self.image_processor, self.gui)
        
    def gui_loop(self):
        self.gui = Gui(list(Main.methods_mapping.keys()), self.process_image)

        self.gui.start()

    def start_gui_loop(self):
        self.thread_gui = threading.Thread(target=self.gui_loop)
        self.thread_gui.start()

    def image_show_loop(self):
        while True:
            time.sleep(0.1)

            cv2.imshow('Result', self.image_processor.cv_img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        cv2.destroyAllWindows()
            
    def start(self):
        self.start_gui_loop()
        self.image_show_loop()
      
if __name__ == "__main__":
  new_gui = Main()
    
  new_gui.start()