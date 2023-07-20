import tkinter as tk


class ResizeCreator:
    def __init__(self, root, process_image_function) -> None:
        self.root = root
        self.process_image_function = process_image_function

    def create_resize_checkbox(self):
        is_resize_checked = tk.IntVar(self.root)
        resize_check = tk.Checkbutton(self.root, text='Resize', variable=is_resize_checked)
        resize_check.pack()

        return is_resize_checked

    def create_width_scale(self):
        width_value = tk.Scale(self.root, label="Width", from_=1, to=1000, orient=tk.HORIZONTAL, command=self.process_image_function)
        width_value.pack()

        return width_value

    def create_height_scale(self):
        height_value = tk.Scale(self.root, label="Height", from_=1, to=1000, orient=tk.HORIZONTAL, command=self.process_image_function)
        height_value.pack()

        return height_value