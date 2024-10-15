import math

# Função para calcular a hipotenusa
def calcular_hipotenusa(cateto1, cateto2):
    return math.sqrt(cateto1**2 + cateto2**2)

# Solicitando os valores dos catetos do usuário
cateto1 = float(input("Digite o valor do primeiro cateto: "))
cateto2 = float(input("Digite o valor do segundo cateto: "))

# Calculando a hipotenusa
hipotenusa = calcular_hipotenusa(cateto1, cateto2)

# Exibindo o valor da hipotenusa
print(f"O valor da hipotenusa é: {hipotenusa:.2f}")
