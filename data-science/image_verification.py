from PIL import Image
import os

#image path in backend to be included

# verify if uploaded image format is jpg/jpeg/png and is not corrupt
def verify_image(image):
    formats = ("jpg", "jpeg", "png")
    try:
        with Image.open(image) as img:
            img.getdata()[0]  # verifies if image is corrupted
            if not image.endswith(formats):
                img.convert('RGB').save("converted_image.jpg", "JPEG")  # converts image to JPG format
            else:
                pass
            print("Uploaded Image has been accepted")
    except (IOError, OSError) as e:
        return e