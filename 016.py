porcentagem = float(input('digite quanto % esta dando de desconto: %'))
valor = float(input('digiete o valor do produto: R$'))
v1 = valor * porcentagem / 100
desconto = valor - v1
print('A porcentagem de desconto e de %{:.2f}, o valor do produto e de R${:.2f}, a quantia de desconto e R${:.2f} o total do produto com o desconto e R${:.2f}'.format(porcentagem, valor,v1, desconto )) 