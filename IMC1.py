peso = 70
altura = 1.58
imc = peso/altura**2

print("Muito abaixo do peso ideal", imc < 17)
print("Abaixo do peso ideal", 17 <= imc < 18.5)
print("Peso ideal", 18.5 <= imc < 25.0)
print("Acima do peso ideal", 25.0 <= imc < 30)
print("Muito acima do peso ideal", imc >= 30)
