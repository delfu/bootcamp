print ("Week 1 Assignment - Math Equation Evaluator")
print ("Intern - Shu Wei")
print ("")

eArray = list(map(str, input("Please enter your input with spaces between them: ").split()))

#Definitions
aCount = (len(eArray))
fCount = 3
nCount = 4
needle = 0

# Check whether the first two inputs are numbers and the last input is a sign
try:
    check1 = int(eArray[0])
except ValueError:
    print("Please make sure that the input #1 is a number")
    exit()
try:
    check2 = int(eArray[1])
except ValueError:
    print("Please make sure that the input #2 input is a number")
    exit()

if aCount > 3:
    CheckNCount = 4
    while (CheckNCount <= aCount):
        try:
            checkN = int(eArray[CheckNCount-1])
        except ValueError:
            print ("Please make sure that the input #", CheckNCount, "is a number")
            exit()
        CheckNCount = CheckNCount + 2
else:
    pass

if aCount >= 3:
    CheckSCount = 3
    while (CheckSCount <= aCount):
        try:
            checkS = int(eArray[CheckSCount-1])
        except ValueError:
            if eArray[CheckSCount-1] == "+" or eArray[CheckSCount-1] == "-" or eArray[CheckSCount-1] == "*" or eArray[CheckSCount-1] == "/":
                pass
            else:
                print("Invalid input #", CheckSCount)
        else:
            print ("Please make sure that the input #", CheckSCount, "is a sign")
            exit ()
        CheckSCount = CheckSCount + 2
else:
    pass

#try:
#    check3 = int(eArray[aCount-1])
#except ValueError:
#    if eArray[aCount-1] == "+" or eArray[aCount-1] == "-" or eArray[aCount-1] == "*" or eArray[aCount-1] == "/":
#        pass
#    else:
#        print("Invalid last sign")
#else:
#    print("Please make sure that the last input is a sign")
#    exit()

# Calculation
import operator
ops = {
    "+" : operator.add,
    "-" : operator.sub,
    "*" : operator.mul,
    "/" : operator.truediv,
}

result1 = ops[eArray[fCount-1]](int(eArray[0]), int(eArray[1]))
if aCount > 4:
    while (fCount < aCount):
        fCount = fCount + 2
        result1 = ops[eArray[fCount-1]](result1, int(eArray[nCount-1]))
        nCount = nCount + 2
    print (result1)
else:
    print (result1)
    
