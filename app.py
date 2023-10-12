from PIL import Image
import ctypes


# Utils
def string_to_binary():
    # Read the file
    f = open("message.txt", "r")
    secret_message = str(f.read())

    # Convert string to Binary
    binary_representation = []
    for character in secret_message:
        binary_value = format(ord(character), '08b')
        binary_representation.append(binary_value)

    secret_message_binary = ''.join(binary_representation)
    return secret_message_binary


def embed_message_in_image(image_path, message_in_binary):
    # Open the image and convert to RGB
    img = Image.open(image_path)
    img_rgb = img.convert('RGB')
    pixels = list(img_rgb.getdata())
    print(pixels)

    # For storing the modified pixels
    new_pixels = []

    # Embed the message in the blue channel of the image
    message_index = 0
    for pixel in pixels:

        r, g, b = pixel

        # If there are still bits left to embed
        if message_index < len(message_in_binary):
            # Get the next bit from the message
            bit = int(message_in_binary[message_index])

            # Embed the bit in the blue channel
            if bit == 1 and b % 2 == 0:
                b += 1
            elif bit == 0 and b % 2 == 1:
                b -= 1

            # Move to the next bit
            message_index += 1

        new_pixels.append((r, g, b))

    # Update the image with the new pixels
    img_rgb.putdata(new_pixels)
    img_rgb.save('./static/images/stego_image.bmp')


def stego_image_to_pixels(image_path):
    img = Image.open(image_path)
    img_rgb = img.convert('RGB')
    pixels = list(img_rgb.getdata())

    return pixels


def extract_secret_message_from_image(image_path):
    image_pixels = stego_image_to_pixels(image_path)

    message_binary_list = []
    pixel_index = 0
    for pixel in image_pixels:
        if pixel_index <= 1000:
            r, g, b = pixel
            b_binary = bin(b)[-1]
            message_binary_list.append(b_binary)
        pixel_index += 1

    message_binary = ''.join(message_binary_list)
    print(message_binary)
    return 0

# ========== Main functions ===========


def embed_to_image():
    print("Embeding secret message to image...")

    try:
        stego_image_path = './static/images/wolf.bmp'
        message_in_binary = string_to_binary()

        embed_message_in_image(
            stego_image_path, message_in_binary)
        print(
            "Successfully embeded secret message to the image on path:" + stego_image_path)
    except ValueError as error:
        print("Error:" + error)


def extract_from_image():
    print('Extracting from image...')

    try:
        message = extract_secret_message_from_image(
            './static/images/stego_image.bmp')
        print(message)
    except ValueError as error:
        print("Something went wrong: ", error)


# Operation call
# embed_to_image()
extract_from_image()
