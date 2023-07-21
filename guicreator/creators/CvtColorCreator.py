import tkinter as tk
from imageprocessor.CvtColorPossibilities import CvtColorMethodsPossibilities


class CvtColorCreator:
    def __init__(self, root, process_image_function) -> None:
        self.root = root
        self.process_image_function = process_image_function

    def create_cvt_color_checkbox(self):
        cvt_color_var: tk.IntVar = tk.IntVar(self.root)
        cvt_color_check = tk.Checkbutton(self.root, text="Cvt Color", variable=cvt_color_var, command=self.process_image_function)
        cvt_color_check.pack()

        return cvt_color_var

    def create_method_option(self):
        all_methods = list(CvtColorMethodsPossibilities.cvt_color_methods.keys())
        cvt_color_method_var = tk.StringVar(self.root)
        cvt_color_method_var.set(all_methods[0])  # set the default option

        cvt_color_option_menu = tk.OptionMenu(self.root, cvt_color_method_var, *all_methods)
        cvt_color_option_menu.pack()

        return cvt_color_method_var
