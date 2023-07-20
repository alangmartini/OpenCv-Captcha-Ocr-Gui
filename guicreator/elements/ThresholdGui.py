import tkinter as tk
from guicreator.creators.ThresholdCreator import ThresholdCreator


class ThresholdCheck:
    def __init__(self, threshold_creator: ThresholdCreator):
        self.threshold_check: tk.IntVar = threshold_creator.create_method_checkbox()

    def get(self):
        return self.threshold_check.get()


class ThresholdAuxiliaryCheck:
    def __init__(self, threshold_creator: ThresholdCreator):
        self.threshold_auxiliary_check: tk.IntVar = threshold_creator.create_auxiliary_method_checkbox()

    def get(self):
        return self.threshold_auxiliary_check.get()


class ThresholdMin:
    def __init__(self, threshold_creator: ThresholdCreator):
        self.threshold_min: tk.Scale = threshold_creator.create_min_scale()

    def get(self):
        return self.threshold_min.get()


class ThresholdMax:
    def __init__(self, threshold_creator: ThresholdCreator):
        self.threshold_max: tk.Scale = threshold_creator.create_max_scale()

    def get(self):
        return self.threshold_max.get()


class ThresholdMethod:
    def __init__(self, threshold_creator: ThresholdCreator):
        self.threshold_method: tk.StringVar = threshold_creator.create_method_option_menu()

    def get(self):
        return self.threshold_method.get()


class ThresholdAuxiliaryMethod:
    def __init__(self, threshold_creator: ThresholdCreator):
        self.threshold_auxiliary_method: tk.StringVar = threshold_creator.create_auxiliary_method_option_menu()

    def get(self):
        return self.threshold_auxiliary_method.get()


class ThresholdGui:
    def __init__(self, root, process_image_function):
        threshold_creator = ThresholdCreator(root, process_image_function)

        self.threshold_check = ThresholdCheck(threshold_creator)
        self.threshold_auxiliary_check = ThresholdAuxiliaryCheck(threshold_creator)
        self.threshold_min = ThresholdMin(threshold_creator)
        self.threshold_max = ThresholdMax(threshold_creator)
        self.threshold_method = ThresholdMethod(threshold_creator)
        self.threshold_auxiliary_method = ThresholdAuxiliaryMethod(threshold_creator)
