import os

a=input()

os.system("cat {}".format(a))
os.system("cat "+(a))

if(";" not in a or "||" not in a and a):
    os.system("cat %s"%a)
    print("random print for testing")
    b=10


os.system("ls")