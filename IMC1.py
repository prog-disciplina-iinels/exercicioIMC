peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura em metros: "))
imc = peso/altura**2

if(imc < 17):
   print("Muito abaixo do peso ideal")
elif(17 <= imc < 18.5):
   print("Abaixo do peso ideal")
elif(18.5 <= imc < 25.0):
   print("Peso ideal")
elif(25.0 <= imc < 30):
   print("Acima do peso ideal")
else:
   print("Muito acima do peso ideal", imc >= 30)