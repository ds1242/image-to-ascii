from tkinter import Tk, BOTH, Canvas
from PIL import ImageTk, Image
import math


# ramp = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
def main():
    ramp = "@%#*+=-:. " 
    ramp_length = len(ramp)

    print(ramp_length)
    output = []
    with Image.open('./test.jpg') as image:
        px = image.load()
        width, height = image.size
    # image = image.convert('L')
    # print(image.format, image.size, image.mode)

    # image.show():
    for x in range(width):
        for y in range(height):
            r, g, b = px[x,y]
            gray_val = 0.3 * r + 0.59 * g + 0.11 * b
            gray_val_int = int(gray_val)
            px[x, y] = (int(gray_val), int(gray_val), int(gray_val))
            char = ramp[math.ceil(((ramp_length - 1) * gray_val) / 255)]
            output[x,y] = char
            
    return output

    # image.show()
main()