#Qidirish algoritmlari

#Linear search

myList = [1,3,4,6,7,8,10,12,23,45,56,78,99]
#
# def linear_search(list, item):
#     for n in range(len(list)):
#         if list[n]==item:
#             return n
#     return None
#
# print(linear_search(myList, 12))

#Binary search

def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low+high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high= mid - 1
        else:
            low= mid + 1
    return None

print(binary_search(myList, 78))
