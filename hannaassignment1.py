#Question 1 using pythons built in function
a = input ("Enter a")    #ask the user to input numbers
b = input ("Enter b")
c = input ("Enter c")
numbers = [a,b,c]          #store all built in functions in a list
max_value = max(numbers)    #use built in function max () to get the largest value

print(max_value)   #calling the function 

#Question 2 using pythons built in function
a = input ("Enter a")    #ask the user to input numbers
b = input ("Enter b")
c = input ("Enter c")
numbers = [a,b,c]  #store all built in functions in a list
min_value = min(numbers)   #use built in function (min) to get the smallest value

print(min_value)   #calling the function

 #Question 3 using the if statement:
def identify_number_type(num_type): 
 #check if number is positive, negative or equal to zero
    if num_type > 0:
       return "the number is positive"
    elif num_type <0:
       return"The number is negative"
    else:
        return "the number is zero"
   

num_type = int(input("identify num type"))    #converting input to integer

print (identify_number_type(num_type))  #calling the function


#Question 4 for loop
def star_shape(rows): 
    
    for i in range(1,rows+1):   #repeat from 1 to number of rows
        print("*" * i)
    
    
rows = int(input("Enter number of rows: "))   #converting input to integer 
star_shape(rows)   #calling the function

#Question 5 while loop

def multiple_of_3(limit) :

    num = 1  #start counting from 1

    while num <= limit :
        if num % 3 == 0 :        #check if the number is divisible by 3
            print('Multiple of 3')
        else:
            print(num)
        num = num + 1    #increase number by 1 each time

limit = int(input('Enter the limit: '))

multiple_of_3(limit)  #calling the function


#Question 6 Sum of even numbers in a range

def sum_even_numbers(start, end):

    sum = 0   #initialize the total sum to 0

    for num in range(start, end + 1) :
        if num % 2 == 0 :  #check if the number is divisible by 2
            sum = sum + num  #add the even number to the total 
    return sum

start = int(input('Enter a start value: '))  #getting the start of the range
end = int(input("Enter an end value: "))    #getting the end of the range 

print(sum_even_numbers(start, end))  #calling the function