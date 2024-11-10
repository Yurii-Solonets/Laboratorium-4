zdanie = input("Podaj zdanie: ")

alfabet = set("aąbcćdeęfghijklłmnńoóprsśtuvwxyzźż")

litery_w_zdaniu = {litera for litera in zdanie.lower() if litera if alfabet}

litery_obecne = sorted(litery_w_zdaniu)

brakujące_litery = sorted(alfabet - litery_w_zdaniu)

print("Litery w zdaniu (w kolejności alfabetycznej):", "".join(litery_obecne))
print("Litery, których nie ma w zdaniu:", "".join(brakujące_litery))