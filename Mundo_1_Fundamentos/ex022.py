"""
Desafio 022
Problema: Crie um programa que leia o nome completo de uma pessoa e mostre:
  - O nome com todas as letras maiúsculas e minúsculas.
  - Quantas letras ao todo(sem considerar espaços)
  - Quantas letras tem o primeiro nome.
Resolução do problema:
"""
from itertools import count


nome = input('Informe seu nome completo: ')
print(f'Nome Maíusculo: {nome.upper()}')
print(f'Nome minúsculo: {nome.lower()}')
print(f'Quantas letras que o nome possue sem espaços: {len(nome)-nome.count(" ")}')
dividido=nome.split()
print(f'Quantas letras tem o primeiro nome: {len(dividido[0])}')