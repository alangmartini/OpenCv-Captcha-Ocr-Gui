from imageprocessor.ImageProcessor import ImageProcessor
from imageprocessor.CvtColorPossibilities import CvtColorMethodsPossibilities
from guicreator.Gui import Gui
from chains.AbsChain import AbsChain


class CvtColorChain(AbsChain):
    name = "CvtColor"
    
    @staticmethod
    def process_image(image_processor: ImageProcessor, gui: Gui):
        if not gui.cvt_color.check.get():
            return

        method = gui.cvt_color.method.get()

        method_to_use = CvtColorMethodsPossibilities.cvt_color_methods[method]

        image_processor.cvt_color(method_to_use)
