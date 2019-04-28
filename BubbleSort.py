#Bubble Sort
def bSort(lst):
    for _ in range(len(lst)):
        for i in range(len(lst) - 1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
    return lst


print(bSort([6, 1, 3, 2, 5, 4]))
