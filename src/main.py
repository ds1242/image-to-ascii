from image import ImageClass

def main():
    image = ImageClass()
    image.image_open('./test.jpg')

    image.wait_for_close()



# image1.show()
main()
