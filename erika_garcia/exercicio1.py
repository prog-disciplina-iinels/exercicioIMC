peso = 56
altura = 1.70
imc = peso/altura**2

print("Muito abaixo do peso normal ", imc < 17)
print("Abaixo do peso normal ", 17 <= imc < 18.5)
print("Peso normal", 18.5 <= imc < 25.0)
print("Acima do peso normal", 25.0 <= imc < 30)
print("Muito acima do peso normal", imc >= 30)