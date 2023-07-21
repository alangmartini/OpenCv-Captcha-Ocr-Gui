import tkinter as tk


class ListBoxUpAndDown:
    @staticmethod
    def move_up(listbox):
        # get the index of the current selection
        selected_index = listbox.curselection()[0]
        if selected_index > 0:
            # get the value of the selected item
            selected_value = listbox.get(selected_index)
            # delete the selected item from the listbox
            listbox.delete(selected_index)
            # insert the item back into the listbox at the new position
            listbox.insert(selected_index - 1, selected_value)
            # select the moved item
            listbox.selection_set(selected_index - 1)

    @staticmethod
    def move_down(listbox):
        # get the index of the current selection
        selected_index = listbox.curselection()[0]
        if selected_index < listbox.size() - 1:
            # get the value of the selected item
            selected_value = listbox.get(selected_index)
            # delete the selected item from the listbox
            listbox.delete(selected_index)
            # insert the item back into the listbox at the new position
            listbox.insert(selected_index + 1, selected_value)
            # select the moved item
            listbox.selection_set(selected_index + 1)


class MethodsListBoxCreator:
    def __init__(self, root, method_to_list):
        self.root = root
        self.method_to_list = method_to_list

    def create_listbox(self):
        listbox = tk.Listbox(self.root)
        listbox.pack()

        for item in self.method_to_list:
            # listbox.insert(tk.END, item.name)
            listbox.insert(tk.END, item)

        up_button = tk.Button(self.root, text="Move up", command=lambda: ListBoxUpAndDown.move_up(listbox))
        up_button.pack()

        down_button = tk.Button(self.root, text="Move down", command=lambda: ListBoxUpAndDown.move_down(listbox))
        down_button.pack()

        return listbox

