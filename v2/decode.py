from PIL import Image


def decode():
    img_rgb = Image.open("./static/stego_image.bmp")
    pixels = list(img_rgb.getdata())
    binary_string = ''
    text_string = ''

    for pixel in pixels:
        r, g, b = pixel
        blue_binary = format(b, '08b')
        least_bit = blue_binary[-1]
        binary_string += least_bit

    # Padding to ensure the length is a multiple of 8
    padding = 8 - len(binary_string) % 8
    binary_string = binary_string + '0' * padding

    # Split binary string into groups of 8 bits
    groups_of_eight = [binary_string[i:i+8]
                       for i in range(0, len(binary_string), 8)]
    print(groups_of_eight[0:100])
    for byte in groups_of_eight:
        decimal = int(byte, 2)
        text = chr(decimal)
        text_string += text

    # print("Decoded text (in groups of eight bits):", text_string)


decode()
