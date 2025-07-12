import sys
#------------------整数のリスト-----------------------
def make_int_data_struct():
    readline = sys.stdin.readline
    return tuple(map(int, readline().replace('\n','').replace('\r','')))
                                                                    #空欄があるときは .split() をつける
            #↑この部分を list か set に変えることで list か set を作ることができる。
#-----------------------------------------------------------------
def make_dict():
    return dict(enumerate(make_int_data_struct()))
#=====================================================

print(make_dict())
