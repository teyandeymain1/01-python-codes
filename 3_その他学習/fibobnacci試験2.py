def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# テスト
n = 10  # 計算したいフィボナッチ数列の項目数
result = fibonacci_recursive(n)
print(f"The {n}-th Fibonacci number is: {result}")
