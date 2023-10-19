import sort
import random
import timeit

dane1=list(range(0,1000))
dane2= list(range(1000,0,-1))
dane3=[1]*1000
dane4= random.sample(range(0,1000),1000)

t1_buble = timeit.timeit("sort.bubblesort(dane1)", number=1000, globals=globals())/1000
print("Średni czas wykonania bubblesort na posortowanej liscie: ")
print(t1_buble)
t2_buble = timeit.timeit("sort.bubblesort(dane2)", number=1000, globals=globals())/1000
print("Średni czas wykonania bubblesort na odwrotnie posortowanej liscie: ")
print(t2_buble)
t3_buble = timeit.timeit("sort.bubblesort(dane3)", number=1000, globals=globals())/1000
print("Średni czas wykonania bubblesort na liscie tych samych elementów: ")
print(t3_buble)
t4_buble = timeit.timeit("sort.bubblesort(dane4)", number=1000, globals=globals())/1000
print("Średni czas wykonania bubblesort na liscie losowych elementów: ")
print(t4_buble)

t1_quick = timeit.timeit("sort.quicksort(dane1)", globals=globals(), number=1000)/1000
print("Średni czas wykonania quickksort na posortowanej liscie: ")
print(t1_quick)
t2_quick = timeit.timeit("sort.quicksort(dane2)", number=1000, globals=globals())/1000
print("Średni czas wykonania quickksort na odwrotnie posortowanej liscie: ")
print(t2_quick)
t3_quick = timeit.timeit("sort.quicksort(dane3)", number=1000, globals=globals())/1000
print("Średni czas wykonania quickksort na liscie tych samych elementów: ")
print(t3_quick)
t4_quick = timeit.timeit("sort.quicksort(dane4)", number=1000, globals=globals())/1000
print("Średni czas wykonania quickksort na liscie losowych elementów: ")
print(t4_quick)

#dla quicksort przypadek oczekiwany i optymistyczny to 3 000, a pesymistyczny to 1 000 000
#dla bubblesort przypadek  optymistyczny to 1 000, a pesymistyczny i oczekiwany to 1 000 000
#jednak przy mojej implementacji (pivot to środkowy element) często przypadki są bardziej optymistyczne a nie pesymistyczne
# by zbadać złożoność czasową przy przypadku pesymistycznym należało by stworzyć taką funkkcję quicksort,
# która wybierała by pierwszy lub ostatni element jako pivot