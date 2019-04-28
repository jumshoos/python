import random


def quick_Sort(lst):
    print(lst)

    def leftp(p, l, r):
        for i in range(r, l-1, -1):
            if lst[p] > lst[i]:
                lst[p], lst[i] = lst[i], lst[p]
                rightp(r, l, r)
        if r != l:
            rightp(r, l+1, r)

    def rightp(p, l, r):
        for j in range(l, r+1, 1):
            if lst[p] < lst[j]:
                lst[p], lst[j] = lst[j], lst[p]
                leftp(j, j, r)
        if r != l:
            leftp(l, l, r-1)

    leftp(0, 0, len(lst)-1)
    return lst

# creating test data
list1 = []
for _ in range(10):
    list1.append(random.randrange(1, 100))


print(quick_Sort(list1))
