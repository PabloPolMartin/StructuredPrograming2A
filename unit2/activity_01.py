import sys
#global
num1 = 9

def isPrime( ):
    # def message(): ##Local
    #    print("It is function")
    global num1 
    num1 = 3
    def localfunction( ):
        print("This is a local function")
# localFunction() ##Local
# message() ## Local
# message( "This is a function..."  )
num_div = 1
count = 2 ##dos cuentas
if(num1 == 1):
    print("it is not a prime")
    exit()

while(count <= num1 ):

    if( num1 % count == 0 ):
        num_div += 1
        count +=1

if(num_div>2):


    return False
else:
    return True

def message(    ): ##Global
    print( "Global var")
    

def powTwoNumbers(  num1, num2  ):
    powNum1 = pow( num1, 2)
    powNum2 = po2( num2, 2)
    return ( powNum1, powNum2 )



if__name__=="__main__":
    print(  f'num1: {num1} ')

    print(  isPrime( )  )

    print(  f'num1: {num1} ')
    
    (x, y) _ powTwoNumbers(  2, 3 )
