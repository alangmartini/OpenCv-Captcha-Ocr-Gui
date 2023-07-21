import tkinter as tk
from guicreator.elements.ThresholdGui import ThresholdGui
from guicreator.elements.MethodsListBoxGui import MethodsListBoxGui
from guicreator.elements.ResizeGui import ResizeGui
from guicreator.elements.GaussianBlurGui import GaussianBlurGui
from guicreator.elements.FindContoursGui import FindContoursGui
from guicreator.elements.CvtColorGui import CvtColorGui


class Gui():
    def __init__(self, method_to_list, process_image_function=None, ocr_function=None):
        if not process_image_function:
            def pass_fn(x):
                pass

            process_image_function = pass_fn
        
        # Function to process the images
        self.process_image_function = process_image_function

        # Function to ocr the images
        self.ocr_function = ocr_function

        # Main Window
        self.root = tk.Tk()
        
        # Title
        self.root.title("Image Processor")

        # List all possible methods
        self.methods_listbox = MethodsListBoxGui(self.root, method_to_list)

        # Methods parameters
        
        self.threshold = ThresholdGui(self.root, process_image_function)
        self.resize = ResizeGui(self.root, process_image_function)
        self.gaussian_blur = GaussianBlurGui(self.root, process_image_function)
        self.find_contours = FindContoursGui(self.root, process_image_function)
        self.cvt_color = CvtColorGui(self.root, process_image_function)

    def start(self): 
        process_button = tk.Button(self.root, text='Process', command=self.ocr_function)
        process_button.pack()

        self.root.mainloop()