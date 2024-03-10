# function to divide the list into sublists 
def merge_sort(lst):

    # base condition:
    # recursion ends if the length of the list is 1 or less    
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2

    # get the left half of the list
    # and further divide it using recursion
    left_partition = merge_sort(lst[: mid])

    # get the right half of the list
    # and further divide it using recursion
    right_partition = merge_sort(lst[mid:])

    # call the merge() function 
    # combine list recursively
    return merge(left_partition, right_partition)

# function to sort and merge sublists (conquer phase)
def merge(left, right):

    output = []

    i = 0   
    j = 0 

    # merge elements in a sorted manner 
    # from left and right portions
    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1

    # append the remaining element
    output.extend(left[i:])
    output.extend(right[j:])
        
    return output
        
data = [6, 8, 1, 4, 5, 3, 7, 2]
print(f"Unsorted: {data}")

result = merge_sort(data)

print(f"Sorted: {result}")