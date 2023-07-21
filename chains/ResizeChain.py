from imageprocessor.ImageProcessor import ImageProcessor
from guicreator.Gui import Gui
from chains.AbsChain import AbsChain


class ResizeChain(AbsChain):
    name = "Resize"

    @staticmethod
    def process_image(image_processor: ImageProcessor, gui: Gui):
        if not gui.resize.check.get():
            return

        width = gui.resize.width_value.get()
        height = gui.resize.height_value.get()

        image_processor.resize_image(width, height)