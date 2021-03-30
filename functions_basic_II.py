#Countdown
def countdown(input):
    x = input
    for i in range(x, -1, -1):
        print(i)
countdown(5)

#Print and Return
def print_and_return(list):
    print(list[0])
    return list[1]
print(print_and_return([1, 2]))

#First Plus Length
def first_plus_length(a):
    sum = a[0] + int(len(a))
    return sum
print(first_plus_length([5,2,3,4,5]))

#Values Greater than Second - ????
def oldList(lis):
    newList = []
    count = 0
    if len(lis) < 2:
            return False
    else:
        for i in range(0, len(lis), 1):
            if lis[i]>=lis[2]:
                count +=1
                newList.append(lis[i])
    print(count)
    return newList

print(oldList([5,2,3,2,1,4]))

# #This Length, That Value
def length_and_value(a, b):
    newValue = []
    for i in range(1, a+1, 1):
        newValue.append(b)
    
    print(newValue)

print(length_and_value(6, 2))

