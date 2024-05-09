from PIL import Image

# ASCII characters
# ramp = "@%#*+=-:. "
# ramp = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'."
ramp = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width / 1.65
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image


def convert_grayscale(image):
    grayscale_img = image.convert('L')
    return grayscale_img

def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ramp[pixel // 25] for pixel in pixels])
    return characters


def main(new_width=100):
    path = ('./test.jpg')
    if path is None:
        print('invalid path')

    image = Image.open(path)
    
    resized = resize_image(image)
    grayscaled = convert_grayscale(resized)
    new_image_data = pixels_to_ascii(grayscaled)

    pixel_count = len(new_image_data)
    ascii_image = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, pixel_count, new_width)])

    with open('ascii_image.txt', 'w') as f:
        f.write(ascii_image)


main()