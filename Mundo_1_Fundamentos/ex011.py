"""
Desafio 011
Problema: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
Resolução do problema:
"""
largura = float(input('Informe a largura da parede: '))
altura = float(input('Informe a altura da parede: '))

area = largura * altura
quantidade_tinta = area / 2

print(f'A parede tem uma área de {area}m².')
print(f'Será necessário {quantidade_tinta}L de tinta para pintar a parede.')