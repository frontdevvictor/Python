velocidade = float(input('Qual é a velocidade do carro?: '))
if velocidade > 80:
    print('\033[91m' + 'MULTADO! Você excedeu o limite permitido que é de 80 km/h')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')

# Neste código, \033[91m é um escape sequence ANSI que representa a cor vermelha no terminal.
# Isso deve exibir o texto "MULTADO! Você excedeu o limite permitido que é de 80 km/h" em vermelho.