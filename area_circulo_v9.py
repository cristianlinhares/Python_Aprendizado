import math


def circulo(raio):
    area_circ = math.pi * (float(raio)**2)
    return area_circ

if __name__ == '__main__': 
    raio = input('Informe o raio: ')
    area = circulo(raio)

print('Área do círculo: ', area)
    
