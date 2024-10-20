from PIL import Image


def check_metadata(image_path):
    try:
        img = Image.open(image_path)
        metadata = img.info
        return metadata
    except Exception as e:
        return str(e)
