distância = float(input('Qual é a distância de sua viagem?: '))
print('Você está prestes a começar uma viagem de {}Km.')
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print('E o preço da sua passagem será de R$:{:.2f}'.format(preço))
