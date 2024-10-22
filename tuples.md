# Tuples in Python


## Fakten
- Tuple sind immutable, also unveränderbar  
- Tuple können aber mutable objects enthalten (z.B. Listen)  
- Tuple sind indizierbar [0], auch negativ [-1] und slicable [start:end]  
- Tuple können unterschiedliche Datentypen enthalten  
- Tuple erlauben doppelte Einträge


## Tuple Funktionen
- tuple(): Konstruktor 
- len(): Bestimmt die Länge des Tuples (Anzal der Elemente)
- count(): Zählt, wie oft ein Element im Tuple enthalten ist  
- index(): Gibt den Index für das gesuchte Element zurück


## Tuple erstellen
Variante 1: Konstruktor tuple()  
```python
my_tuple = tuple("apple", "banana")
```
Variante 2: 
```python
my_tuple = ("apple", "banana")
```
> Wichtig bei Tuples mit nur einem Wert MUSS ein Komma folgen:
```python
my_tuple = ("apple",)
```


<p style="page-break-after: always;">


## Tuple verändern
Auch wenn Tuple immutable, also unveränderbar sind, gibt es Workarounds:  

1. Um Werte zu verändern:  
 Dafür wandelt man mit Hilfe der list() Funktion das Tuple in eine Liste, ändert den gewünschten Wert und wandelt dann mit Hilfe der tuple() Funktion die Liste zurück in ein Tuple.

```python
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
```

2. Um Werte hinzuzufügen:  
Hierfür gibt es 2 Möglichkeiten. Entweder wie unter 1. das Tuple in eine Liste und zurück wandeln.  
Oder alternativ kann man Tuple zu Tuple hinzufügen:

```python
this_tuple = ("apple", "banana", "cherry")
y = ("orange",)
this_tuple += y
```

3. Um Werte zu löschen:  
Hier bleibt nur die unter 1. genannte Möglichkeit.


## Packing und Unpacking
Das Erstellen von Tuple nennt man "Packing"
```python
fruits = ("apple", "banana", "cherry")
```

Durch "Unpacking" kann man die Werte im Tuple einzelnen Variablen zuweisen
```python
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
```

Durch Nutzung des Sterns * kann man mehrere Werte einer Variablen als Liste zufügen
```python
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
```


## Über Tuple iterieren
1. For-Schleife
```python
this_tuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)
```

2. For-Schleife mit Index
```python
this_tuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
```


## Tuple zusammenfügen
Wenn man 2 Tuple zusammenfügen möchte, kann man diese eine durch ein "+" konkatenieren
```python
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
```


## Good to know
Multiple return Werte werden in Python standardmäßig als Tuple zurückgegeben  
```python
def example_function():
    return value1, value2
```


> Quellen:  
>https://docs.python.org/3/tutorial/datastructures.html  
>https://www.w3schools.com/python/python_tuples.asp  
