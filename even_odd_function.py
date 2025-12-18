#program to check even or odd numbers using a function

def check(numbers):
   for num in numbers:
     if num % 2 == 0:
        print(num,"is even")
     else:
        print(num,"is odd")
numbers = [1,2,3,4,5,6]
check(numbers)
