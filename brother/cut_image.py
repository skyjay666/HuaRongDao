'''
将一张图片切为9张图
'''
from PIL import Image
import sys


def Cut_image(image):
    width, height = image.size
    item_width = int(width / 3)
    box_list = []
    for i in range(0, 3):
        for j in range(0, 3):
            box = (j * item_width, i * item_width, (j + 1) * item_width,
                   (i + 1) * item_width)  # Image.crop(left, up, right, below)
            box_list.append(box)

    image_list = [image.crop(box) for box in box_list]
    return image_list


# 保存
def save_images(folder, image_list):
    index = 1
    for image in image_list:
        image.save(folder + str(index) + '.jpg')
        index += 1