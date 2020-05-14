from random import randint
sortear_dado = randint(1,7)
    
for x in range(1,7):
        if x %2 != 0:
            print(f'Errou: {x}')
            continue
        elif x == sortear_dado:
            print(f'Acertou: {x}')
print('FIM')
