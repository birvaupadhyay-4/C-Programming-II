lst = list(map(int, input("Enter list: ").split()))

def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


result = list(filter(lambda x: prime(x), lst))

print("Prime numbers:", result)
