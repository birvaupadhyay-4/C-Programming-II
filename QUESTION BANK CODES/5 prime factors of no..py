def prime_factors(n):
    i = 2
    print("Prime factors:", end=" ")

    while n > 1:
        if n % i == 0:
            print(i, end=" ")
            n = n // i
            i=i+1
        else:
            i += 1       

num = int(input("Enter number: "))
prime_factors(num)
