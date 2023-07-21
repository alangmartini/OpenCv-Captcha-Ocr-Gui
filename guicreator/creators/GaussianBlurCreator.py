import tkinter as tk


class GaussianBlurCreator:
    def __init__(self, root, process_image_function) -> None:
        self.root = root
        self.process_image_function = process_image_function

    def create_method_checkbox(self):
        check = tk.IntVar()
        c = tk.Checkbutton(self.root, text="GaussianBlur", variable=check, command=self.process_image_function)
        c.pack(side=tk.RIGHT)

        return check

    def create_size_scale(self):
        size = tk.Scale(self.root, label="size", from_=1, to=100, orient=tk.HORIZONTAL, command=self.process_image_function)
        size.pack(side=tk.RIGHT)
        return size

    def create_sigma_scale(self):
        sigma = tk.Scale(self.root, label="sigma", from_=0.1, to=10, resolution=0.1, orient=tk.HORIZONTAL, command=self.process_image_function)
        sigma.pack()
        return sigma
