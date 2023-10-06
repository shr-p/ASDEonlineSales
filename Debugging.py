def compute(n):
    if n < 10:
        out = n ** 2
    elif n <= 20: # to include 20
        out = 1
        for i in range(1, n-9): # to fix the range
            out *= i
    else:
        lim = n - 20
        out = lim * lim
        out = out + lim # sign change
        out = out / 2 
    print(out)


n = int(input("Enter an integer: "))
compute(n)