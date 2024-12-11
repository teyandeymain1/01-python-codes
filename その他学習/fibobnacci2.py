#Observe the behavior of the recurrence function

def funcFibo(n):

    n = int(n)

    print("Call Fibonacci sequence " + str(n) + "th")

    if n < 0:
        print("Invalid")

    if n <= 1:
        print("Fibonacci sequence: " + str(n) + "th number is: " + str(n))
        return n
    else:
        resultF = funcFibo(n - 1) + funcFibo(n - 2)
        print(f"Fibonacci sequence→ {n}th number is: {resultF}")
        return resultF

v = input("Enter the number: ")

funcFibo(v)