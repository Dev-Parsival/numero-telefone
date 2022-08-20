import phonenumbers
from phonenumbers import geocoder, carrier

numeroTelefone = input("Digite seu numero no modelo +5511987654321  : ")

numero = phonenumbers.parse(numeroTelefone)

operadora = carrier.name_for_number(numero, 'pt-br')

estado = geocoder.description_for_number(numero, 'pt-br')

print(" ")
print(" A operadora é: " + operadora)
print(" ")
print(" O estado é: " + estado)
