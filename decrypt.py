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

#etaoinshrdlcumwfgypbvkjxqz
def freq_dict(s):
    s=s.lower()
    d={}
    for i in s:
        if ord(i) >122 or ord(i)<97:
            continue
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    # print(d)
    return d
def sorted_letters(s1):
    s1=s1.lower()
    d1=freq_dict(s1)
    keys = [i for i in d1]
    keys.sort(key=lambda x : d1[x])
    # print(keys)
    return keys

def create_mapping(s2):#sorted based on freq
    s2=s2.lower()
    keys=sorted_letters(s2)
    s="etaoinshrdlcumwfgypbvkjxqz"
    print(len(s))
    d={}
    for i in range(len(keys)):
        d[keys[len(keys)-i-1]]=s[i]

    return d



    


def freq_analysis(s):
    s=s.lower()
    d=create_mapping(s)
    for i in s:
        if i in d:
            print(d[i],end="")
        else:
            print(i,end="")
    print("\nMapping used:\n\n",d)
    
    ans=input("Would you like to change the mapping(y/n): ")
    while(ans=="y"):
        a=input("enter letter whose mapping u want to change: ")
        b=input("new mapping of previously mentioned letter: ")
        print("\n")
        
        for i in d:
            if d[i]==b:
                d[i]=d[a]
        d[a]=b
        # print("Original is:\n")
        # print(s+"\n")

        for i in s:
            if i in d:
                print(d[i],end="")
            else:
                print(i,end="")
        print("\nMapping used:\n\n",d)

        ans=input("Would you like to change the mapping(y/n): ")




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
        


    
# freq_analysis(sys.argv[3])


# print("".join(sys.argv[3:]))
#python3 decrypt.py -sk rot 12 asasasasasass
#python3 decrypt.py -s rot asasasasasass
try:
    option=sys.argv[1]
    type=sys.argv[2]
    if option=="-sk":

        if type=="rot":

            t=ceasar(sys.argv[4],26-int(sys.argv[3]))
            print(t)
        if type=="vignere":
            key_new=""
            key=sys.argv[3]
            for i in key:
                key_new+=chr(26-ord(i)+97*2)
            t=vignere(sys.argv[4],key_new)
            print(t)

        
    elif option=="-s":

        if type=="rot":
            for i in range(26):
                t=ceasar(sys.argv[3],26-i)
                print("key is",i,":",t)

        elif type=="monoalph":
            # print("in monoalphabetic substitution")
            freq_analysis(" ".join(sys.argv[3:]))

        

    elif option=="-f":
        f=open(sys.argv[3],"r")
        s=f.read()
        print("File content:\n"+s)
        f.close()
        if type=="rot":
            for i in range(26):
                t=ceasar(s,26-i)
                print("key is",i,":\n",t)

        elif type=="monoalph":
            # print("in monoalphabetic substitution")
            freq_analysis(s)



except Exception as ex:
    print(ex)



