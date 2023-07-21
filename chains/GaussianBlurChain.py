from imageprocessor.ImageProcessor import ImageProcessor
from guicreator.Gui import Gui
from chains.AbsChain import AbsChain


class GaussianBlurChain(AbsChain):
    name = "GaussianBlur"

    @staticmethod
    def process_image(image_processor: ImageProcessor, gui: Gui):
        if not gui.gaussian_blur.check.get():
            return
        
        size = gui.gaussian_blur.size.get()

        if size & 1 == 0:
            size += 1

        sigma = gui.gaussian_blur.sigma.get()

        image_processor.gaussian_blur(size, sigma)
    
