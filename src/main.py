from tkinter import Tk, BOTH, Canvas
from PIL import ImageTk, Image



root = Tk()
root.title('Image to Convert')
# root.protocol('WM_DELETE_WINDOW', close)


image1 = Image.open('./test.jpg')
print(image1.format, image1.size, image1.mode)

image1.show()
