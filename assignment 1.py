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




