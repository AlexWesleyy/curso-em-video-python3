"""
Desafio 024
Problema: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
Resolução do problema:
"""
nome = input('Cidade: ').strip().split()
if nome[0].upper() == 'SANTO':
    print('O nome da cidade digitada começa com Santo')
else:
    print('O nome da cidade digitada não começa com Santo')
