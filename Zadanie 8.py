stopnie = ("Szeregowy", "Kapral", "Sierżancie", "Porucznik", "Kapitan", "Major", "Pułkownik")

ilość_stopnii = len(stopnie)
major_index = stopnie.index('Major')
Pułkownik_wstepowanie = "Pułkownik" in stopnie

print("Liczba stopnii wojskowych:", ilość_stopnii)
print("Indeks stopnia Majora:", major_index)
print("Czy 'Pułkownik znajduje się w krotce?:",  Pułkownik_wstepowanie)