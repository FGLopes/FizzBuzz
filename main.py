print("Welcome to FizzBuzz!")

game = input("Select a number between 1 and 100: ")

for number in range(1, 31):

    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")

    elif number % 3 == 0:
        print("fizz")

    elif number % 5 == 0:
        print("buzz")

    else:
        print(number)
