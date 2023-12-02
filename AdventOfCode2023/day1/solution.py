    
def calibrationValuePart1(group):
    f = ''.join(filter(str.isdigit, group))
    print(f)
    last_digit = int(str(f)[-1])
    first_digit = int(str(f)[0])
    res = int(f)
    print("last ", last_digit)
    print("first ", first_digit)
    res =  int(''.join([str(first_digit), str(last_digit)]))
    print("res ", res)
    return res

def calibrationValuePart2(calibrationValue):
    REPLACEMENTS = [
        ("one", "one1one"),
        ("two", "two2two"),
        ("three", "three3three"),
        ("four", "four4four"),
        ("five", "five5five"),
        ("six", "six6six"),
        ("seven", "seven7seven"),
        ("eight", "eight8eight"),
        ("nine", "nine9nine")
    ]
    for old, new in REPLACEMENTS:
        calibrationValue = calibrationValue.replace(old, new)
    
    print("part2",  calibrationValue)
    
    return calibrationValuePart1(calibrationValue)

def sumOfAllCallibrationValuesPart1():
    with open("sampleinput") as f:
        data = f.read().strip()
        calibrationDocument = data.split("\n")
    print("input", calibrationDocument)
    sumOfAllCalibrationValues = sum(calibrationValuePart1(calibrationValue) for calibrationValue in calibrationDocument)
    return sumOfAllCalibrationValues

def sumOfAllCalibrationValuesPart2():
    with open("input") as f:
        data = f.read().strip()
        calibrationDocument = data.split("\n")
    print("input", calibrationDocument)
    sumOfAllCalibrationValues = sum(calibrationValuePart2(calibrationValue) for calibrationValue in calibrationDocument)
    return sumOfAllCalibrationValues

# Part 1
print(sumOfAllCallibrationValuesPart1())

# Part 2
print(sumOfAllCalibrationValuesPart2())
