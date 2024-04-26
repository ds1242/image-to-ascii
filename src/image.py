from tkinter import Tk, BOTH, Canvas
from PIL import ImageTk, Image

class ImageClass():
    def __init__(self, file_path):
        self.__root = Tk()
        self.__root.title('ASCII Image')

        self.__image_path = file_path

    def image_open(self):
        return Image.open(self.__image_path)


    def show_image(self):
        pass
