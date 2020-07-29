from PIL import Image
import os


def resize_image(original_image_path, resized_image_path, alpha):
    image = Image.open(original_image_path)
    size = round(image.size[0] / alpha), round(image.size[1] / alpha)

    image = image.resize(size, Image.ANTIALIAS)
    image.save(resized_image_path)

    return Image.open(resized_image_path)


os.chdir(r'C:\Gry\Files\Django\blog_project\media\test\images')
for i in range(3):
    img = Image.open(os.path.join(os.getcwd(), 'test' + str(i) + '.jpg'))
    print(img.size)
