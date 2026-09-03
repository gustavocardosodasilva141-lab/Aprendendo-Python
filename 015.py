# O valor de um produto ao ser passado no credito tem um aumento de 6$, ja se pago a vista ou me pix 8% de desconto.

valor = float(input('qual o valor do produto? R$:'))
desconto = valor * 8 / 100
v1 = valor - desconto
juros = valor * 6 / 100
v2 = valor + juros
print('o valor do produto e R${:.2f} o valor do desconto e de R${:.2f} com o desconto o produto vai para R${:.2f}'.format(valor, desconto, v1))
print('O valor do produto e R${:.2f} o valor do juros e de R${:.2f} com o juros o produto vai para R${:.2f}'.format(valor, juros, v2))