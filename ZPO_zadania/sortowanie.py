def quciksort(L1:list, start:int,end:int, pivot: int=None):
    if pivot is None:
        pivot= L1[(start+end)/2]
    