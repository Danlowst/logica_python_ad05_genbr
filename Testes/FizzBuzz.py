num = int(input("Digite um número: "))

# if num % 15 == 0:
#     print("FizzBuzz")
# elif num % 3 == 0:
#     print("Fizz")
# elif num % 5 ==0 :
#     print("Buzz")
# else:
#     print(num)

if num % 3 == 0:
    print("FizzBuzz" if num % 5 == 0 else "Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)

#print("FizzBuzz" if num % 15 == 0 else "Fizz" if num % 3 == 0 else "Buzz" if num % 5 == 0 else num)

