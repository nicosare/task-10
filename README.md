# task-10 Галкин Даниил
***
## Время работы старого фильтра:
![время работы старого фильтра](https://github.com/nicosare/task-10/blob/main/screenshots/old_filter.png)

## Время работы нового фильтра:
![время работы нового фильтра](https://github.com/nicosare/task-10/blob/main/screenshots/filter.png)

На данный момент новый фильтр работает медленнее, так как на ввод данных уходит большая часть времени работы программы.
Для более справедливого сравнения проверим время работы аналогичного кода, но без ввода данных.

## Время работы фильтра без ввода данных:
![время работы фильтра без ввода данных](https://github.com/nicosare/task-10/blob/main/screenshots/filter_with_filename.png)

Как мы видим, программа без ввода работает гораздо быстрее, чем старый фильтр.
В большей части этому поспособствовала замена ручных циклов на матричные преобразования с помощью **библиотеки NumPy**.
***
## Тестовое изображение:
![тестовое изображение](https://github.com/nicosare/task-10/blob/main/test_img.jpg)

## Результат работы старого фильтра:
![результат работы старого фильтра](https://github.com/nicosare/task-10/blob/main/old_filter_result.jpg)

## Результат работы нового фильтра:
![результат работы нового фильтра](https://github.com/nicosare/task-10/blob/main/new_filter_result.jpg)
***
## Результат тестов DocTest функции find_average_brightness:
![Результат работы DocTest](https://github.com/nicosare/task-10/blob/main/screenshots/doctest.png)


Через отладчик вывел на экран в свойствах изображения ширину и высоту, а также тип изображения. 
Также в отладчике выведены значения ширины блока и количество градаций серого.
![Работа отладчика](https://github.com/nicosare/task-10/blob/main/screenshots/debug.png)

