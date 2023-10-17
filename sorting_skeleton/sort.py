# Szymon Turkiewicz, 414461
from typing import List
#import copy
def quicksort_on_copy(l2:List[int],start:int, end:int, pivot:int=None)-> None:
        #w takim przypadku l2 (prawdopodobnie) będzie kopią l1 którą otrzyma od funkcji quicksort, 
        #najlepszą opcją było by stworzenie dwóch osobych funkcji(by można z nich było korzystać zależnie od sytuacji) z których jedna polega na drugiej,
        # ale uznałem to za zbędne i niezgodne z tym jak wyglądał szkielet zadania
    if pivot is None:
        
        if l2[start] >= l2[end] and l2[start] > l2[(start + end) // 2]:
            pivot = l2[start]
        elif l2[end] >= l2[start] and l2[end] > l2[(start + end) // 2]:
            pivot = l2[end]
        else:
            pivot = l2[(start + end) // 2]
#
    i = start
    j = end
    while i <= j:
        while l2[i] < pivot:
            i += 1
        while l2[j] > pivot:
            j -= 1
        if i <= j:
            l2[i], l2[j] = l2[j], l2[i]
            i += 1
            j -= 1

    if start < j:
        l2=quicksort_on_copy(l2, start, j)
    if i < end:
        l2= quicksort_on_copy(l2, i, end)
    return l2


def quicksort(l1)-> List[int]:
    sorted_copy = l1.copy()
    sorted_copy = quicksort_on_copy(sorted_copy,0,len(l1)-1,None)
    return sorted_copy


test_list=[1,7,8,9,3,2,6,13,5,165,64,5,45,65,63,64,65]
sorted_by_quicksort = quicksort(test_list)
print(test_list)
print(sorted_by_quicksort)

def bubblesort() -> None:
    pass
