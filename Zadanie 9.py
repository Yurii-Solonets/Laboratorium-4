lista_zakupów = {
    "chleb": 4.50,
    "mleko": 3.20,
    "masło": 7.50,
    "ser": 12.00,
    "jajka": 10.00,
    "pomidory": 5.30,
}

print("Lista zakupów: ")
for artykul, kwota in lista_zakupów.items():
    print(f"{artykul}: {kwota:.2f} zł")

suma_wydatków = sum(lista_zakupów.values())
print("\nSuma wydatków: " f"{suma_wydatków:.2f} zł")