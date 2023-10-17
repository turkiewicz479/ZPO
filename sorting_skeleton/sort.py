# Szymon Turkiewicz, 414461
from typing import List, Tuple
#import copy



def quicksort(l1)-> List[int]:
    def quicksort_on_copy(l2:List[int],start:int, end:int, pivot:int=None)-> None:
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
    sorted_copy = l1.copy()
    sorted_copy = quicksort_on_copy(sorted_copy,0,len(l1)-1,None)
    return sorted_copy


test_list=[1,7,8,9,3,2,6,13,5,165,64,5,45,65,63,64,65]
sorted_by_quicksort = quicksort(test_list)
print(test_list)
print(sorted_by_quicksort)


def bubblesort(l1:list[int]) -> Tuple[List[int], int]:
    n= len(l1)
    l2=l1.copy()
    count=0
    iterations=0
    while n>1:
        count_before=count
        for i in range(1,n):
            if l2[i-1]>l2[i]:
                temp=l2[i-1]
                l2[i-1]=l2[i]
                l2[i]= temp
                count+=1
        iterations+=1
        n-=1
        if count==count_before:
            return (l2,iterations)
        #nie jestem pewny czy rozumieć ilość posortowań jako ilość "przejść" przez liste czy ilość łącznych zamian dwóch elementów ale wystarczy zamienić iterations na count
        # i uzyka się tą drugą wersję
    pass

sorted_by_bublesort=bubblesort(test_list) 
print(test_list)
print(sorted_by_bublesort)
