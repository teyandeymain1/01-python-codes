import sys
#------------------整数のタプル-----------------------
def make_int_data_struct():
    readline = sys.stdin.readline
    return tuple(map(str, readline().split()))
            #↑この部分を list か set に変えることで list か set を作ることができる。
#=====================================================

inTuple1 = make_int_data_struct()
 #↑この部分を list か set に変えることで list か set を作ることができる。

if inTuple1[0] == "<" and inTuple1[1] == "<" and inTuple1[2] == "<":
    answerList = ["A", "B", "C"]
elif inTuple1[0] == "<" and inTuple1[1] == "<" and inTuple1[2] == ">":
    answerList = ["A", "C", "B"]
elif inTuple1[0] == ">" and inTuple1[1] == "<" and inTuple1[2] == "<":
    answerList = ["B", "A", "C"]
elif inTuple1[0] == ">" and inTuple1[1] == ">" and inTuple1[2] == "<":
    answerList = ["B", "C", "A"]
elif inTuple1[0] == "<" and inTuple1[1] == ">" and inTuple1[2] == ">":
    answerList = ["C", "A", "B"]
elif inTuple1[0] == ">" and inTuple1[1] == ">" and inTuple1[2] == ">":
    answerList = ["C", "B", "A"]
    
print(answerList[1])