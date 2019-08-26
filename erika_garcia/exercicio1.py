peso = float(input("digite o peso: "))
altura = float(input ("digite a altura: "))
imc = peso/altura**2


if(imc < 17):
    print("Muito abaixo do peso normal ")
elif (17 <= imc < 18.5):
    print("Abaixo do peso normal ")
elif (18.5 <= imc < 25.0):
    print("Peso normal")
elif ( 25.0 <= imc < 30):
    print("Acima do peso normal")
else:
    print("Muito acima do peso normal")
