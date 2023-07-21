import tkinter as tk
from guicreator.creators.FindContoursCreator import FindContoursCreator


class FindContoursGui:
    def __init__(self, root, process_image_function):
        creator = FindContoursCreator(root, process_image_function)
        self.check = FindContoursCheck(creator)
        self.retr_method = FindContoursRetrMethod(creator)
        self.approx_method = FindContoursApproxMethod(creator)


class FindContoursCheck:
    def __init__(self, creator: FindContoursCreator):
        self.check: tk.IntVar = creator.create_contours_checkbox()

    def get(self):
        return self.check.get()


class FindContoursRetrMethod:
    def __init__(self, creator: FindContoursCreator):
        self.method: tk.StringVar = creator.create_retr_method_option()

    def get(self):
        return self.method.get()


class FindContoursApproxMethod:
    def __init__(self, creator: FindContoursCreator):
        self.method: tk.StringVar = creator.create_approx_method_option()

    def get(self):
        return self.method.get()
