def counting_sort(lst):

   # if list is empty or has one element, return itself 
    if len(lst) <= 1:
        return lst
    
    # find the largest element
    # and create the counting list
    max_element = max(lst)
    counting_list = [0] * (max_element + 1)
    
    # fill the counting list with frequency of each number
    for num in lst:
        counting_list[num] += 1
    
    # create the sorted output list   
    sorted_output = []
    for index, value in enumerate(counting_list):
        sorted_output.extend([index] * value)

    return sorted_output

input_list = [5, 8, 4, 9, 7, 10, 3, 5, 4, 9]
print(f'Unsorted List: {input_list}')

sorted_list = counting_sort(input_list)
print(f'Sorted List: {sorted_list}')