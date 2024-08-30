import os
from PIL import Image
from secretMessage.picture.MessageSystem import add_metadata, read_metadata


def create_image_with_message(image_path, color, message):
    image = Image.new('RGB', (250, 250), color=color)
    image.save(image_path)
    print(f"Image created at {image_path}")

    add_metadata(image_path, image_path, [message])
    print(f"Message added to image at {image_path}")


def get_valid_color():
    valid_colors = ['blue', 'green', 'red', 'yellow', 'cyan', 'magenta', 'white', 'black', 'orange']

    while True:
        color = input(
            f"Enter the color for the new image ues 'list' to see all available colors: ").strip().lower()

        if color == 'list':
            print("Available colors:")
            print(", ".join(valid_colors))
        elif color in valid_colors:
            return color
        else:
            print("Invalid color. Use 'list' to see all available colors.")


def main():
    print("Secret Message Tool by JonasHeilig")
    print("1. Show secret message in an image")
    print("2. Add a secret message to an existing image")
    print("3. Create a new image with a secret message")

    choice = input("Please select an option: ").strip()

    if choice not in ['1', '2', '3']:
        print("Invalid option.")
        return

    if choice == '1':
        image_path = input("Enter the path to the image file: ").strip()
        if not os.path.isfile(image_path):
            print("File does not exist.")
            return
        read_metadata(image_path)

    elif choice == '2':
        image_path = input("Enter the path to the image file: ").strip()
        if not os.path.isfile(image_path):
            print("File does not exist.")
            return
        message = input("Enter the secret message: ").strip()
        add_metadata(image_path, image_path, [message])
        print("Secret message added to the image.")

    elif choice == '3':
        image_path = input("Enter the path to save the new image: ").strip()
        color = get_valid_color()
        message = input("Enter the secret message: ").strip()
        create_image_with_message(image_path, color, message)


if __name__ == "__main__":
    main()
