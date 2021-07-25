import sys

add = 0
sub = 0
mult = 0
div = 0

n1=int(sys.argv[1])
n2=int(sys.argv[2])

if __name__ == "__main__":

    add = n1+n2
    sub = n1-n2
    mult = n1*n2
    div = n1/n2

    print(f"Addition:{add}")
    print(f"Subtraction:{sub}")
    print(f"Multiplication:{mult}")
    print(f"Division:{div}")