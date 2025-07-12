def fibonacci_dynamic_programming(n):
    if n <= 0:
        return "引数は正の整数である必要があります"
    
    fib_sequence = [0, 1]

    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])

    return fib_sequence

# 例: 最初の10個のフィボナッチ数を表示
n = input("Enter the number: ")
n = int(n)
result = fibonacci_dynamic_programming(n)
print(result)
