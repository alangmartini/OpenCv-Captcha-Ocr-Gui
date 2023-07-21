from guicreator.creators.GaussianBlurCreator import GaussianBlurCreator
import tkinter as tk


class GaussianBlurCheck:
    def __init__(self, creator: GaussianBlurCreator):
        self.check: tk.IntVar = creator.create_method_checkbox()

    def get(self):
        return self.check.get()


class GaussianBlurSize:
    def __init__(self, creator: GaussianBlurCreator):
        self.check: tk.Scale = creator.create_size_scale()

    def get(self):
        return self.check.get()


class GaussianBlurSigma:
    def __init__(self, creator: GaussianBlurCreator):
        self.check: tk.Scale = creator.create_sigma_scale()

    def get(self):
        return self.check.get()


class GaussianBlurGui:
    def __init__(self, root, process_image_function):
        creator = GaussianBlurCreator(root, process_image_function)

        self.check = GaussianBlurCheck(creator)
        self.size = GaussianBlurSize(creator)
        self.sigma = GaussianBlurSigma(creator)
