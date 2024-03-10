def quick_sort(lst):
    length = len(lst)
    
    if length <= 1:
        return lst     
    else:
        pivot = lst.pop()

    right = []
    left = []

    for element in lst:
       
        if element > pivot:
            right.append(element)        
        else:
            left.append(element)

    return quick_sort(left) + [pivot] + quick_sort(right)

list1 = [7, 2, 1, 6, 8, 5, 3, 4]
print(f"Unsorted List: {list1}")

sorted_list = quick_sort(list1)
print(f"Sorted List: {sorted_list}")