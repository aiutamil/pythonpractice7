def findMax(lst):
    return max(lst)


arr = input("Enter array: ")
list1 = list(map(int, arr.split()))
print("Maximum of list1:", findMax(list1))

arr = input("Enter array: ")
list2 = list(map(int, arr.split()))
print("Maximum of list2:", findMax(list2))

index1 = list1.index(findMax(list1))
index2 = list2.index(findMax(list2))

list1[index1], list2[index2] = list2[index2], list1[index1]

print(list1, list2)
