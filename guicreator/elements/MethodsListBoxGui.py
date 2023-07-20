from guicreator.creators.MethodsListBoxCreator import MethodsListBoxCreator
import tkinter as tk


class Listbox:
    def __init__(self, methods_listbox_creator: MethodsListBoxCreator):
        self.listbox = methods_listbox_creator.create_listbox()

    def get(self):
        return self.listbox.get(0, tk.END)
    

class MethodsListBoxGui:
    def __init__(self, root, method_to_list):
        methods_listbox_creator = MethodsListBoxCreator(root, method_to_list)

        self.listbox: Listbox = Listbox(methods_listbox_creator)
