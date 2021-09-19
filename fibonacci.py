def fibonacci(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fibonacci(i-2) + fibonacci(i-1)
    for x in range(9):
         print(fibonacci(x))

num = int(input("Enter any number: "))
n1, n2 = 0, 1
sum = 0
if num <= 0:
     print('please enter number greater than 0')
else:
   for i in range(num):
    print(fibonacci(i))



