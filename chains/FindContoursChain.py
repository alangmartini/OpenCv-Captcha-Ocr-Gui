from imageprocessor.ImageProcessor import ImageProcessor
from imageprocessor.FindContoursPossibilities import FindContoursMethodsPossibilities
from guicreator.Gui import Gui
from chains.AbsChain import AbsChain


class FindContoursChain(AbsChain):
    name = "FindContours"
    
    @staticmethod
    def process_image(image_processor: ImageProcessor, gui: Gui):
        if not gui.find_contours.check.get():
            return

        retr_method = gui.find_contours.retr_method.get()
        approx_method = gui.find_contours.approx_method.get()

        retr_method = FindContoursMethodsPossibilities.retr_methods[retr_method]
        approx_method = FindContoursMethodsPossibilities.approx_methods[approx_method]

        image_processor.find_contours(retr_method, approx_method)
