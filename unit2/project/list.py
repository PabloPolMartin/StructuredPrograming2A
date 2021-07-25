import sys

tempF = [63, 73, -999, 91, 86, 82, 72, 81, 66, 77, 75, 104, -999, 84, 77, 66, 82, 63, 93, 72, 82, 64, 75 , 90, 64, -999, 99, 82, 95, 82]

tempC=[]

if __name__ == "__main__":
    print("Original list\n",tempF)
    l=tempF.count(-999)
    for i in range (0,l):
        tempF.remove(-999)
    print("Only Relevant Data:\n",tempF)
    
    for j in range (0,len(tempF)):
        tempC.append(round((tempF[j]-32)*(5/9)))
    print("Celsius Degrees:\n", tempC)

    print("\n Fahrenheit Maximum:", max(tempF))

    print("\n Celsius Maximum:", max(tempC))