km = float(input('digite quantos KM vc percorreu: ')) 
dias = int(input('digite a quatindade de dias que você usou o carro: '))

k = km * 0.15 
d = dias * 60
t = k + d
print('O total em dinheiro dos kms rodados são RS{:.2f} e dos dias rodados são {:.2f} ao total ficam {:.2f}'.format(k, d, t))