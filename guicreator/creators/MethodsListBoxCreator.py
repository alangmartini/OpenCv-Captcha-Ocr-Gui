import tkinter as tk


class ListBoxDrag:
  def drag_start(event):
      widget = event.widget
      widget.drag_data = widget.get(tk.ACTIVE)

      # Change the background color of the active item
      widget.itemconfig(tk.ACTIVE, bg='gray')

  def drag_end(event):
      widget = event.widget
      if widget.drag_data:
          # Delete the original list item
          index = widget.index(tk.ACTIVE)
          widget.delete(index)

          # Insert the dragged item at the current position
          drop_index = widget.nearest(event.y)
          widget.insert(drop_index, widget.drag_data)

          # Reset the background color of the item
          widget.itemconfig(drop_index, bg='white')

          widget.drag_data = None 


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

        listbox.drag_data = None
        listbox.bind("<Button-1>", ListBoxDrag.drag_start)
        listbox.bind("<ButtonRelease-1>", ListBoxDrag.drag_end)

        return listbox
