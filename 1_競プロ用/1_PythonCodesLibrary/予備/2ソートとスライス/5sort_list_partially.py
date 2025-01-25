import sys
#---------------リストをスライスしてソート----------------
def sort_list_partially(stSlice, enSlice, inList):
    #変数定義
    stSlice = stSlice - 1
    #
    sliceList = inList[stSlice:enSlice] #配列の一部をスライス
    sliceList = sorted(sliceList, reverse=True) #スライスした配列を降順でソート
    inList[stSlice:enSlice] = sliceList[0:len(sliceList)] #元の配列にソートした配列を代入
    return inList
#=====================================================

readline = sys.stdin.readline
length, stSlice, enSlice = map(int, readline().replace('\n','').replace('\r','').split())
                                                                                #空欄がないときは .split() を消す

#-------以下を問題に応じて書き換える。以下はAtCoderBeginnerContest356A_Subsegment Reverse用-----
inList2 = [i for i in range(1, (length+1))]
#------------------------ここまで-------------------------

inList2 = sort_list_partially(stSlice, enSlice, inList2)

print(*inList2)