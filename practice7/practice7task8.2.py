def swap(lst):
    lst[0],lst[len(lst)-1] = lst[len(lst)-1],lst[0]
    return lst
input("Enter length of array:")
list_new = list(map(int, (input("Enter array: ")).split()))
print(" ",list_new)
print("Swapped: ",swap(list_new))
