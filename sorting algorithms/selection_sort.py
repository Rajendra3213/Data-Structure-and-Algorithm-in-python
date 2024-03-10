def selection_sort(lst):
   
    for i in range(len(lst)):
        
        # assume the first unsorted element is the minimum
        min_index = i
    
        # iterate over unsorted elements
        for j in range(i + 1, len(lst)):

            # find index of the smallest element
            # in the unsorted part of the list
            if lst[j] < lst[min_index]:
                min_index = j
    
        # swap the smallest element with the first element
        # of the unsorted part 
        lst[min_index], lst[i] = lst[i], lst[min_index]
    
    return lst


data = [18, 10, 8, 14, 1]
print(f'Unsorted List: {data}')

sorted_list = selection_sort(data)
print(f'Sorted List: {sorted_list}')