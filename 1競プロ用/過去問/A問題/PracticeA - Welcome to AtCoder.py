#----------------------------------------------
def InputFunc():
    int_list = list(map(int, input().split()))
    return int_list
#------------------------------------------------

num1 = int(input())

num_list1 = InputFunc()

str_low1 = str(input())

sum_num1 = num1 + sum(num_list1)

print(str(sum_num1) + " " + str_low1)

#format()メソッドを用いた解答例
print("{} {}".format(num1 + sum(num_list1), str_low1))