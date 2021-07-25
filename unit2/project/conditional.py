import sys

list3 = []
list5 = []
x = 0

if __name__ == "__main__":
    print("The numbers are divisible by 3 and 5\n")
    for x in range (0,101):
       if x%3==0:
            list3.append(x)
    print("The numbers are divisible by 3: ",list3)

    for x in range (0,101):
       if x%5==0:
            list5.append(x)
    print("The numbers are divisible by 5: ", list5)   

