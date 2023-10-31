from PIL import Image

HEADER_SIZE = 254


def text_decoder():
    print("Image decoding started...")
    delimiter_found = False
    img_rgb = Image.open("./static/stego_image.bmp")
    width, height = img_rgb.size

    pixels = list(img_rgb.getdata())
    binary_string = ''
    text_string = ''

    for y in range(height):
        for x in range(width):
            if y * width + x >= HEADER_SIZE:
                r, g, b = pixels[y * width + x]
                blue_binary = format(b, '08b')
                least_bit = blue_binary[-1]
                binary_string += least_bit

                if len(binary_string) % 8 == 0:
                    byte = binary_string[-8:]
                    text_string += chr(int(byte, 2))
                    if "DELIMITTER" in text_string:
                        delimiter_found = True
                        break

            if delimiter_found:
                break

        if delimiter_found:
            break

    secret_text = text_string.replace("DELIMITTER", " ")
    print(f"Decoded text from the image: {secret_text}")
