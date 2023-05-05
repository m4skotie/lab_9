import csv
import os
from PIL import Image, ImageFilter

def z1():
    images = 'C:/Users/user/PycharmProjects/lab_9/pics'

    if not os.path.exists('C:/Users/user/PycharmProjects/lab_9/mod_pics'):
        os.mkdir('C:/Users/user/PycharmProjects/lab_9/mod_pics')

    for i in os.listdir(images):
        image = Image.open(os.path.join(images,i))
        image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
        image.save(os.path.join('C:/Users/user/PycharmProjects/lab_9/mod_pics', i))
def z2():
    images = 'C:/Users/user/PycharmProjects/lab_9/pics'

    if not os.path.exists('C:/Users/user/PycharmProjects/lab_9/mod_pics2'):
        os.mkdir('C:/Users/user/PycharmProjects/lab_9/mod_pics2')

    for i in os.listdir(images):
        if i.endswith('.jpg'):
            image = Image.open(os.path.join(images,i))
            image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
            image.save(os.path.join('C:/Users/user/PycharmProjects/lab_9/mod_pics2', i))
def z3():
    with open("data.csv") as a:
        list=[]
        s = 0
        reader = csv.reader(a, delimiter = ",")
        print("Нужно купить")
        for row in reader:
            a, b, c = row
            b = int(b)
            c = int(c)
            s+=b*c
            print(f'{row[0]} - {row[1]} шт. за {row[2]} руб.')
        print("Итоговая сумма =", s)

z3()