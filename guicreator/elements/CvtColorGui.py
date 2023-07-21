import tkinter as tk
from guicreator.creators.CvtColorCreator import CvtColorCreator


class CvtColorGui:
    def __init__(self, root, process_image_function):
        creator = CvtColorCreator(root, process_image_function)
        self.check = CvtColorCheck(creator)
        self.method = CvtColorMethod(creator)


class CvtColorCheck:
    def __init__(self, creator: CvtColorCreator):
        self.check: tk.IntVar = creator.create_cvt_color_checkbox()

    def get(self):
        return self.check.get()


class CvtColorMethod:
    def __init__(self, creator: CvtColorCreator):
        self.method: tk.StringVar = creator.create_method_option()

    def get(self):
        return self.method.get()