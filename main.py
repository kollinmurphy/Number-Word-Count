import math

ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
hundred = "hundred"
bigger = ["thousand", "million", "billion", "trillion"]

def getName(num):
    names = [get_group_name(num % 1000)]
    temp = num
    while (temp > 999):
        temp = math.floor(temp / 1000)
        names.append(get_group_name(temp % 1000))
    i = len(names) - 1
    name = ""
    while i >= 0:
        if names[i] != "zero":
            name += " " + names[i]
            if i != 0:
                name += " " + bigger[i - 1]
        else:
            if len(names) == 1:
                name = "zero"
        i -= 1
    return name.strip(), count_letters(name)

def get_group_name(num):
    if num < 20:
        return ones[num]
    elif num < 100:
        digitTens = math.floor(num / 10) - 1
        digitOnes = num % 10
        if digitOnes != 0:
            name = tens[digitTens] + " " + ones[digitOnes]
        else:
            name = tens[digitTens] + " "
        return name.rstrip()
    elif num < 1000:
        digitHundreds = math.floor(num / 100)
        digitTens = math.floor((num % 100) / 10)
        digitOnes = num % 10
        name = ones[digitHundreds] + " " + hundred + " "
        if digitTens != 0:
            name += tens[digitTens - 1] + " "
        if digitOnes != 0:
            name += ones[digitOnes]
        return name.rstrip()

def count_letters(word):
    return len(word) - word.count(' ')

def chain(num, minToPrint):
    length = 0
    name, nameLength = getName(num)
    strToPrint = ""
    while name != "four":
        length += 1
        name, nameLength = getName(num)
        strToPrint += str(num) + " = " + name + " (" + str(nameLength) + " letters)\n"
        num = nameLength
    print(strToPrint + "\n")
    return length

def main():
    for i in range(1,500):
        if chain(i, 7) >= 7:
            break

def findWordsOfLetter():
    i = 3
    name, nameLength = getName(i)
    print(nameLength)
    print(name)

chain(323, 0)