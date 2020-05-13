operacao = str(input("Qual operação matemática deseja realizar?"))
primeiro_numero = float(input('Informe o primeiro número: '))
segundo_numero = float(input('Informe o segundo número: '))


if operacao == 'soma':
        print('O resultado é',primeiro_numero + segundo_numero)
elif operacao == 'multiplicação':
        print('O resultado é',primeiro_numero * segundo_numero)
elif operacao == 'divisão':
        print('O resultado é',primeiro_numero/segundo_numero)
elif operacao == 'subtração':
        print('O resultado é',primeiro_numero - segundo_numero)
else:
    print('Erro na operação')
    