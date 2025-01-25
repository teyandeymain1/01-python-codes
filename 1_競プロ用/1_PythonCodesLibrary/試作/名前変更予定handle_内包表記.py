x = ["even" if i%2==0 else "odd" \
      for i in range(10)]
print(x)

xx = [i+j for i in list(range(5)) for j in list(range(5))]
print(xx)

xxx = [[i+j for i in range(3)] for j in range(5)]
print(xxx)

xxxx = [i+j for i,j in zip(list(range(5)), list(range(5)))]
print(xxxx)
