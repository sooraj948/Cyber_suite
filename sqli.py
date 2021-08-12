import ast
import sys
#https://pybit.es/articles/ast-intro/
# test_code=open("test.py","r").read()

# tree=ast.parse(test_code)
#print(ast.dump(tree))

#in code here i am assuming the only reason to pass a variable to a formatted or f-string is if it is being taken as
#input and hence it might be sql injection vulnerable.
#eg: c.execute("select .... where user={}".format(user))
#in this eg i am assuming 'user' is being input from somewhere(web or cmd line or anything) and not checking for it.
#bcz if 'user' is known what is the point of using a variable and using formatting?


def create_ast(file):#creates the abstract syntax tree of a python prog
    test_code=open(file,"r").read()

    tree=ast.parse(test_code)
    # print(ast.dump(tree))
    return tree
    
def find_vuln_nodes(tree,l):#finds the lines which are prolly sql injection vulnerabe

    for node in ast.walk(tree):#goes thru the whole ast
        if isinstance(node,ast.Call) and isinstance(node.func,ast.Attribute):
             
            if node.func.attr=="execute" or node.func.attr=="executemany":#checks if it is function cal is execute or executemany
                for i in node.args:
                    # print(i)
                    # if isinstance(i , ast.Call) or isinstance(i,ast.BinOp) or isinstance(i,ast.Name):

                    #     l.append(i)
                    if check(i,tree):#does a more checking
                        l.append(node)
                    
     

    return l


def find_func(func_name,tree):#finds function node with same function name as in parameters

    for node in ast.walk(tree):

        if isinstance(node,ast.FunctionDef) and node.name==func_name:

            return node



def check_name(node,tree,lineno):#checks for most recent assignment with that name/variable
    
    for some in ast.walk(tree):
        # if some.lineno==lineno:
        #     break
        if isinstance(some,ast.Assign) and some.lineno< lineno:# for most recent assignment of that value

            for i in some.targets:
                if i.id==node.id:
                    res=some

    # print("res is ",res, res.lineno)
    return res

def check(i,tree):
    # print(i.lineno,i)
    if isinstance(i , ast.Call) and isinstance(i.func,ast.Attribute) and i.func.attr=="format" :#this is for the str.format
        # print(i)
        for j in i.args:
            #to avoid those where of the form .format(int()) or....bcz these are not sqli vuln. 
                #They will o/p error if we try to put " or # or --
            if isinstance(j,ast.Name):#returns True if any 1 of the parameters is a variable. Check assumption above
                return True
            elif isinstance(j,ast.Call):#if parameter is another function call
                if isinstance(j.func,ast.Name) and j.func.id=="str":   #if str then sqli
                    return True
                
                if check(j,tree):#recursively check/do it again
                    return True
                # print("Just testing",j.lineno,j.func.id)
            

    elif isinstance(i,ast.BinOp) and (isinstance(i.op,ast.Mod) or isinstance(i.op,ast.Add)):#for + and % Eg: print("Name %s"%a)
        # print("right is ",i.right,i.lineno)
        if isinstance(i.right,ast.Name) :
            return True

        elif isinstance(i.right,ast.Tuple):#multiple parameters
            for j in i.right.elts:

                if check(j,tree) or isinstance(j,ast.Name):
                    return True

        return check(i.right,tree)

    elif isinstance(i,ast.Name):#if query string is in a variable 
        res=check_name(i,tree,i.lineno)
        # print("res value is ",res.value)
        if check(res.value,tree):#recursively check that string
            return True

    elif isinstance(i , ast.Call) and isinstance(i.func,ast.Name):#user defined fuction is the parameter

        node=find_func(i.func.id,tree)
        # print(node.body)
        ret_obj=node.body[-1]#whatever is returned by that function
        return check(ret_obj.value,tree)#check return object

    elif isinstance(i , ast.JoinedStr):#f string . Eg: f"my name is {name}"
        # print(i.lineno,i)
        for j in i.values:
            if isinstance(j,ast.FormattedValue):#if it is {}

                if isinstance(j.value,ast.Name):
                    return True
                elif isinstance(j.value,ast.Call):
                    # print(j.lineno,j.value.func)
                    if check(j.value,tree):
                        return True
                     

    

    
    return False
    
    

    


if __name__=="__main__":
    try:
        file=sys.argv[1]
        tree=create_ast(file)

        l=find_vuln_nodes(tree,[])#list of vulnerable lines

        for i in l:
            print(i.lineno,i)
        # rank="baseuser' or 1=1--"
        # a="SELECT username, rank FROM users WHERE rank = '{0}'".format(str(rank))
        # print(a)
    except IndexError:
        print("Usage: python3 sqli.py <filename>.py")
    








