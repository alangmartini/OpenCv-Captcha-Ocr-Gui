from imageprocessor.ImageProcessor import ImageProcessor
from imageprocessor.ThresholdMethodsPossibilites import ThresholdMethodsPossibilites
from guicreator.Gui import Gui
from chains.AbsChain import AbsChain


class ThresholdChain(AbsChain):
    @staticmethod
    def process_image(image_processor: ImageProcessor, gui: Gui):
        if not gui.threshold.check.get():
            print("falhou")
            return

        t_min = gui.threshold.min.get()
        t_max = gui.threshold.max.get()

        method = gui.threshold.method.get()

        # Not working yet
        # use_auxiliary = gui.threshold.auxiliary_check.get()
        # auxiliary_method = gui.threshold.auxiliary_method.get()

        method_to_use = ThresholdMethodsPossibilites.threshold_methods[method]

        image_processor.threshold_image(t_min, t_max, method_to_use)
