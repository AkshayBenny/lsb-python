from PIL import Image

HEADER_SIZE = 254


def text_encoder():
    secret_text = str(input("Enter secret text:"))
    binary_data = text_to_binary(secret_text + "DELIMITTER")
    embed_binary_in_image("./static/skyrim.bmp", binary_data)
    print("Embedding completed successfully!")


def text_to_binary(text):
    print("Converting text to binary...")
    binary_list = []
    for char in text:
        binary_list.append(format(ord(char), '08b'))
    print("Converted text to binary!")
    return {
        "binary": "".join(binary_list),
        "binary_length": len("".join(binary_list))
    }


def embed_binary_in_image(image_path, binary_data):
    print("Embedding binary data into the image...")
    img_rgb = Image.open(image_path).convert("RGB")
    width, height = img_rgb.size

    pixels = list(img_rgb.getdata())
    new_pixels = []
    binary_message_read_index = 0

    for h in range(height):
        for w in range(width):
            if h * width + w < HEADER_SIZE:
                new_pixels.append(pixels[h * width + w])
            elif binary_message_read_index < int(binary_data["binary_length"]):
                r, g, b = pixels[h * width + w]
                channel_binary = format(b, '08b')
                new_pixel = (r, g, int(
                    channel_binary[:-1] + binary_data["binary"][binary_message_read_index], 2))
                new_pixels.append(new_pixel)
                binary_message_read_index += 1
            else:
                new_pixels.append(pixels[h * width + w])

    img_rgb.putdata(new_pixels)
    img_rgb.save('./static/stego_image.bmp')
