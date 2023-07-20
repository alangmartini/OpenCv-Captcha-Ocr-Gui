from imageprocessor.ImageProcessor import ImageProcessor
from guicreator.Gui import Gui
from chains.AbsChain import AbsChain


class BlurChain(AbsChain):
    @staticmethod
    def process_image(image_processor: ImageProcessor, gui: Gui):
        if not gui.blur_check.get():
            return
        
        blur_amount = gui.blur_scale.get()

        image_processor.blur_image(blur_amount)
    
