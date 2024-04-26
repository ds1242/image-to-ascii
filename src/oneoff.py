from tkinter import Tk, BOTH, Canvas
from PIL import ImageTk, Image


# ramp = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'.'
with Image.open('./test.jpg') as image:
    px = image.load()
    width, height = image.size
# image = image.convert('L')
# print(image.format, image.size, image.mode)

# image.show():
for x in range(width):
    for y in range(height):
        r, g, b = px[x,y]
        gray_val = int(0.3 * r + 0.59 * g + 0.11 * b)
        px[x, y] = (gray_val, gray_val, gray_val)

image.show()
