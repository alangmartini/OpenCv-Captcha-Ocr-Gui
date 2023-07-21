import tkinter as tk
from guicreator.creators.ThresholdCreator import ThresholdCreator
from guicreator.elements.AbstractGui import AbstractGui


class ThresholdGui(AbstractGui):
    def __init__(self, root, process_image_function):
        # Creates self.creator with the class in self.get_creator()
        super().__init__(root, process_image_function, "Threshold", "+100+100")
        # self.window = tk.Toplevel(root)
        # self.window.title("Threshold")
        
        # Gui Elements
        self.check = ThresholdCheck(self.creator)
        self.auxiliary_check = ThresholdAuxiliaryCheck(self.creator)
        self.min = ThresholdMin(self.creator)
        self.max = ThresholdMax(self.creator)
        self.method = ThresholdMethod(self.creator)
        self.auxiliary_method = ThresholdAuxiliaryMethod(self.creator)

    def get_creator(self, window, process_image_function):
        return ThresholdCreator(window, process_image_function)


class ThresholdCheck:
    def __init__(self, creator: ThresholdCreator):
        self.check: tk.IntVar = creator.create_method_checkbox()

    def get(self):
        return self.check.get()


class ThresholdAuxiliaryCheck:
    def __init__(self, creator: ThresholdCreator):
        self.auxiliary_check: tk.IntVar = creator.create_auxiliary_method_checkbox()

    def get(self):
        return self.auxiliary_check.get()


class ThresholdMin:
    def __init__(self, creator: ThresholdCreator):
        self.min: tk.Scale = creator.create_min_scale()

    def get(self):
        return self.min.get()


class ThresholdMax:
    def __init__(self, creator: ThresholdCreator):
        self.max: tk.Scale = creator.create_max_scale()

    def get(self):
        return self.max.get()


class ThresholdMethod:
    def __init__(self, creator: ThresholdCreator):
        self.method: tk.StringVar = creator.create_method_option_menu()

    def get(self):
        return self.method.get()


class ThresholdAuxiliaryMethod:
    def __init__(self, creator: ThresholdCreator):
        self.auxiliary_method: tk.StringVar = creator.create_auxiliary_method_option_menu()

    def get(self):
        return self.auxiliary_method.get()