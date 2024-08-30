from PIL import Image
import piexif

def add_metadata(image_path, output_path, messages):
    image = Image.open(image_path)

    try:
        exif_dict = piexif.load(image.info.get('exif', b''))
    except Exception:
        exif_dict = {'0th': {}, 'Exif': {}, 'GPS': {}, '1st': {}, 'thumbnail': None}

    concatenated_messages = "\n".join(messages)

    exif_dict['0th'][piexif.ImageIFD.ImageDescription] = concatenated_messages.encode('utf-8')
    exif_bytes = piexif.dump(exif_dict)

    image.save(output_path, exif=exif_bytes)

    print(f"Secret Message added. Image saved as {output_path}")

def read_metadata(image_path):
    image = Image.open(image_path)
    exif_data = image.info.get('exif', b'')

    try:
        exif_dict = piexif.load(exif_data)
        hidden_message = exif_dict['0th'].get(piexif.ImageIFD.ImageDescription, b'').decode('utf-8')
        print(f"Hidden messages:\n{hidden_message}")
    except Exception as e:
        print(f"Error reading EXIF data: {e}")