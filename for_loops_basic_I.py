#Basic
for i in range(0, 151, 1):
    print(i)

#Multiples of Five
for i in range(5, 1000, 1):

    if i%5 == 0:
        print(i)

#Counting, the Dojo Way
for i in range(1, 100, 1):
    if i%5 == 0:
        print(str(i) + " Coding")
    if i%10 == 0:
        print(str(i) + " Coding Dojo")

#Whoa. That Sucker's Huge
sum = 0
for i in range(0, 500000, 1):
    if i%2 == 1:
        sum = sum + i
print(sum)

#Countdown by Fours
for i in range(2018, 0, -4):
    print(i)

#Flexible Counter
def flexCounter(lowNum, highNum, mult):
    for i in range(lowNum, highNum+1, 1):
        if i%mult == 0:
            print(i)
flexCounter(2, 20, 10)