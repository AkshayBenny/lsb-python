from PIL import Image


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
        if pixel_index <= 10000:
            r, g, b = pixel
            b_binary = bin(b)[-1]
            message_binary_list.append(b_binary)
        pixel_index += 1

    message_binary = ''.join(message_binary_list)
    return message_binary


def binary_to_text(binary_string):
    print("Converting binary to string...")
    char_list = []

    count = 1
    byte = ''
    for bin in binary_string:
        if count <= 8:
            byte = byte + bin
            count += 1
        else:
            count = 1

            # Here we first convert the binary to decimal, then to its corresponding character
            char_list.append(chr(int(byte, 2)))
            byte = ''

    return ''.join(char_list)

# Test function to convert binary to string.
# DELETE ME AFTER


def binary_to_text_test(binary_string, encoding='utf-8'):
    print("Converting binary to string...")

    # Convert the binary string to a bytes object
    byte_data = int(binary_string, 2).to_bytes(
        (len(binary_string) + 7) // 8, byteorder='big')

    # Decode the bytes object using the specified encoding
    text = byte_data.decode(encoding)

    return text


def convert_string_to_groups_of_eight(input_string):
    # Padding to ensure the length is a multiple of 8
    padding = 8 - len(input_string) % 8
    padded_string = input_string + '0' * padding

    # Split the string into groups of 8 characters
    groups_of_eight = [padded_string[i:i+8]
                       for i in range(0, len(padded_string), 8)]

    return groups_of_eight


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
        secret_text = ""

        binary_message = extract_secret_message_from_image(
            './static/images/stego_image.bmp')
        binary_list = convert_string_to_groups_of_eight(binary_message)

        for i in binary_list:
            secret_text += chr(int(i, 2))
        print(secret_text)
        # print(binary_message)
        # secret_message = binary_to_text_test(binary_message)
        # print(secret_message)

    except ValueError as error:
        print("Something went wrong: ", error)


# Operation call
# embed_to_image()
extract_from_image()
