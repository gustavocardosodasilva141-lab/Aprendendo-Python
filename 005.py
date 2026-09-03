print ('oi'*5)

print('='*20)

n1 = int(input('digite um valor: '))
n2 = int(input('digite outro: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e =  n1 ** n2
print('A soma e {} \n o produto e {} e a divisão e {}'.format(s, m, d), end=' ')
print('Divisão inteira {} e potência {}'.format(di, e))
# , end=' ') para n quebrar o codigo na linha 
# \n para quebrar a linha