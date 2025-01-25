import sys

readline = sys.stdin.readline
inList1 = list(map(str, readline().replace('\n','').replace('\r','')))
                                                                    #空欄があるときは .split() をつける
          #↑この部分を list か set に変えることで list か set を作ることができる。

#------------以下はAtCoder ABC360-B-Vertical Reading用---------
for i, item in enumerate(inList1):

    print(i-1, "個おきにリストの要素を表示、-1個おきは無いので表示無し")

    for j in range(i):
        print("文字列のスタート位置=", j)
        print(inList1[j::i]) #i個おきにリストの要素を表示、ただの文字列でも同じ操作ができる。

#----------以下はAtCoder ABC066-B-ss用---------

inList2 = inList1

print(" ")

print("リストの前半部")
print(inList2[:(len(inList2)//2)])

print("リストの後半部")
print(inList2[(len(inList2)//2):])

print("反転")
print(inList1[::-1])

print("後ろから2つ")
print(inList1[-2:])

print("2番目以降1個飛ばし")
print(inList1[1::2])


import sys
#------------------リストの回転-----------------------
def rotate_list(st, inTuple):
    #変数定義
    from collections import deque
    #dequeの利用
    inDeque = deque(inTuple)
    inDeque.rotate(st) #右回転は+、左回転は-の符号をつける
    return list(inDeque)
#=====================================================
readline = sys.stdin.readline
st, = map(int, readline().replace('\n','').replace('\r',''))
                                                        #空欄があるときは .split() をつける
inTuple1 = tuple(map(int, readline().replace('\n','').replace('\r','')))
                                                                    #空欄があるときは .split() をつける
            #↑この部分を list か set に変えることで list か set を作ることができる。
answerList = rotate_list(st, inTuple1)

print(answerList)