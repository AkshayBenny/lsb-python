from PIL import Image


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

    return img_rgb


message_in_binary = string_to_binary()
stego_image = embed_message_in_image(
    './static/images/wolf.bmp', message_in_binary)
