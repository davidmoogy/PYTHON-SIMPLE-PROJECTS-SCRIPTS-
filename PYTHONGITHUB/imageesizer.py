from PIL import Image
import os

def resize_images(directory, width, height):
    for filename in os.listdir(directory):
        if filename.endswith(('.jpg', '.png')):
            img_path = os.path.join(directory, filename)
            img = Image.open(img_path)
            img = img.resize((width, height))
            img.save(img_path)
            print(f"Resized {filename}")

resize_images('path/to/images', 800, 600)
