h = float(input("Informe sua altura: "))
sexo = input("Informe seu sexo m/f: ").lower()

if sexo == 'm':
    peso_ideal = (72.7*h) - 58
    print("Seu peso ideal é de ", peso_ideal)

elif sexo == 'f':
    peso_ideal = (62.1*h) - 44.7
    print("Seu peso ideal é de ", peso_ideal)

else:
    print("Sexo não reconhecido. ")
