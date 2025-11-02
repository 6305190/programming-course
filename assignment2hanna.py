 #Question 1: Lists - removing duplicates and sorting
def remove_duplicates_and_sort(numbers):
    return sorted(list(set(numbers)))    #return sorted list without duplicates

numbers = [3, 6, 4, 3, 5]

print(remove_duplicates_and_sort(numbers))   

#Question 2: Single-Dimensional Arrays - Cummulative sum 
def cummulative_sum(numbers):
    result = []       #create an empty list to store the cummulative sums
    total = 0         #start total at zero
    for num in numbers:
        total += num      #add the number to the total
        result.append(total)   #add the new total to the list
    return result

numbers = [1, 2, 3, 4, 5]
print(cummulative_sum(numbers))

 #Question 3: Slicing - extracting Every Nth Element:
def extract_every_nth(numbers, n):
    result = numbers[n-1::n]   #take every nth number from the list
    return result  #returrn the new list containing only the selected elements

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n= int(input("Enter the value of n"))
print(extract_every_nth(numbers, n))

#Questiom 4: Arithmetic Operations with Arrays - Dot product:
def dot_product(list1, list2):
    total = 0     #start total at zero
    for i in range(len(list1)):  #go through each position in the list
        total += list1[i]*list2[i]   #multiply matching numbers and add to the total
    return total 

list1 = [2, 3, 4]
list2 = [3, 4, 5]

print(dot_product(list1, list2))

#Question 5: Arithmetic operations with Arrays - Matrix multiplication
def matrix_multiply(A, B):
    result = []  #start with an empty list for the final matrix
    for i in range(len(A)):   #go through each row of A 
        row = []            #make a new row for the result
        for j in range(len(B[0])):    #go through each row of B
            total = 0
            for k in range(len(B)):   #multiply and add all matching elements
                 total += A[i][k] * B[k][j]
            row.append(total)   #add total to the row
        result.append(row)    #add row to the result matrix
    return result            #return the final matrix

A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8],
    [9,10],
    [11, 12]
]

print(matrix_multiply(A, B))

