from imageprocessor.ThresholdMethodsPossibilites import ThresholdMethodsPossibilites
import tkinter as tk

class ThresholdCreator:
    def __init__(self, root, process_image_function) -> None:
        self.root = root
        self.process_image_function = process_image_function
       
    def create_min_scale(self):
        threshold_min = tk.Scale(self.root, label="min",from_=1, to=255, orient=tk.HORIZONTAL, command=self.process_image_function)
        threshold_min.pack()

        return threshold_min

    def create_max_scale(self):
        threshold_max = tk.Scale(self.root, label="max", from_=1, to=255, orient=tk.HORIZONTAL, command=self.process_image_function)
        threshold_max.set(255)
        threshold_max.pack()

        return threshold_max

    def create_method_option_menu(self):
        all_methods = list(ThresholdMethodsPossibilites.threshold_methods.keys())
        selected_threshold_method = tk.StringVar(self.root)
        selected_threshold_method.set(all_methods[0])

        # selected_threshold_method.trace('w', fn)

        threshold_methods_dropdown = tk.OptionMenu(self.root, selected_threshold_method, *all_methods, command=self.process_image_function)
        threshold_methods_dropdown.pack()

        return selected_threshold_method
    
    def create_auxiliary_method_option_menu(self):
        all_methods = list(ThresholdMethodsPossibilites.threshold_auxiliary_methods.keys())
        selected_threshold_method = tk.StringVar(self.root)

        selected_threshold_method.set(all_methods[0])

        threshold_methods_dropdown = tk.OptionMenu(self.root, selected_threshold_method, *all_methods)
        threshold_methods_dropdown.pack()

        return selected_threshold_method
    
    def create_method_checkbox(self):
        is_method_checked = tk.IntVar(self.root)
        method_check = tk.Checkbutton(self.root, text='Use auxiliary method', variable=is_method_checked)
        method_check.pack()

        return is_method_checked
    
    def create_auxiliary_method_checkbox(self):
        is_threshold_auxiliary_checked = tk.IntVar(self.root)
        threshold_auxiliary_check = tk.Checkbutton(self.root, text='Auxiliary Threshold', variable=is_threshold_auxiliary_checked) 
        threshold_auxiliary_check.pack()

        return is_threshold_auxiliary_checked
