

n1 = int(input("Enter number: "))
n2 = int(input("Enter number: "))
n3 = int(input("Enter number: "))

if (n1 >= n2) and (n1 >= n3):
    val = n1
elif (n2 >= n1) and (n2 >= n3):
    val = n2
else:
    val = n3
print("Largest number: ", val)