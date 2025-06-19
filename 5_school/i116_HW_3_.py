# string part 1
s = 'JAIST'
print(s[0])
print(s[1])
try:
    print(s[5])
except IndexError as em:
    print(em)

s1 = 'Japn '
s2 = 'Advanced '
s3 = 'Institute '
s4 = 'of '
s5 = 'Science '
s6 = 'and '
s7 = 'Technology'
print(s1+s2+s3+s4+s5+s6+s7)

# string part 2
jaist = 'Japn '\
'Advanced '\
'Institute '\
'of '\
'Science '\
'and '\
'Technology'
print(jaist)
print('Japn\tAdvanced\tInstitute\tof\tScience\tand\tTechnology')
print('Japn Advanced Institute of \'Science\' and \'Technology\'')

# Tuples
aTuple = (0, 'zero', 0.0)
print(aTuple)
print((), ' is the empty tuple.')
print(('zero',), ' is the tuple that only consists of \'zero\'.')
print('(\'zero\') is not a tuple but a string, the same as \'zero\'.')
print('(\'zero\') == \'zero\' returns ', ('zero') == 'zero', '.')
print('(\'zero\',) == \'zero\' returns ', ('zero',) == 'zero', '.')
print(aTuple[0])
print(aTuple[1])
print(aTuple[-1])
print(aTuple[-2])

try:
    aTuple[2] = 1.41421356
except TypeError as em:
    print('If we try to do aTuple[2] = 1.41421356, the following message is written:')
    print(em)

try:
    aTuple[3]
except IndexError as em:
    print('If we try to do aTuple[3], the following message is written:')
    print(em)

aTuple = (aTuple[0], aTuple[1], 1.41421356)
print(aTuple)

# Lists
aList = [0,1,2,3,4]
print(aList)
print(aList[0])
print(aList[1])
print(aList[-1])
print(aList[-2])
aList[2] = 10
print(aList) # aList[2] = 10 changes aList.

try:
    aList[5]
except IndexError as em:
    print('If we try to do aList[5], the following message is written:')
    print(em)

# Lists part 2
print(aList[1:4])
print(aList[2:1])
print(aList[1:]) # deleting the top element
print(aList[:-1]) # deleting the bottom element
print(aList[100:])
print(aList[:-100])
print(aList) # aList[1:4] ... do not change aList.
print(aList[-100:100]) # seems strange but returns the list stored in aList
print(aList + aList)
print(aList) # + does not change aList.
print([-1] + aList)
print(aList + [5])

# Lists part 3
def qsort(lst):
    if len(lst) <= 1:
        return lst
    else:
        pair = partition(lst[0],lst[1:])
        return qsort(pair[0]) + [lst[0]] + qsort(pair[1])

def partition(pvt,lst):
    pair = ([], [])
    for e in lst:
        if e < pvt:
            pair = ([e] + pair[0], pair[1])
        else:
            pair = (pair[0], [e] + pair[1])
    return pair

lst = [4,7,5,1,0,3,6,2]
print('Input: ', lst)
print('Output: ', qsort(lst))

# Lists part 4
def msort(lst):
    if len(lst) <= 1:
        return lst
    else:
        pair = split(lst,[],[])
    return merge(msort(pair[0]),msort(pair[1]))

def split(lst,l1,l2):
    if len(lst) == 0:
        return (l1,l2)
    else:
        return split(lst[1:],l2,[lst[0]]+l1)

def merge(l1,l2):
    if len(l1) == 0:
        return l2
    elif len(l2) == 0:
        return l1
    else:
        if l1[0] < l2[0]:
            return [l1[0]] + merge(l1[1:],l2)
        else:
            return [l2[0]] + merge(l1,l2[1:])

lst = [4,7,5,1,0,3,6,2]
print('Input: ', lst)
print('Output: ', msort(lst))

# Dictionaries
aDict = {'x':1.41, 'y':3.14, 'z':1.73}
aDict2 = {'y':3.14, 'z':1.73, 'x':1.41}
print(aDict)
print(aDict2)
print(aDict, ' == ', aDict2, ' returns ', aDict == aDict2, '.')
print(aDict['x'])
print(aDict['z'])

try:
    print(aDict['a'])
except KeyError as em:
    print('If we do aDict[\'a\'], we have the follwing message:')
    print(em)

aDict['a'] = 2.71
print(aDict)
print(aDict['a'])
aDict['x'] = 2.23
print(aDict)

# Dictionaries part 2
aDict = {'x':1.41, 'y':3.14, 'z':1.73}
aDict2 = {'y':3.14, 'z':1.73, 'x':1.41}
print(aDict)
print(aDict2)
print(aDict, ' == ', aDict2, ' returns ', aDict == aDict2, '.')

x = 0
for k in aDict:
    x = x + 1
    if k == 'z':
        break
print('x = ', x)

x = 0
for k in aDict2:
    x = x + 1
    if k == 'z':
        break
print('x = ', x)

catalog ={'mp':('MacPro', 5000000), 'im':('iMac', 400000), 'mbp':('MacBookPro', 500000), 'am':('AirMac', 200000)}
cart = [('am', 4), ('mbp', 2), ('mp',1), ('am', 3), ('mp', 1)]

def normCart(c):
    tc = []
    flg = True
    for i in range(len(c)):
        for j in range(len(tc)):
            if (c[i])[0] == (tc[j])[0]:
                tc[j] = ((tc[j])[0], (c[i])[1] + (tc[j])[1])
                flg = False
            break
        if flg:
            tc = tc + [c[i]]
        flg = True
    return tc

print(normCart(cart))

def mkBillItemLst(cat,nc):
    bil = []
    for i in range(len(nc)):
        try:
            ip = cat[(nc[i])[0]]
            bil = bil + [(ip[0], (nc[i])[1], ip[1] * (nc[i])[1])]
        except KeyError:
            return []
    return bil

print(mkBillItemLst(catalog,normCart(cart)))

def mkBill(cat,c):
    bil = mkBillItemLst(cat,normCart(c))
    ttl = 0
    for bi in bil:
        ttl = ttl + bi[2]
    return (bil, ttl)

print(mkBill(catalog,cart))

def printBill(bll):
    bil = bll[0]
    ttl = bll[1]
    print('************** Billing **************')
    print('item ordered\t#items\tsub-total')
    for bi in bil:
        print(bi[0], '\t', bi[1], '\t', bi[2])
    print('*********** total amount ***********')
    print(ttl, ' Japanese Yen')

printBill(mkBill(catalog,cart))