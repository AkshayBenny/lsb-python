from PIL import Image


def encode():
    secret_text = str(input("Enter secret text:"))
    binary_data = text_to_binary(secret_text)
    embed_binary_in_image("./static/skyrim.bmp", binary_data)


def text_to_binary(text):
    binary_list = []
    for char in text:
        binary_list.append(format(ord(char), '08b'))
    return {
        "binary": "".join(binary_list),
        "binary_length": len("".join(binary_list))
    }


def embed_binary_in_image(image_path, binary_data):
    img_rgb = Image.open(image_path).convert("RGB")
    pixels = list(img_rgb.getdata())
    new_pixels = []
    binary_message_read_index = 0
    for pixel in pixels:
        r, g, b = pixel
        if binary_message_read_index >= int(binary_data["binary_length"]):
            new_pixels.append(pixel)
        else:
            channel_binary = bin(b)[2:]
            print(channel_binary)
            new_pixels.append((r, g, int(
                channel_binary[:-1] + binary_data["binary"][binary_message_read_index])))
        binary_message_read_index += 1

    img_rgb.putdata(new_pixels)
    img_rgb.save('./static/stego_image.bmp')


encode()
