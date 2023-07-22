# IN PROGRESS
# Image Processing GUI with OpenCV

This project provides a graphical user interface (GUI) for applying various image processing methods using OpenCV. With a "Process" button that applies
all Tesseract methods in the current altered image.

## Adding a New Method

The process of adding a new method to the application consists of the following steps:

1. **Update `Main.methods_mapping`**: In the `Main` class, add a new entry to the `methods_mapping` dictionary. The key should be a string with the name of the method (this is the name that will appear in the GUI), and the value should be a reference to the Chain class you'll create in step 4 (ex. `"NewMethod": NewMethodChain.NewMethodChain`).

2. **Create the necessary GUI classes**: For each new method, you need to create a new set of GUI classes in the Gui module:
    - A `Creator` class that generates the necessary Tkinter widgets for your method's parameters and stores them.
    - A `Check` class to handle whether the method should be applied or not. This will typically just be a checkbox.
    - Classes for each parameter your method will use. Each parameter will have a corresponding class to create the widget and store the value.

3. **Update the `Gui` class**: Add a new instance of your GUI class to the `Gui` class, so it gets rendered on startup.

4. **Update `ImageProcessor`**: Add a new method to the `ImageProcessor` class for applying your image processing method. This method should take in parameters as needed, apply the cv2 method to the `cv_img` attribute, and then store the result back in `cv_img`.

5. **Create a Chain class**: Create a Chain class to handle applying your method in the Chain of Responsibility pattern. This class should have a static `process_image` method that checks if the method should be applied (using the check class from step 2), and if so, applies the method using the parameters from the GUI and the method you added to `ImageProcessor` in step 4.

## Example

Here's a simple example of adding a new method, `cv2.resize`, to the application:

1. Update `Main.methods_mapping`:

```
class Main:
    methods_mapping = {
        ...
        "Resize": ResizeChain.ResizeChain
    }
    ...
```

2. Create the necessary GUI classes:

```
class ResizeGui:
    def __init__(self, root, process_image_function):
        creator = ResizeCreator(root, process_image_function)

        self.check = ResizeCheck(creator)
        self.width = ResizeWidth(creator)
        self.height = ResizeHeight(creator)
```

3. Update the `Gui` class:

```
class Gui():
    ...
    def __init__(self, method_to_list, process_image_function=None, ocr_function=None):
        ...
        self.resize = ResizeGui(self.root, process_image_function)
```

4. Update `ImageProcessor`:

```
class ImageProcessor:
    ...
    def resize_image(self, width, height):
        self.cv_img = cv2.resize(self.cv_img, (width, height))
```

5. Create a Chain class:

```
class ResizeChain(AbsChain):
    @staticmethod
    def process_image(image_processor: ImageProcessor, gui: Gui):
        if not gui.resize_check.get():
            return

        width = gui.resize_width.get()
        height = gui.resize_height.get()

        image_processor.resize_image(width, height)
```

With these steps, you can easily add any cv2 method to the application. Happy coding!
