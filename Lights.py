X = [255, 0, 0]  # Red
O = [255, 255, 255]  # White

digitOne = ""
digitTwo = ""

ledArray = []


class Numbers:
    zero = [
        0, 0, 0, 0,
        0, 0, 0, 0,
        0, 0, 0, 0,
        0, 1, 1, 1,
        0, 1, 0, 1,
        0, 1, 0, 1,
        0, 1, 0, 1,
        0, 1, 1, 1,
    ]
    one = [
        0, 0, 0, 0,
        0, 0, 0, 0,
        0, 0, 0, 0,
        0, 0, 1, 0,
        0, 1, 1, 0,
        0, 0, 1, 0,
        0, 0, 1, 0,
        0, 1, 1, 1,
    ]
    two = [
        0, 0, 0, 0,
        0, 0, 0, 0,
        0, 0, 0, 0,
        0, 1, 1, 1,
        0, 0, 0, 1,
        0, 1, 1, 1,
        0, 1, 0, 0,
        0, 1, 1, 1,
    ]
    three = [
        0, 0, 0, 0,
        0, 0, 0, 0,
        0, 0, 0, 0,
        0, 1, 1, 1,
        0, 0, 0, 1,
        0, 0, 1, 1,
        0, 0, 0, 1,
        0, 1, 1, 1,
    ]
    four = [
        0, 0, 0, 0,
        0, 0, 0, 0,
        0, 0, 0, 0,
        0, 1, 0, 1,
        0, 1, 0, 1,
        0, 1, 1, 1,
        0, 0, 0, 1,
        0, 0, 0, 1,
    ]
    five = [
        0, 0, 0, 0,
        0, 0, 0, 0,
        0, 0, 0, 0,
        0, 1, 1, 1,
        0, 1, 0, 0,
        0, 1, 1, 1,
        0, 0, 0, 1,
        0, 1, 1, 1,
    ]
    six = [
        0, 0, 0, 0,
        0, 0, 0, 0,
        0, 0, 0, 0,
        0, 1, 1, 1,
        0, 1, 0, 0,
        0, 1, 1, 1,
        0, 1, 0, 1,
        0, 1, 1, 1,
    ]
    seven = [
        0, 0, 0, 0,
        0, 0, 0, 0,
        0, 0, 0, 0,
        0, 1, 1, 1,
        0, 0, 0, 1,
        0, 0, 1, 1,
        0, 1, 1, 0,
        0, 1, 0, 0,
    ]
    eight = [
        0, 0, 0, 0,
        0, 0, 0, 0,
        0, 0, 0, 0,
        0, 1, 1, 1,
        0, 1, 0, 1,
        0, 1, 1, 1,
        0, 1, 0, 1,
        0, 1, 1, 1,
    ]
    nine = {
        0, 0, 0, 0,
        0, 0, 0, 0,
        0, 0, 0, 0,
        0, 1, 1, 1,
        0, 1, 0, 1,
        0, 1, 1, 1,
        0, 0, 0, 1,
        0, 0, 0, 1,
    }

def determineEnglishDigit(number, digit):
    num = str(int(number))
    if num[digit] == "0":
        return Numbers.zero
    elif num[digit] == "1":
        return Numbers.one
    elif num[digit] == "2":
        return Numbers.two
    elif num[digit] == "3":
        return Numbers.three
    elif num[digit] == "4":
        return Numbers.four
    elif num[digit] == "5":
        return Numbers.five
    elif num[digit] == "6":
        return Numbers.six
    elif num[digit] == "7":
        return Numbers.seven
    elif num[digit] == "8":
        return Numbers.eight
    elif num[digit] == "9":
        return Numbers.nine

def combineDigitArrays(digitOneArray, digitTwoArray):
    print(digitOneArray, digitTwoArray)
    i = 0
    j = 0
    while i < len(digitOneArray):
        print(i % 4)
        ledArray.append(digitOneArray[i])
        if i % 4 == 3:
            print("divisible by 4")
            while j <= i:
                ledArray.append(digitTwoArray[j])
                j += 1
        i += 1
    print(ledArray)

combineDigitArrays(determineEnglishDigit(76, 0),determineEnglishDigit(76, 1))


