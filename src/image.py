from tkinter import Tk, BOTH, Canvas
from PIL import ImageTk, Image

class ImageClass():
    def __init__(self):
        self.__root = Tk()
        self.__root.title('ASCII Image')
        self.__root.protocol('WM_DELETE_WINDOW", self.close)
        self.__running = False


    def image_open(self, file_path):
        return Image.open(file_path)

    def wait_for_close(self):
        self.__running = True
        print('window close')

    def close(self):
        self.__running = False
