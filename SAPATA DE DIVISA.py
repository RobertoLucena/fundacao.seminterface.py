#PROGRAMA PARA CALCULAR AS DIMENSÕES DE UMA SAPATA DE DIVISA

import math

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-= OTIMIZAÇÃO DE SAPATA DE DIVISA =-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("Utilize sempre PONTO (.) NÃO VÍRGULA (,)")

lado_A = float(input("Qual o Tamanho do Lado A? "))
lado_B = float(input("Qual o Tamanho do Lado B? "))

area = lado_A*lado_B
A = math.sqrt((area/2))

B = A*2

print("\nO Lado maior A pode ser 2 ou 2.5 vezes maior que B.\n"
      "Dessa forma, a sapata otimizada possui as seguintes Dimensões:\n ")

#print("Sua sapata possui uma área de: {} m²" .format(area))
print("O Lado A fica com {} m" .format(A))
print("O Lado B fica com {} m" .format(B))

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-= OTIMIZAÇÃO DE SAPATA DE DIVISA =-=-=-=-=-=-=-=-=-=-=-=-=-=-=")