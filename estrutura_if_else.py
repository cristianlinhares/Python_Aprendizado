def nota_conceito(valor):
    nota = float(valor)

    if nota > 10 or nota < 0: 
        return "Nota inválida"
    elif nota >= 9.1:
        return "Conceito na prova: A"
    elif nota >= 8.1:
        return "Conceito na prova: A-"
    elif nota >= 7.1:
        return "Conceito na prova: B"
    elif nota >= 6.1:
        return "Conceito na prova: B-"
    elif nota >= 5.1:
        return "Conceito na prova: C"
    elif nota >= 4.1:
        return "Conceito na prova: C-"
    elif nota >= 3.1:
        return "Conceito na prova: D"
    elif nota >= 2.1:
        return "Conceito na prova: D-"
    elif nota >= 1.1:
        return "Conceito na prova: E"
    else: 
        return "Conceito na prova: E-"
    
    
if __name__ =='__main__':
    valor_informado = input('Nota do aluno: ')
    conceito = nota_conceito(valor_informado)
    print(conceito)
    