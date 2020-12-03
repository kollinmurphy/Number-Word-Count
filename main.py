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
    if length >= minToPrint:
        print(strToPrint)
    return length

def searchChains(length, start, end):
    for i in range(start, end + 1):
        chain(i, length)

def findNumbersOfGivenLength(length, start, end):
    for i in range(start, end + 1):
        name, nameLength = getName(i)
        if nameLength == length:
            print(str(i) + " = " + name + " (" + str(nameLength) + " letters)")

def main():
    print("Hello! Welcome to the Number Word Length program.")
    while True:
        print()
        print("1) Print all chains")
        print("2) Search for chains of a given length")
        print("3) Find numbers of a given length")
        print("4) Exit")
        choice = input("What would you like to do? ")

        if not choice.isdigit(): # validate input
            continue
        choice = eval(choice)

        if choice == 1:
            start, end = askForBounds()
            print()
            searchChains(0, start, end)
        elif choice == 2:
            start, end = askForBounds()
            while True:
                search = input("What minimum length of chain do you want to search for? ")
                if search.isdigit():
                    break
            print()
            searchChains(eval(search), start, end)
        elif choice == 3:
            start, end = askForBounds()
            while True:
                search = input("What word length do you want to search for? ")
                if search.isdigit():
                    break
            print()
            findNumbersOfGivenLength(eval(search), start, end)
        elif choice == 4:
            break

def askForBounds():
    while True:
        print()
        lower = input("What number do you want to start from? ")
        upper = input("What number do you want to end on? ")
        if lower.isdigit() and upper.isdigit():
            break
    return eval(lower), eval(upper)

main()
