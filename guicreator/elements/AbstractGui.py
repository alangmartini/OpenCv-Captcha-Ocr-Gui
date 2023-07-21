import tkinter as tk
import abc


class AbstractGui(abc.ABC):
    def __init__(self, root, process_image_function, title, position):
        self.window = tk.Toplevel(root)
        self.window.title(title)
        self.window.geometry(position)
        self.creator = self.get_creator(self.window, process_image_function)

    @abc.abstractmethod
    def get_creator(self, window, process_image_function):
        pass