imiona = ["Anna", "Marek", "Zofia", "Bartek"]

imiona.sort()
print("Posortowana lista:", imiona)

imiona.append("Andrzej")
imiona.append("Janek")
ostatnia_osoba = imiona.pop()
print("Lista po dodawaniu dwóch osób i użyciu pop:", imiona)
print("Pobrana ostatnia osoba:", ostatnia_osoba)

imiona.insert(3, "Ewa")
print("Lista po dodawaniu osoby na pozycji 3:", imiona)

imiona.reverse()
imiona *= 2
print("Lista po odwróceniu i zdublowaniu:", imiona)