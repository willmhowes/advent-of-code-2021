# Day 03.2 - Advent of Code
# Author: Will Howes
# Goal: Use the binary numbers in your diagnostic report to calculate
#       the oxygen generator rating and CO2 scrubber rating, then multiply
#       them together. What is the life support rating of the submarine?
#       (Be sure to represent your answer in decimal, not binary.)

def giveInput():
    with open('puzzleinput03.txt', 'r') as file:
        return file.read().split()

def mostCommon(x):
    if x >= 0: return '1'
    else:      return '0'

def leastCommon(x):
    if x < 0: return '1'
    else:     return '0'

def calcFreq(ls, com):
    binLen = len(ls[0])
    ct = [0 for x in range(binLen)]
    for b in ls:
        for i in range(binLen):
            if int(b[i]): ct[i]+=1
            else:         ct[i]-=1
    return list(map(com,ct))

def reduce(ls, i, freq, com):
    if i < len(freq) and len(ls) > 1:
        nls = [b for b in ls if b[i] == freq[i]]
        newFreq = calcFreq(nls, com)
        return reduce(nls, i+1, newFreq, com)
    else: return ls

def calcLifeSupport(ls):
    oxyFreq = calcFreq(ls, mostCommon)
    oxyBin = reduce(ls, 0, oxyFreq, mostCommon)
    oxyRating = int(oxyBin[0], base=2)

    cO2Freq = calcFreq(ls, leastCommon)
    cO2Bin = reduce(ls, 0, cO2Freq, leastCommon)
    cO2Rating = int(cO2Bin[0], base=2)

    return oxyRating*cO2Rating

if __name__ == "__main__":
    ls = giveInput()
    print(calcLifeSupport(ls))
