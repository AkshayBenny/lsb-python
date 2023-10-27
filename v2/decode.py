from PIL import Image


def text_decoder():
    print("Image decoding started...")
    img_rgb = Image.open("./static/stego_image.bmp")
    pixels = list(img_rgb.getdata())
    binary_string = ''
    text_string = ''
    print("Extracting pixels...")
    for pixel in pixels:
        r, g, b = pixel
        blue_binary = format(b, '08b')
        least_bit = blue_binary[-1]
        binary_string += least_bit
    print("Extraction complete!")
    print("Taking data from pixels...")
    padding = 8 - len(binary_string) % 8
    binary_string = binary_string + '0' * padding
    groups_of_eight = [binary_string[i:i+8]
                       for i in range(0, len(binary_string), 8)]

    for byte in groups_of_eight[0:15]:
        print(type(chr(int(byte, 2))))
        text_string += chr(int(byte, 2))

    print(f"Decoded text from the image: {text_string}")
