import math
x = int(input("Enter a number: "))
i = 1
sqrt_x = math.sqrt(x)
factors = []
primeFactors = []

print("--------------------")

while i <= x:
    if x % i == 0:
        #print(i, "is a factor of", x, "(", i, "x", int(x / i), "=", int(i * (x / i)), ")")
        factors.append(i)
        #isPrime = False
    i += 1

if len(factors) == 2:
    print(x, "is a prime number.")
else:
    print("The factors of", x, "are:")
    print(factors)

