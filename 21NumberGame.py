def nearestMultiple(num):
    if num >= 4:
        near = num + (4 - (num % 4))
    else:
        near = 4
    return near

def lose1():
    print("\n\nYOU LOSE")
    exit(0)

def checkIsConsecutive(listNumbers):
    i = 1
    while i < len(listNumbers):
        if (listNumbers[i] - listNumbers[i - 1]) != 1:
            return False
        i = i + 1
    return True