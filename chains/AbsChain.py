from abc import ABC, abstractmethod
from imageprocessor.ImageProcessor import ImageProcessor
from guicreator.Gui import Gui


class AbsChain(ABC):
    @staticmethod
    @abstractmethod
    def process_image(image_processor: ImageProcessor, gui: Gui):
        pass
