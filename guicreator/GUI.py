import tkinter as tk
from guicreator.gui_elements_creator import ElementsCreator
from interfaces.ThresholdGuiElements import ThresholdGuiElements

class Threshold:
  def __init__(self, root):
    # Get threshold handlers
    threshold_vars: ThresholdGuiElements = elements_creator.create_threshold(self.root, process_image_function)
    
    self.threshold_check: tk.IntVar = threshold_vars["threshold_check"]
    self.threshold_auxiliary_check: tk.IntVar = threshold_vars["threshold_auxiliary_check"]
    self.threshold_min = threshold_vars["threshold_min"]
    self.threshold_max = threshold_vars["threshold_max"]
    self.threshold_method = threshold_vars["threshold_method"]
    self.threshold_auxiliary_method = threshold_vars["threshold_auxiliary_method"]

class Gui():
  def __init__(self, method_to_list, process_image_function):
    self.root = tk.Tk()
    self.process_image_function = process_image_function
    elements_creator = ElementsCreator()
    self.root.title("Image Processor")

    self.listbox = elements_creator.create_listbox(self.root, method_to_list)

    self.blur_check, self.blur_scale = elements_creator.create_blur_check(self.root)

    self.color_check = elements_creator.create_color_check(self.root)


  

  def get_listbox(self):
     return self.listbox.get(0, tk.END)
  
  
  def start(self): 
    process_button = tk.Button(self.root, text='Process', command=self.process_image_function)
    process_button.pack()

    self.root.mainloop()