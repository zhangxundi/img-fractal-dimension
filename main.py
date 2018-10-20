import fractal as fr
from PIL import Imge

def main():
    image = fr.FractalImge()
    path = input('Pls input file name: ')
    image.setName(path.split('.')[0])
    image.setImag(Imge.open(path))
    image = fr.img_pre(image)
    fr.fractal_diamond(image)

if __name__ == '__main__':
    main()
