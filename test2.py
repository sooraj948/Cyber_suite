import os
def genstr(rank="admin"):
    return "test.txt {}".format(rank)
    # return  "asdf"
a=input()

os.system("cat {}".format(a))
os.system("cat "+(a))
b="rand test"
if(";" not in a or "||" not in a and a or 1):
    if ("; " in a):
        os.system("cat %s"%a)
    elif(a):
        os.system("cat {}".format(a))
    print("random print for testing")
    b=10


os.system("ls %s"%a)
# a=""
# os.system("cat {}".format(a))
# os.system("ls %s"%a)

