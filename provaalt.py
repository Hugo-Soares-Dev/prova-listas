""" Faça um programa que solicite ao usuário que digite 10 valores para preencher uma lista. Em seguida, o programa deve separar os números pares e ímpares em listas diferentes. Por fim, exiba na tela os números pares, os números ímpares em uma tupla, a quantidade de números pares e ímpares presentes na lista, e a soma de todos os números pares e ímpares, respectivamente."""

lista = []
par = []
impar = []

for i in range(1,11):
    numero = int(input(f'digite o {i}° numero: '))
    lista.append(numero)

for num in lista:
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

tupla_par = tuple(par)
tupla_impar = tuple(impar)


print(f'Foram encontrados ({len(par)}) numeros pares.\nOs numeros pares são:{tupla_par}\n a soma dos pares corresponde a: ({sum(par)}).')

print(f'Foram encontrados ({len(impar)}) numeros impares.\n são eles:{tupla_impar}\n a soma dos impares corresponde ao valor de  ({sum(impar)}).')

print(f'a soma de todos os numeros encontrados é de ({sum(lista)}).')