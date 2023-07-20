import tkinter as tk
from imageprocessor.ThresholdMethodsPossibilites import ThresholdMethodsPossibilites
from interfaces.ThresholdGuiElements import ThresholdGuiElements

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

class ThresholdCreator:
  def create_min_scale(root, process_image_function):
      threshold_min = tk.Scale(root, label="min",from_=1, to=255, orient=tk.HORIZONTAL, command=process_image_function)
      threshold_min.pack()

      return threshold_min

  def create_max_scale(root, process_image_function):
      threshold_max = tk.Scale(root, label="max", from_=1, to=255, orient=tk.HORIZONTAL, command=process_image_function)
      threshold_max.set(255)
      threshold_max.pack()

      return threshold_max

  def create_method_option_menu(root, process_image_function):
      all_methods = list(ThresholdMethodsPossibilites.threshold_methods.keys())
      selected_threshold_method = tk.StringVar(root)
      selected_threshold_method.set(all_methods[0])

      # selected_threshold_method.trace('w', fn)

      threshold_methods_dropdown = tk.OptionMenu(root, selected_threshold_method,*all_methods, command=process_image_function)
      threshold_methods_dropdown.pack()

      return selected_threshold_method
  
  def create_auxiliary_method_option_menu(root):
      all_methods = list(ThresholdMethodsPossibilites.threshold_auxiliary_methods.keys())
      selected_threshold_method = tk.StringVar(root)

      selected_threshold_method.set(all_methods[0])

      threshold_methods_dropdown = tk.OptionMenu(root, selected_threshold_method,*all_methods)
      threshold_methods_dropdown.pack()

      return selected_threshold_method
  
  def create_method_checkbox(root):
      is_method_checked = tk.IntVar(root)
      method_check = tk.Checkbutton(root, text='Use auxiliary method', variable=is_method_checked)
      method_check.pack()

      return is_method_checked
  
  def create_auxiliary_method_checkbox(root):
      is_threshold_auxiliary_checked = tk.IntVar(root)
      threshold_auxiliary_check = tk.Checkbutton(root, text='Auxiliary Threshold', variable=is_threshold_auxiliary_checked) 
      threshold_auxiliary_check.pack()

      return is_threshold_auxiliary_checked

      
class ElementsCreator:
    def create_blur_check(self, root):
      is_blur_checked = tk.IntVar(root)
      blur_check = tk.Checkbutton(root, text='Blur', variable=is_blur_checked)
      blur_check.pack()

      blur_scale = tk.Scale(root, from_=1, to=10, orient=tk.HORIZONTAL)
      blur_scale.pack()

      blur_scale = blur_scale
      blur_check = blur_check

      return [is_blur_checked, blur_scale]
    
    def create_color_check(self, root):
      is_color_checked = tk.IntVar(root)
      color_check = tk.Checkbutton(root, text='Convert color', variable=is_color_checked)
      color_check.pack()

      return is_color_checked
          
    def create_listbox(self, root, method_to_use):
      listbox = tk.Listbox(root)
      listbox.pack()

      for item in method_to_use:
          listbox.insert(tk.END, item)

      listbox.drag_data = None
      listbox.bind("<Button-1>", ListBoxDrag.drag_start)
      listbox.bind("<ButtonRelease-1>", ListBoxDrag.drag_end)

      return listbox
    
    def create_threshold(self, root, process_image_function) -> ThresholdGuiElements:
      is_threshold_checked = tk.IntVar(root)
      threshold_check = tk.Checkbutton(root, text='Threshold', variable=is_threshold_checked)
      threshold_check.pack()

           
      threshold_min = Threshold.create_min(root, process_image_function)
      threshold_max = Threshold.create_max(root, process_image_function)

      threshold_method = Threshold.create_method(root, process_image_function)

      is_threshold_auxiliary_checked = tk.IntVar(root)
      threshold_auxiliary_check = tk.Checkbutton(root, text='Auxiliary Threshold', variable=is_threshold_auxiliary_checked) 
      threshold_auxiliary_check.pack()
      
      threshold_auxiliary_method = Threshold.create_auxiliary_method(root)

      # Return methods as a dict instead of array
      return {
        "threshold_check": is_threshold_checked,
        "threshold_auxiliary_check": is_threshold_auxiliary_checked,
        "threshold_min": threshold_min,
        "threshold_max": threshold_max,
        "threshold_method": threshold_method,
        "threshold_auxiliary_method": threshold_auxiliary_method
      }