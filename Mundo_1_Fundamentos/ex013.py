"""
Desafio 013
Problema: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
Resolução do problema:
"""
salario = float(input('Informe seu sálario: R$'))

salario_aumento = salario + (salario * 15 / 100)

print(f'Salário final: R${salario_aumento:.2f}')