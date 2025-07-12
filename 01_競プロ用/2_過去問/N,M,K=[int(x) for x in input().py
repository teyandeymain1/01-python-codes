N,M,K=[int(x) for x in input().split()]
maru=set()
bastu=set()
for i in range(M):
  c,*A,r=[x for x in input().split()] #*Aは二つ目に入力された数字分、1から順に数字を挿入する。
  print("-" + c)
  print("--" + str(A))
  print("---" + r)

  a=0
  for x in A:
    a+=1<<(int(x)-1)    #右にint(x)-1、ビットシフト
    print("---x-" + str(x))
    print("----a-" + str(a))
  if r=="o":
    maru.add(a)
  else:
    bastu.add(a)

print("-" + str(maru))
print("-" + str(bastu))

ans=0

print("--" + str(1<<N))

for i in range(1<<N):
  f=True
  for a in bastu:
    print("---" + str(a))
    print("----" + str(i))       
    print("-----" + str(i&a))
    print("------b---" + str((i&a).bit_count()))
    if (i&a).bit_count()>=K:
        f=False
        break
  for a in maru:
    print("------m---" + str((i&a).bit_count()))
    if (i&a).bit_count()<K:
        
        f=False
        break
  if f:
    ans+=1
print(ans)