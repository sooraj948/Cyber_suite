#this program converts from from one form to another. eg-hex to dec or ascii to bin
import sys


try:
    t=sys.argv[1]

    if t=="hex-dec":
        for i in range(2,len(sys.argv)):
            n=sys.argv[i]
            print(int(n,16),end=" ")
    elif t=="hex-asc":#https://www.knowprogram.com/python/convert-hex-string-to-ascii-string-python/
        for i in range(2,len(sys.argv)):
            n=sys.argv[i]
            bytes_array = bytes.fromhex(n)
            ascii_str = bytes_array.decode()
            print(ascii_str,end=" ")
    elif t=="hex-bin":
        for i in range(2,len(sys.argv)):
            n=sys.argv[i]
            print(bin(int(n,16))[2:],end=" ")

    elif t=="asc-bin":
        for i in range(2,len(sys.argv)):
            n=sys.argv[i]
            for j in n:
                print(bin(ord(j))[2:],end=" ")

    elif t=="asc-hex":
        for i in range(2,len(sys.argv)):
            n=sys.argv[i]
            for j in n:
                print(hex(ord(j))[2:],end="")

    elif t=="asc-dec":
        for i in range(2,len(sys.argv)):
            n=sys.argv[i]
            for j in n:
                print((ord(j)),end=" ")
            print("\n")


    elif t=="dec-bin":
        for i in range(2,len(sys.argv)):
            n=sys.argv[i]
            print(bin(int(n))[2:],end=" ")

    elif t=="dec-asc":
        for i in range(2,len(sys.argv)):
            n=sys.argv[i]
            print(chr(int(n)),end=" ")

    elif t=="dec-hex":
        for i in range(2,len(sys.argv)):
            n=sys.argv[i]
            print(hex(int(n)),end=" ")


    #https://www.simplifiedpython.net/python-binary-to-decimal/
    elif t=="bin-asc":
        
        for i in range(2,len(sys.argv)):
            n=sys.argv[i]
            print(chr(int(n,2)),end="")

    elif t=="bin-dec":
        
        for i in range(2,len(sys.argv)):
            n=sys.argv[i]
            print(int(n,2),end=" ")

    elif t=="bin-hex":
        
        for i in range(2,len(sys.argv)):
            n=sys.argv[i]
            print(hex(int(n,2)),end=" ")

    else:

        print("hex-dec means conversion from hexadecimal to decimal. asc-bin = ascii to binary conversion.\n all 12 combinations possible")

    
except Exception as ex:
    print("\n")
    # print("***"+str(ex)+"***")
    # print(type(ex))
    if type(ex)==ValueError:
        print("Please Enter correct values.Argument '"+sys.argv[i]+"' is incorrect for the required conversion")

    if type(ex)==IndexError:
        print("Eg: python3 converter.py hex-dec ff")
