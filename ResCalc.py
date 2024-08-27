#made by Lorbasta
#Standard used is IEC 60063:1963

resVal = [1, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2]
R1list = []
R2list = []

print("Enter input voltage:")
Vin = float(input())
print("Enter wanted output voltage:")
Vout = float(input())

def calcRes(Vin, Vout):
    R1 = 0
    bestDiff = 10000000000000
    for R2 in resVal:
        for i in range(7):
            #calc the ideal R1 for every standard resistor
            R1 = R2 * Vin
            R1 = R1 - Vout * R2
            R1 = R1 / Vout
            R1list.append(R1)
            R2list.append(R2)
            R2 = R2 * 10
    i = 0

    #find the closest standard resistor for every R1 
    #and choose the one with smallest difference
    for R1 in R1list:
        for standardRes in resVal:
            for g in range(7):
                lastDiff = R1 - standardRes
                lastDiff = abs(lastDiff)

                if(lastDiff <= bestDiff):
                    bestDiff = lastDiff
                    bestRes = standardRes
                    bestResnum = i
                standardRes = standardRes * 10
        i = i + 1
    i = 0
    print()
    print("Difference between ideal and closest resistor:")
    print(bestDiff)
    print("Closest R2:")
    print(R2list[bestResnum])
    return bestRes
print("Closest R1:")
print(calcRes(Vin, Vout))