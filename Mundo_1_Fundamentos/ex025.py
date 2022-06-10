"""
Desafio 025
Problema: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
Resolução do problema:
"""
nome = input('Nome: ').strip()
if 'SILVA' in nome.upper():
    print('Tem silva no seu nome!')
else:
    print('Não Tem silva no seu nome!')