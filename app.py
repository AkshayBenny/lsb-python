from encode import text_encoder
from decode import text_decoder


def main():
    user_choice = str(input(
        "- Enter 1 for encoding text into an image file\n- Enter 2 for decoding text from an image file\n- Enter 3 to exit\nEnter your choice:  "))

    if int(user_choice) == 1:
        text_encoder()
        main()
    elif int(user_choice) == 2:
        text_decoder()
        main()
    elif int(user_choice) == 3:
        print("Exiting...")
        return
    else:
        print("Invalid response!\nPlease Try again.")
        main()


main()
