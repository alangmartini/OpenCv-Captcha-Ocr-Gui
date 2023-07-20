from guicreator.creators.ResizeCreator import ResizeCreator
import tkinter as tk


class ResizeCheck:
    def __init__(self, creator: ResizeCreator):
        self.check: tk.IntVar = creator.create_resize_checkbox()

    def get(self):
        return self.check.get()


class WidthValue:
    def __init__(self, creator: ResizeCreator):
        self.width_value: tk.Scale = creator.create_width_scale()

    def get(self):
        return self.width_value.get()
    

class HeightValue:
    def __init__(self, creator: ResizeCreator):
        self.height_value: tk.Scale = creator.create_height_scale()

    def get(self):
        return self.height_value.get()
    

class ResizeGui:
    def __init__(self, root, process_image_function):
        creator = ResizeCreator(root, process_image_function)

        self.check = ResizeCheck(creator)
        self.width_value = WidthValue(creator)
        self.height_value = HeightValue(creator)
