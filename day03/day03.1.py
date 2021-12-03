# Day 03.1 - Advent of Code
# Author: Will Howes
# Goal: Use the binary numbers in your diagnostic report to
#       calculate the gamma rate and epsilon rate, then multiply
#       them together. What is the power consumption of the submarine?
#       (Be sure to represent your answer in decimal, not binary.)

def giveInput():
    with open('puzzleinput03.txt', 'r') as file:
        return file.read().split()

def calcFreq(ls):
    binLen = len(ls[0])
    ct = [0 for x in range(binLen)]
    for b in ls:
        for i in range(binLen):
            if int(b[i]): ct[i]+=1
            else:         ct[i]-=1
    return ct

def findGEProduct(ls):
    freq = calcFreq(ls)
    g, e = '0b', '0b'
    for x in freq:
        if x > 0:
            g+='1'
            e+='0'
        else:
            g+='0'
            e+='1'
    return int(g, base=2)*int(e, base=2)

if __name__ == "__main__":
    ls = giveInput()
    print(findGEProduct(ls))
