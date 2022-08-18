#Faça um algoritmo que leia um número inteiro e imprima seu antecessor e seu sucessor.

valor = int(input('digite um número inteiro e descubra seu antecessor e seu sucessor:'))
print(f"Seu número escolhido é {valor}")

antecessor = valor - 1
print(f"Seu antecessor é {antecessor}")
sucessor = valor + 1 
print(f"Seu sucessor é {sucessor}")