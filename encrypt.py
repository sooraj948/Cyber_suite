import sys

def ceasar(s,n):
    t=""
    s=s.lower()
    for i in s:
        if 97<=ord(i)<=122:
            # print((ord(i)-97+n)%26)
            t+=chr((ord(i)-97+n)%26+97)
        else:
            t+=i
    return t

def vignere(s,key):
    n=len(key)
    s=s.lower()
    t=""
    for i in range(len(s)):
        if 97<=ord(s[i])<=122:
            t+=chr((ord(s[i])-97*2+ord(key[i%n]))%26+97)
        else:
            t+=s[i]

    return t

    

try:
    option=sys.argv[1]
    if option=="-s":
        s=sys.argv[2]

        if s=="rot":
            t=ceasar(sys.argv[4],int(sys.argv[3]))
            print(t)
        if s=="vignere":
            # print(sys.argv[3])
            t=vignere(sys.argv[4],sys.argv[3])
            print(t)
    if option == "-f":
        f=open(sys.argv[4],"r")
        a=f.read()
        s=sys.argv[2]
        if s=="rot":
            t=ceasar(a,int(sys.argv[3]))
            print(t)
        if s=="vignere":
            t=vignere(a,sys.argv[3])
            print(t)
    print("Ignoring special characteers and numbers. Also giving in lowercase only")

        
except Exception as ex:
    print(ex)
