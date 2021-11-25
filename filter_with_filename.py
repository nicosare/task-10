from PIL import Image
import numpy as np


def do_filter():
    count_gradations = 5
    mosaic_size = 10
    img = Image.open("test_img.jpg")
    img_data = np.array(img)
    size_img = img_data.shape

    for i in range(0, size_img[0], mosaic_size):
        for j in range(0, size_img[1], mosaic_size):
            paint_cell(img_data, i, j, mosaic_size, count_gradations)

    res = Image.fromarray(img_data)
    res.save("new_filter_result.jpg")


def find_average_brightness(img_data, width, height, mosaic_size):
    return np.average(img_data[width: width + mosaic_size, height: height + mosaic_size])


def paint_cell(img_data, width, height, mosaic_size, count_gradations):
    gradations = 255 // count_gradations
    average_brightness = find_average_brightness(img_data, width, height, mosaic_size)
    img_data[width: width + mosaic_size, height: height + mosaic_size] = average_brightness // gradations * gradations


do_filter()