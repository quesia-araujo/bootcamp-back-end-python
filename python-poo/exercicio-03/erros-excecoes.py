def calcular_media(valores):
    tamanho = 0
    soma = 0.0
    for i, valor in enumerate(valores):
        soma += valor
        i += 1
        tamanho += 1
    return soma/tamanho

continuar = True
valores = []
while continuar:
    try:
        valor = input('Digite um número para entrar na sua media ou "ok" para calcular o valor: ')
        if valor.lower() == 'ok':
            continuar = False
        else:
            valores.append(float(valor))
    except TypeError as e:
        print(e)

media = calcular_media(valores)
print('A média calculada para os valores {} foi de {}'.format(valores, media))