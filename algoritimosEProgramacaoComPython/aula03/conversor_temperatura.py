temp_c = float(input("Digite a temperatura em graus Ceulsius: "))

temp_f = 1.8 * temp_c + 32 # Converte para Fahrenheit
temp_k = temp_c + 273.15 # Converte para Kelvin

print("Temperatura em Celsius: " + str(temp_c))
print("Temperatura em Fahrenheit: " + str(temp_f))
print("Temperatura em Kelvin: " + str(temp_k))

#Digite a temperatura em graus Ceulsius: 25
#Temperatura em Celsius: 25.0
#Temperatura em Fahrenheit: 77.0
#Temperatura em Kelvin: 298.15