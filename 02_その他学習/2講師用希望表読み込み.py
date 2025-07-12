from Classes import *
#=====================講師用=====================

RWCls = read_and_write_class(varCls.inTeacherWs)
matrixFromSheet = RWCls.read_sheet_make_matrix()
rsvCls.find_available_date(matrixFromSheet)

print("講師用希望日程表を読み込みました")