import tkinter as tk


class FindContoursCreator:
    def __init__(self, root, process_image_function) -> None:
        self.root = root
        self.process_image_function = process_image_function

    def create_contours_checkbox(self):
        contours_var: tk.IntVar = tk.IntVar(self.root)
        contours_check = tk.Checkbutton(self.root, text="Find Contours", variable=contours_var, command=self.process_image_function)
        contours_check.pack()

        return contours_var

    def create_retr_method_option(self):
        retr_methods = ['RETR_EXTERNAL', 'RETR_LIST', 'RETR_CCOMP', 'RETR_TREE']
        retr_method_var = tk.StringVar(self.root)
        retr_method_var.set(retr_methods[0])  # set the default option
        retr_option_menu = tk.OptionMenu(self.root, retr_method_var, *retr_methods)
        retr_option_menu.pack()

        return retr_method_var

    def create_approx_method_option(self):
        approx_methods = ['CHAIN_APPROX_SIMPLE', 'CHAIN_APPROX_NONE']
        approx_method_var = tk.StringVar(self.root)
        approx_method_var.set(approx_methods[0])  # set the default option
        approx_option_menu = tk.OptionMenu(self.root, approx_method_var, *approx_methods)
        approx_option_menu.pack()

        return approx_method_var
