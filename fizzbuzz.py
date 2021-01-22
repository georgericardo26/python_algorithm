# for fizzbuzz in range(51):
#     if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
#         print("fizzbuzz")
#         continue
#     elif fizzbuzz % 3 == 0:
#         print("fizz")
#         continue
#     elif fizzbuzz % 5 == 0:
#         print("buzz")
#         continue
#     print(fizzbuzz)

def fizzbuzz(n):
    # for y in range(n):
    #     if y % 3 == 0 and y % 5 == 0:
    #         print("Fizz Buzz")
    #     elif y % 5 == 0:
    #         print("Buzz")
    #     elif y % 3 == 0:
    #         print("Fizz")
    #     else:
    #         print(y)

    for n in range(1, n+1):
        # if n % 2 == 0:
        #     print("Fizz")
        #     continue
        # if n % 5 == 0:
        #     print("Buzz")
        #     continue
        # print(str(n))

        if n % 3 == 0 and n % 5 == 0:
            print('FizzBuzz')
        elif n % 3 == 0:
            print('Fizz')
        elif n % 5 == 0:
            print('Buzz')
        else:
            print(str(n))

fizzbuzz(15)
