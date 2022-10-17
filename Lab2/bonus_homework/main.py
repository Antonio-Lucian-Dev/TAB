# Sa se afiseze index-ul elementului cautat in Array, chiar daca acesta apare de mai multe ori.
# Date de intrare: 1, 2, 2, 3, 4, 5, 2
# Date de iesire: 1, 2, 6
# Punctul il obtine prima persoana care incarca codul in Assigment. Asta nu trebuie sa va impiedice sa incarcati codul.

def find(array, size, search, rezultat):
    gasit = 0
    for i in range(size):
        if array[i] == search:
            rezultat.append(i)
            gasit=1
    if gasit == 0:
        print("Valoarea ", search, " nu a fost gasita.")
    return -1

data = [1 , 2 , 2, 3, 4, 5, 2]
length = len(data)
value = 2
result=[]
find(data, length, value, result)
delim = ","
temp = list(map(str, result))
res = delim.join(temp)
print(str(res))
