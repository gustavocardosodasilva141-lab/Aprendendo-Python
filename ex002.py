#numerosnão precisma de "asapas"
print (7+4)

#se "aspas" forem acressentadas ele juntara os numeros 

print ("7"+"4")

nome = 'gustavo'
idade = '21'
peso = '53.4'
print(nome,idade,peso)

#para transformar em função o comamdo INPUT tem q ser adicionado

nome = input ('qual seu nome? ')
idade = input ('qual sua idade? ')
peso = input ('qual seu peso? ')
print ('olá,',nome)
print ('sua idade e',idade)
print ('seu peso e',peso)

nome = input ('qual seu nome? ')
print ('seja bem vindo,{}!'.format(nome))

dia = input('em qual dia voce nasceu? ')
mes = input('em em que mes voce nasceu? ')
ano = input('em que ano voce nasceu? ')
print('voce nasceu no',dia, mes, ano + (' certo? '))

namber = input('digite um numero ')
numero = input('digite outro numero ')
print (namber+numero)

alcool = input('quer beber hj? ')
rosh = input ('e fumar um rosh? ')
print ('tem certeza q quer bebr hoje? {} e fumar? {}'.format(alcool,rosh))