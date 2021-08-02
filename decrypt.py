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
    # print(len(s))
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
    count=0
    for i in range(len(s)):
        if 97<=ord(s[i])<=122:
            t+=chr((ord(s[i])-97*2+ord(key[count%n]))%26+97)
            count+=1
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
        elif type=="vignere":
            key_new=""
            key=sys.argv[3]
            for i in key:
                key_new+=chr(26-ord(i)+97*2)
            t=vignere(sys.argv[4],key_new)
            print(t)

        
    elif option=="-s":

        if type=="rot":
            for i in range(26):
                t=ceasar(" ".join(sys.argv[3:]),26-i)
                print("key is",i,":",t)

        elif type=="monoalph":
            # print("in monoalphabetic substitution")
            freq_analysis(" ".join(sys.argv[3:]))
    
    elif option=="-sK" and type=="vignere" :#note K in caps
        
        s=" ".join(sys.argv[4:])
        # print("File content:\n"+s+"\n**********************************************")
        
        key_len=int(sys.argv[3])
        l=[]
        # s_new=s.replace(" ","")
        s_new=""
        for i in s:
            if 97<=ord(i)<=122:
                s_new+=i
        
        # print(s_new)
        key=""
        for i in range(key_len):
            t=""
            for j in range(i,len(s_new),key_len):
                t+=s_new[j]
            # l.append(create_mapping(t))
            d=create_mapping(t)
            # print(d)
            
            for i in d:
                if d[i]=="e":#in freq_analysis mapping to 'e' is usually correct as 'e' is by far the most used letter in english
                    # print(chr(abs(ord(i)-ord("e"))+97))
                    key+=chr(abs(ord(i)-ord("e"))+97)
                    break

        print("\nKey is most probaly:",key+"\n\n*************************************")
        key_new=""
            
        for i in key:
            key_new+=chr(26-ord(i)+97*2)
        t=vignere(s,key_new)
        print(t)
        


        

    elif option=="-f":
        f=open(sys.argv[3],"r")
        s=f.read()
        print("File content:\n"+s+"\n**********************************************")
        f.close()
        if type=="rot":
            for i in range(26):
                t=ceasar(s,26-i)
                print("key is",i,":\n",t)

        elif type=="monoalph":
            # print("in monoalphabetic substitution")
            freq_analysis(s)

    elif option=="-fk":
        f=open(sys.argv[4],"r")
        s=f.read()
        print("File content:\n"+s+"\n**********************************************")
        f.close()
        if type=="rot":
            t=ceasar(s,sys.argv[3])
            print(t)
        elif type=="vignere":
            key_new=""
            key=sys.argv[3]
            for i in key:
                key_new+=chr(26-ord(i)+97*2)
            t=vignere(s,key_new)
            print(t)

    elif option=="-fK" and type=="vignere" :
        f=open(sys.argv[4],"r")
        s=f.read()
        print("File content:\n"+s+"\n**********************************************")
        f.close()
        key_len=int(sys.argv[3])
        l=[]
        # s_new=s.replace(" ","")
        s_new=""
        for i in s:
            if 97<=ord(i)<=122:
                s_new+=i
        
        # print(s_new)
        key=""
        for i in range(key_len):
            t=""
            for j in range(i,len(s_new),key_len):
                t+=s_new[j]
            # l.append(create_mapping(t))
            d=create_mapping(t)
            # print(d)
            
            for i in d:
                if d[i]=="e":#in freq_analysis mapping to 'e' is usually correct as 'e' is by far the most used letter in english
                    # print(chr(abs(ord(i)-ord("e"))+97))
                    key+=chr(abs(ord(i)-ord("e"))+97)
                    break

        print("\nKey is most probaly:",key+"\n\n*************************************")
        key_new=""
            
        for i in key:
            key_new+=chr(26-ord(i)+97*2)
        t=vignere(s,key_new)
        print(t)


        # for i in l:
        #     print(i)

            

        


except Exception as ex:
    print(ex)



