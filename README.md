# Cyber_suite

# Motivation/Introduction

I got really interested in hacking and ctfs after the Zense team sent us a mail way back in 1st sem , talking about bandit(https://overthewire.org/wargames/) and ctfs in general. I tried to do them when I got some free time. They were hard ,to be honest, but in the process I noticed that there were similarities and mundane tasks, in challenges that could possibly be automated. So I thought I would build a suite of tools that would help in these hacking challenges like convertion from one form to another, encryption and decryption of basic ciphers and maybe try and detect vulnerabilities in code. Now I know that there are some amazing tools(mostly free!) which do these tasks super efficiently and there is no way that a 1st year cse student who has just started out with hacking and making large projects could match those projects. But I really enjoy these challenges and I thought building tools which might help in them, would be fun. And it was! 

The tools I was finally able to accomplish was not as vast I had imagined but I think they are decent:
1. Converter: Converts between hex,decimal,binary and ascii.
2. Encrypter: Given a file or string it encrypts the data using the specified cipher(Ceasar,vignere with specified keys)
3. Decryptor: Given an encrypted file and type of encryption(ceasar,vignere,monoalphabetic random substitution) it decrypts the data to the best possible extent.
4. Static Code Analysis: Given python files it outputs lines which might be vulnerable to sql injection and command line injection.

# Modules used
1. sys: For command line arguements
2. ast: Abstract Syntax Tree used for static code analysis
* No special installation of modules required

# Usage

## Converter

python3 converter.py conversion value_to_be_converted

Eg:
<code>
python3 converter.py hex-dec ff
<code>

conversion arguement is of the form datatype1-datatype2(asc,hex,dec,bin)

Eg: hex-asc, dec-bin, asc-bin. All 12 combination are allowed

Note: Hex values cannot have upper case letters. So A3 is not allowed. Instead use a3.


## Encrypter

python3 encrypt.py option cipher key data

Eg:
<code>
python3 encrypt.py -s rot 13 sooraj
<code>

option: -s or -f to input direct string or input file contaning text

cipher: rot(caesar) or vignere

key: For rot it has to be a number and for vignere it has to be a small word.
https://www.geeksforgeeks.org/vigenere-cipher/
https://en.wikipedia.org/wiki/Caesar_cipher


data : if -s then a string has to be given. If -f then name of file has to be given








test5.txt has encoded text of test2.txt using vignere cipher and key='gold'. 



