import tkinter as tk
from guicreator.elements.ThresholdGui import ThresholdGui
from guicreator.elements.MethodsListBoxGui import MethodsListBoxGui

class Gui():
    def __init__(self, method_to_list, process_image_function):
        self.root = tk.Tk()
        self.process_image_function = process_image_function

        self.threshold = ThresholdGui(self.root, process_image_function)
        self.methods_listbox = MethodsListBoxGui(self.root, method_to_list)

        self.root.title("Image Processor")



    def start(self): 
        process_button = tk.Button(self.root, text='Process', command=self.process_image_function)
        process_button.pack()

        self.root.mainloop()