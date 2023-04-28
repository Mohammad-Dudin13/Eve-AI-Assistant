import tkinter as tk
from PIL import Image, ImageTk
from itertools import count, cycle

class ImageLabel(tk.Label):
    """
    A Tkinter label widget that displays an animated image. It can load an animated image from a file path and display it
    using the PIL library. The widget cycles through each frame of the image and displays it with a given delay time.
    """

    def load(self, im):
        """
        Loads an animated image from a file path or PIL Image object and prepares the widget to display it.

        Args:
            im: A file path or a PIL Image object representing the animated image.
        """
        if isinstance(im, str):
            # If the input is a string, open it as an image file
            im = Image.open(im)

        frames = []
        try:
            # Iterate over each frame of the animated image and create a PhotoImage object from it
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            # When the end of the image file is reached, continue to the next step
            pass

        # Create an iterator that cycles through the PhotoImage objects
        self.frames = cycle(frames)

        try:
            # Try to get the delay time of the animated image from its metadata
            self.delay = im.info['duration']
        except:
            # If no delay time is specified in the metadata, set it to 100ms by default
            self.delay = 100

        if len(frames) == 1:
            # If there is only one frame in the animated image, display it directly
            self.config(image=next(self.frames))
        else:
            # If there are multiple frames, start displaying the frames with a given delay time
            self.next_frame()

    def unload(self):
        """
        Unloads the animated image from the widget and removes it.
        """
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        """
        Displays the next frame of the animated image with a given delay time.
        """
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)
