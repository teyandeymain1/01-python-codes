import numpy as np

num = int(input())

if num <= 10**3-1:
    print(int(num))
elif 10**3 <= num <= 10**4-1:
    print(int(np.floor(num / 10) * 10))
elif 10**4 <= num  <= 10**5-1:
    print(int(np.floor(num / 100) * 100))
elif 10**5 <= num <= 10**6-1:
    print(int(np.floor(num / 1000) * 1000))
elif 10**6 <= num <= 10**7-1:
    print(int(np.floor(num / 10000) * 10000))
elif 10**7 <= num <= 10**8-1:
    print(int(np.floor(num / 100000) * 100000))
elif 10**8 <= num <= 10**9-1:
    print(int(np.floor(num / 1000000) * 1000000))