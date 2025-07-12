from Classes import *
#=====================生徒用=====================

RWCls = read_and_write_class(varCls.inStudentWs)
matrixFromSheet = RWCls.read_sheet_make_matrix()

print("生徒用希望日程表を読み込みました")