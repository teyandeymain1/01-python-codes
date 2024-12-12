#

def funcFibo(v):

    v = int()

    if v == 0:
        print("Fibonacci sequence first term is 1")
    elif v == 1:
        print("Fibonacci sequence second term is 1")
    else:
        resultF: int = funcFibo(v-1) + funcFibo(v-2)
        return resultF
    
    k = str(v)
    print("Fibonacci sequence:" + k + " term is " + resultF)

print("Enter the number:")
k:int = input()

funcFibo(k)