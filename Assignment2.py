# Function 1: Lists - Finding the Maximum and Second Maximum in a List
# This function takes a list of numbers as input and returns the maximum and second maximum values.
def max_two_in_list(numbers):
    if len(numbers) < 2:
        max_1 = max(numbers)
        max_2 = None

    else:
        remove_duplicates = set(numbers)
        my_list = list(remove_duplicates)
        max_1 = max(my_list)
        my_list.remove(max_1)
        max_2 = max(my_list)

    return (max_1, max_2)

# Function 2: Lists - Removing Duplicates and Sorting
# This function takes a list of numbers and returns a sorted list with duplicates removed.
def remove_duplicates_and_sort(numbers):
    cast_as_set = set(numbers)
    my_list = list(cast_as_set)

    return sorted(my_list)

# print(remove_duplicates_and_sort([10, 5, 5, 10, 2]))

# Function 3: Single-Dimensional Arrays - Cumulative Sum
# This function takes an array (list) of numbers and returns a new list where each element is the cumulative sum of the previous elements.
def cumulative_sum(arr):
    total = 0
    result = []

    for num in arr:
        total += num
        result = result + [total]
    
    return result

# print(cumulative_sum([1, 2, 3, 4]))


# Function 4: Two-Dimensional Arrays - Matrix Transpose
# This function takes a 2D list (matrix) and returns its transpose.
def transpose_matrix(matrix):
    rows_transpose = len([row[0] for row in matrix])
    columns_transpose = len(matrix[0])

    result = []

    for i in range(columns_transpose):
        new_row = []
        for j in range(rows_transpose):
            new_row += [matrix[j][i]]
        result = result + [new_row]

    return result

# print(transpose_matrix([[1, 2, 3], [4, 5, 6]]))

# Function 5: Slicing - Extracting Every Nth Element
# This function takes a list and a step value N and returns every Nth element.
def slice_every_nth(lst, step):
    slice = lst[::step]

    return slice

# print(slice_every_nth([1, 2, 3, 4, 5, 6], 2))

# Function 6: Arithmetic Operations with Arrays - Dot Product
# This function takes two lists of the same length and returns their dot product.
def dot_product(list1, list2):
    product_lists = [a * b for a, b in zip(list1, list2)]
    total_sum = sum(product_lists)
    
    return total_sum

# print(dot_product([1, 2, 3], [4, 5, 6]))

# Function 7: Arithmetic Operations with Arrays - Matrix Multiplication
# This function takes two 2D lists (matrices) and returns their matrix product.
def matrix_multiplication(matrix1, matrix2):

    rows_matrix1 = len(matrix1)
    columns_matrix1 = len(matrix1[0])
    columns_matrix2 = len(matrix2[0]) 

    result = []

    for i in range(rows_matrix1):
        new_row = []
        for j in range(columns_matrix2):
            sum_products = 0
            for k in range(columns_matrix1):
                sum_products = sum_products + matrix1[i][k] * matrix2[k][j]

            new_row = new_row + [sum_products]

        result = result + [new_row]
    
    return result

# print(matrix_multiplication([[1, 2], [3, 4]], [[5, 6], [7, 8]]))