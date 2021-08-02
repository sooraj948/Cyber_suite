import sys

def ceasar(s,n):
    t=""
    s=s.lower()
    for i in s:
        if 97<=ord(i)<=122:
            # print((ord(i)-97+n)%26)
            t+=chr((ord(i)-97+n)%26+97)# this is actual encryption by rotation or movement
        else:
            t+=i
    return t

def vignere(s,key):
    n=len(key)
    s=s.lower()
    t=""
    count=0
    for i in range(len(s)):
        if 97<=ord(s[i])<=122:
            t+=chr((ord(s[i])-97*2+ord(key[count%n]))%26+97)
            count+=1#keeps track of lower case letters . used above
        else:
            t+=s[i]#encrypt only letters not special chars

    return t

    

try:
    option=sys.argv[1]
    if option=="-s":#string input
        s=sys.argv[2]

        if s=="rot":
            t=ceasar(" ".join(sys.argv[4:]),int(sys.argv[3]))#.join is to take everything after the key as input not just the first one
            print(t)
        if s=="vignere":
            # print(sys.argv[3])
            t=vignere(" ".join(sys.argv[4:]),sys.argv[3])
            print(t)
            
    if option == "-f":#file input
        f=open(sys.argv[4],"r")
        a=f.read()
        s=sys.argv[2]
        if s=="rot":
            t=ceasar(a,int(sys.argv[3]))
            print(t)
        if s=="vignere":
            t=vignere(a,sys.argv[3])
            print(t)
    # print("Ignoring special characteers and numbers. Also giving in lowercase only")

        
except Exception as ex:
    print(ex)
