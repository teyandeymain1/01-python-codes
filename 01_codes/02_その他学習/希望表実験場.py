from Classes import *
#=====================講師用=====================

string  = "講師用/希望/日程表/を/初期化/しました"
bufList = list(string.split("/"))
bufList.append("ヤッホー")
print(bufList[:-1])

bufString = "/".join(bufList) #文字列として結合して代入
print(bufString)

bufList = ["N"]
bufList = bufList[:-1]
print(len(bufList))