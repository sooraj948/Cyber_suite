import sys

def ceasar(s,n):
    t=""
    s=s.lower()#we are dealing only with lowercase letters for simplicity
    for i in s:
        if 97<=ord(i)<=122:
            # print((ord(i)-97+n)%26)
            t+=chr((ord(i)-97+n)%26+97)
        else:#if special characters then dont encode or decode
            t+=i
    return t

#etaoinshrdlcumwfgypbvkjxqz
def freq_dict(s):#creates a dictionary with letters as keys and frequency of occurence as values
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
def sorted_letters(s1):#sorts letters based on freq of occurence
    s1=s1.lower()
    d1=freq_dict(s1)
    keys = [i for i in d1]
    keys.sort(key=lambda x : d1[x])
    # print(keys)
    return keys

def create_mapping(s2):#maps to letters in english which occur most often to least often: etaoinshrdlcumwfgypbvkjxqz
    s2=s2.lower()
    keys=sorted_letters(s2)
    s="etaoinshrdlcumwfgypbvkjxqz"
    # print(len(s))
    d={}
    for i in range(len(keys)):
        d[keys[len(keys)-i-1]]=s[i]

    return d



    


def freq_analysis(s):#https://overthewire.org/wargames/krypton/krypton3.html
    s=s.lower()
    d=create_mapping(s)
    for i in s:
        if i in d:
            print(d[i],end="")
        else:
            print(i,end="")
    print("\nMapping used:\n\n",d)
    
    ans=input("Would you like to change the mapping(y/n): ")
    #the thing with frequency analysis is that it is not extremely accurate. There are are few variations.
    #but users can usually identify such discrepencies quite easily and correct them.
    #HINT: e and t are usually mapped properly. So h can be obtained from "the" if it was mapped wrong.

    #similarly familiar words with 1 or two letter(s) wrong can be easily identified and mapping can be corrected. The context of text if 
    #known may also be exploited. For example if the encoded text is about coronavirus and we come across something like dolonavilus we
    #correct it easily
    #in this way we eventually get the exact right mapping

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




def vignere(s,key):#https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
    #https://overthewire.org/wargames/krypton/krypton4.html

    n=len(key)
    s=s.lower()
    t=""
    count=0
    for i in range(len(s)):
        if 97<=ord(s[i])<=122:
            t+=chr((ord(s[i])-97*2+ord(key[count%n]))%26+97)#basically ceasar cipher but the key keeps changing
            count+=1
        else:
            t+=s[i]

    return t
        


    
#python3 decrypt.py -sk rot 12 asasasasasass
#python3 decrypt.py -s rot asasasasasass
try:
    option=sys.argv[1]#if -s for string or -f for file etc
    type=sys.argv[2]#which cipher decryption
    if option=="-sk":#string and key known

        if type=="rot":#ceasar or rotation

            t=ceasar(" ".join(sys.argv[4:]),26-int(sys.argv[3]))#26-key... for decryption of encrypted text with key
            print(t)
        elif type=="vignere":
            key_new=""
            key=sys.argv[3]#new key for decryption
            for i in key:
                key_new+=chr(26-ord(i)+97*2)#new key consists of 26-old letters of og key
            t=vignere(" ".join(sys.argv[4:]),key_new)#.join thing is so that we take everyting after key as 1 string 
            print(t)

        
    elif option=="-s":#string input without key known

        if type=="rot":
            for i in range(26):#try all 26 possible decryptions/brute force
                t=ceasar(" ".join(sys.argv[3:]),26-i)
                print("key is",i,":",t)

        elif type=="monoalph":#monoalphabetic subtitution of random letters. That is each letter is mapped to another unique random letter.
            #we are trying to decrypt it
            # print("in monoalphabetic substitution")
            freq_analysis(" ".join(sys.argv[3:]))
    
    elif option=="-sK" and type=="vignere" :#note K in caps. This is if only key length is known
        
        s=" ".join(sys.argv[4:])
        # print("File content:\n"+s+"\n**********************************************")
        
        key_len=int(sys.argv[3])
        
        # s_new=s.replace(" ","")
        s_new=""
        for i in s:
            if 97<=ord(i)<=122:
                s_new+=i
        
        # print(s_new)
        key=""#this will hold the string used to encode the og text
        for i in range(key_len):#we are trying to determine the key
            t=""
            for j in range(i,len(s_new),key_len):
                t+=s_new[j]
            # l.append(create_mapping(t))
            d=create_mapping(t)#use freq analysis of s[0]+s[key_len]+s[2*key_len]...and s[1]+s[1+key_len]+... and s[2]+s[2+key_len]+............
            # print(d)
            
            for i in d:
                if d[i]=="e":#in freq_analysis mapping to 'e' is usually correct as 'e' is by far the most used letter in english
                    # print(chr(abs(ord(i)-ord("e"))+97))
                    key+=chr(abs(ord(i)-ord("e"))+97)#add the letter to the key
                    break

        print("\nKey is most probaly:",key+"\n\n*************************************")
        key_new=""#same as before to decrypt
            
        for i in key:
            key_new+=chr(26-ord(i)+97*2)
        t=vignere(s,key_new)
        print(t)
        


        

    elif option=="-f":
        f=open(sys.argv[3],"r")
        s=f.read()#read contents from file and store as string
        print("File content:\n"+s+"\n**********************************************")
        f.close()
        #same as above from now
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


        

        


except Exception as ex:
    print(ex)



