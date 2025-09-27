#Question 1 using pythons built in function
a = input ("Enter a")
b = input ("Enter b")
c = input ("Enter c")
numbers = [a,b,c]
max_value = max(numbers)

print(max_value)

#Question 2 using pythons built in function
a = input ("Enter a")
b = input ("Enter b")
c = input ("Enter c")
numbers = [a,b,c]
min_value = min(numbers)

print(min_value)

 #Question 3 using the if statement:
def identify_number_type(num_type):

    if num_type > 0:
       return "the number is positive"
    elif num_type <0:
       return"The number is negative"
    else:
        return "the number is zero"
   

num_type = int(input("identify num type"))

print (identify_number_type(num_type))


#Question 4 for loop
def star_shape(rows): 
    
    for i in range(1,rows+1):
        print("*" * i)
    
    
rows = int(input("Enter number of rows: "))
star_shape(rows)

#Question 5 while loop

def multiple_of_3(limit) :

    num = 1

    while num <= limit :
        if num % 3 == 0 :
            print('Multiple of 3')
        else:
            print(num)
        num = num + 1

limit = int(input('Enter the limit: '))

multiple_of_3(limit)


#Question 6 Sum of even numbers in a range

def sum_even_numbers(start, end):

    sum = 0

    for num in range(start, end + 1) :
        if num % 2 == 0 :
            sum = sum + num
    return sum

start = int(input('Enter a start value: '))
end = int(input("Enter an end value: "))

print(sum_even_numbers(start, end))