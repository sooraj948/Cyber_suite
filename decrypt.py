import sys

def ceasar(s,n):
    t=""
    s.lower()
    for i in s:
        if 97<=ord(i)<=122:
            # print((ord(i)-97+n)%26)
            t+=chr((ord(i)-97+n)%26+97)
        else:
            t+=i
    return t

#etaoinshrdlcumwfgypbvkjxqz
def freq_dict(s):
    s.lower()
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

    d1=freq_dict(s1)
    keys = [i for i in d1]
    keys.sort(key=lambda x : d1[x])
    # print(keys)
    return keys

def create_mapping(s2):#sorted based on freq
    keys=sorted_letters(s2)
    s="etaoinshrdlcumwfgypbvkjxqz"
    print(len(s))
    d={}
    for i in range(len(keys)):
        d[keys[len(keys)-i-1]]=s[i]

    return d



    


def freq_analysis(s):
    d=create_mapping(s)
    for i in s:
        if i in d:
            print(d[i],end="")
        else:
            print(i)
    print("\nMapping used:\n",d)
        


    
# freq_analysis(sys.argv[3])



#python3 decrypt.py -sk rot 12 asasasasasass
#python3 decrypt.py -s rot asasasasasass
try:
    option=sys.argv[1]
    type=sys.argv[2]
    if option=="-sk":

        if type=="rot":

            t=ceasar(sys.argv[4],26-int(sys.argv[3]))
            print(t)
        
    elif option=="-s":

        if type=="rot":
            for i in range(26):
                t=ceasar(sys.argv[3],26-i)
                print("key is",i,":",t)

        elif type=="monoalph":
            # print("in monoalphabetic substitution")
            freq_analysis(sys.argv[3])


except Exception as ex:
    print(ex)



