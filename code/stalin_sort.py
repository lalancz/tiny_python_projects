import matplotlib.pyplot as plt

# eliminates all unordered items from list

def stalin_sort(input_list):
    if len(input_list) == 0:
        return input_list

    result = [input_list[0]]

    for i in input_list[1:]:
        if i >= result[-1]:
            result.append(i)
    
    return result

print(stalin_sort([5, 5, 4, 2, 6]))