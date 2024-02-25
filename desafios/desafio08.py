# medida = float(input('Uma distância em metros: '))
# cm = medida * 100
# mm = medida * 1000
# print('A medida de {}m, corresponde a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))

medida = float(input('Digite uma distancia: '))
dam = medida / 10
hm = medida / 100
km = medida / 1000
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('A distancia de {} é igual a {}dam \n {}hm \n {}km \n {}dm \n {}cm \n {}mm'.format(medida, dam, hm, km, dm, cm, mm))