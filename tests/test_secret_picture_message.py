from secretMessage.picture.MessageSystem import add_metadata, read_metadata
from PIL import Image


def test_add_and_read_metadata():
    input_image = "test_image.png"
    output_image = "test_image_with_message.png"
    messages = [
        "This is a hidden message.",
        "Message 2.",
        "And finally, let' look if it works!?"
    ]

    image = Image.new('RGB', (100, 100), color='white')
    image.save(input_image)
    print(f"Created test image: {input_image}")

    print(f"Adding metadata to {input_image}...")
    add_metadata(input_image, output_image, messages)
    print(f"Metadata added. Saved as: {output_image}")

    print(f"Reading metadata from {output_image}...")
    read_metadata(output_image)

    print(f"Test complete. Images '{input_image}' and '{output_image}' have been created and not deleted.")


if __name__ == "__main__":
    test_add_and_read_metadata()
