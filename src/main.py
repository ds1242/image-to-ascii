from image import ImageClass

def main():
    image = ImageClass()
    image.image_open('../test.jpg')

    image.wait_for_close()


# print(image1.format, image1.size, image1.mode)

# image1.show()
