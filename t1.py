def tabuada2():
    numero = int(input('Tabuada do número: '))
    for numeros in range(1, 11):
        multiplicacao = numero * numeros
        print(f'{numero} x {numeros} = {multiplicacao}')

tabuada2()