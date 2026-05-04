# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

'''
Faça um programa que calcule e mostre o volume de uma esfera sendo fornecido o valor de seu raio (R). A fórmula para calcular o volume é: (4/3) * pi * R3. Considere (atribua) para pi o valor 3.14159.

Dica: Ao utilizar'''

## Declaração de variáveis
r = float(input('Digite o Raio: '))

# Calculo para saber o raio de um circulo

resultado = (4.0/3) * 3.14159 * float(r) ** 3


# Saída de dados
print(f'VOLUME = {resultado:.3f} ')
