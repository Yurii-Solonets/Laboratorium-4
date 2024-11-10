Moja_lista=[1, 17, 3, 5, 3, 4, 86, 90, 2, 21]

Moja_lista.append(100)
print("Po dodawanie elementu 100:", Moja_lista)

Moja_lista.insert(2, 50)
print("Po dodawaniu elementu 50 na indeks 2:", Moja_lista)

Moja_lista.remove(3)
print("Po usunięciu pierwsziego wstąpienia liczby 3:", Moja_lista)

element_usuniety = Moja_lista.pop(4)
print(f"Po usunięciu elementu na indiksie 4:", Moja_lista)

indeks_17 = Moja_lista.index(17)
print("Indeks pierwszego wstąpienia liczby 17:", indeks_17)

liczba_trojki = Moja_lista.count(3)
print("Lista wystąpień liczby 3:", liczba_trojki)

Moja_lista.sort()
print("Lista po posortowaniu rosnąco:", Moja_lista)

Moja_lista.reverse()
print("Lista po odwróceniu kolejności:", Moja_lista)

kopiowana_lista = Moja_lista.copy()
print("Skopiowana lista:", kopiowana_lista)

Długość_lista = len(Moja_lista)
print("Długość lista:", Długość_lista)

większe_lista = max(Moja_lista)
print("Największa wartość:", większe_lista)

mniejsza_lista = min(Moja_lista)
print("Najmniejsza wartość:", mniejsza_lista)

suma_lista = sum(Moja_lista)
print("Suma listy:", suma_lista)