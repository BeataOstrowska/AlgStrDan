#Przygotować funkcję, która przyjmie w parametrach pierwszą literę imienia, oraz nazwisko, a następnie zwróci te wartości połączone kropką. Przykładowe wyjście: J. Kowalski.
def funckja(a,b):
    return a+'.'+b
a=input('Podaj pierwsza litere swojego imienia: ')
b=input('Podaj swoje nazwisko: ')
print(funckja(a,b))
