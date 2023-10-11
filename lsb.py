# Add secret message to encode to message.txt

# imports
from PIL import Image


def string_to_binary():
    f = open("message.txt", "r")
    secret_message = str(f.read())

    # Convert string to Binary
    binary_representation = []
    for character in secret_message:
        binary_value = format(ord(character), '08b')
        binary_representation.append(binary_value)

    secret_message_binary = ''.join(binary_representation)

    return secret_message_binary


def image_to_pixel(path_to_image):
    img = Image.open(path_to_image)

    img_rgb = img.convert('RGB')
    pixels = list(img_rgb.getdata())

    return pixels


message_in_binary = string_to_binary()

for character in message_in_binary:
    # print(int(character))
    pixels = image_to_pixel('./static/images/wolf.bmp')

    for pixel in pixels:
        print(pixel)

        # Pixel is a tuple in the form of (255, 44, 66) and here the last value in the tuple represent blue color
        blue_value = pixel[-1]

        # convert the blue_value to binary
        blue_value_binary = bin(blue_value)[2:]
        print(type(blue_value_binary))
