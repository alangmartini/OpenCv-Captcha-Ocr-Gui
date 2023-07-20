import tkinter as tk
from imageprocessor.ThresholdMethodsPossibilites import ThresholdMethodsPossibilites
from interfaces.ThresholdGuiElements import ThresholdGuiElements


class ElementsCreator:
    def create_blur_check(self, root):
      is_blur_checked = tk.IntVar(root)
      blur_check = tk.Checkbutton(root, text='Blur', variable=is_blur_checked)
      blur_check.pack()

      blur_scale = tk.Scale(root, from_=1, to=10, orient=tk.HORIZONTAL)
      blur_scale.pack()

      blur_scale = blur_scale
      blur_check = blur_check

      return [is_blur_checked, blur_scale]
    
    def create_color_check(self, root):
      is_color_checked = tk.IntVar(root)
      color_check = tk.Checkbutton(root, text='Convert color', variable=is_color_checked)
      color_check.pack()

      return is_color_checked
        
    