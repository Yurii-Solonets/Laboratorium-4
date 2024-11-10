# a
imię = input("Podaj swoje imię: ")
print(f"Witaj {imię}!")

# b
wiek = input("Podaj swój wiek: ")
print(f"Twój wiek to: {wiek}")

# c
imię_nazwisko = input("Podaj swoje imię i nazwisko: ")
imię, nazwisko = imię_nazwisko.split()
inicjały = imię[0].upper() + nazwisko[0].upper()
print(f"Iniciały: {inicjały}")

# d
łańcuch = input("Podaj łańcuch: ")
for _ in range(5):
    print(łańcuch)

# e
łańcuch1 = input("Podaj pierwszy łańcuch: ")
łańcuch2 = input("Podaj drugi łańcuch: ")
polaczony = łańcuch1 + łańcuch2
print(f"Połączony łańcuch: {polaczony}")

# f
łańcuch3 = input("Podaj pierwszy łańcuch: ")
łańcuch4 = input("Podaj drugi łańcuch: ")
połowa1 = len(łańcuch3) // 2
połowa2 = len(łańcuch4) // 2

nowy_łancuch = łańcuch3[:połowa1] + łańcuch4[połowa2:]
print("Nowy łańcuch (połączenie połowy pierwszego i połówy drugiego):", nowy_łancuch)