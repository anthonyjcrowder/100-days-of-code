#Write your code below this row 👇
number = 0
for n in range (1,101):

     # print fizzbuzz if number mod 3 = 0 AND number mod 5 = 0
    if n % 3 == 0 and n % 5 == 0:
        print('FizzBuzz')

    # print fizz if number mod 3 = 0
    elif n % 3 == 0:
        print('Fizz')

    # print buzz if number mod 5 = 0
    elif n % 5 == 0:
        print('Buzz')

    else:
        print(n)