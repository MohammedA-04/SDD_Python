# Activty 4A | So get the Fibonacci 0-50
# FibSeq = [0,1,1,2,3,4,8,13,21,34]

FibSeq0 = 0
FibSeq1 = 1


while FibSeq0<50:
    print(FibSeq1)
    FibSeq0, FibSeq1 = FibSeq1,FibSeq0 + FibSeq1
   # FibSeq0,FibSeq1 = FibSeq1,FibSeq0 + FibSeq1
    if FibSeq1>50:
        break

