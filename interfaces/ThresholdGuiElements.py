from typing import TypedDict
import tkinter as tk

class ThresholdGuiElements(TypedDict):
    threshold_check: tk.Checkbutton
    threshold_auxiliary_check: tk.Checkbutton
    threshold_min: tk.Scale
    threshold_max: tk.Scale
    threshold_method: tk.StringVar
    threshold_auxiliary_method: tk.StringVar