import tkinter as tk
from guicreator.creators.ThresholdCreator import ThresholdCreator


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


class ThresholdGui:
    def __init__(self, root, process_image_function):
        creator = ThresholdCreator(root, process_image_function)

        self.check = ThresholdCheck(creator)
        self.auxiliary_check = ThresholdAuxiliaryCheck(creator)
        self.min = ThresholdMin(creator)
        self.max = ThresholdMax(creator)
        self.method = ThresholdMethod(creator)
        self.auxiliary_method = ThresholdAuxiliaryMethod(creator)
