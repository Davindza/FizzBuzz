print("Hi and welcome to FizzBuzz game!")

hey = input("Enter a number between 1 and 100: ")
hey = int(hey)

for num in range(1, hey+1):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)