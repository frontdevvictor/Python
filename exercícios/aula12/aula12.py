nome = str(input('Qual é o seu nome?: '))
# Código abaixo são as Condições Aninhadas
if nome == 'Victor':
    print('Que nome bonito')
elif nome == 'João' or nome == 'Maria' or nome == 'Pedro':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Claúdia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}'.format(nome))
