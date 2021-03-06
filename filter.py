from PIL import Image
import numpy as np


def do_filter():
    """
    :return: обработанное фильтром изображение
    """
    path_img = input("Введите путь к изображению: ")
    name = input("Введите имя выходного изображения: ")
    count_gradations = int(input("Введите количество градаций: "))
    mosaic_size = int(input("Введите размер мозайки: "))
    img = Image.open(path_img)
    img_data = np.array(img)
    size_img = img_data.shape
    for i in range(0, size_img[0], mosaic_size):
        for j in range(0, size_img[1], mosaic_size):
            paint_cell(img_data, i, j, mosaic_size, count_gradations)

    res = Image.fromarray(img_data)
    path_output = path_img[0:path_img.rindex('\\') + 1]
    res.save(f"{path_output}{name}")


def find_average_brightness(img_data, width, height, mosaic_size):
    """
    :param img_data: изображение, представленное в виде массива
    :param width: позиция по ширине изображения
    :param height: позиция по высоте изображения
    :param mosaic_size: размер ячейки
    :return: среднее значение яркости выбранной области изображения

    >>> find_average_brightness(np.array([[[1,1,1],[1,1,1]],[[1,1,1],[1,1,1]]]),0,0,2)
    1.0
    >>> find_average_brightness(np.array([[[2,2,2],[2,2,2,]],[[2,2,2],[2,2,2]]]),0,0,2)
    2.0
    """
    return np.average(img_data[width: width + mosaic_size, height: height + mosaic_size])


def paint_cell(img_data, width, height, mosaic_size, count_gradations):
    """
    :param img_data: изображение, представленное в виде массива
    :param width: позиция по ширине изображения
    :param height: позиция по высоте изображения
    :param mosaic_size: размер ячейки
    :param count_gradations: количество градаций
    :return: перекрашенная ячейка изображения
    """
    gradations = 255 // count_gradations
    average_brightness = find_average_brightness(img_data, width, height, mosaic_size)
    img_data[width: width + mosaic_size, height: height + mosaic_size] = average_brightness // gradations * gradations


do_filter()