#similar to sqli.py

#Assumption: Here I am not considering the functions from subprocess module like run() and Popen.
#Reasons:
# 1. They are complex in that the command can be both a string or a list . Also many extra arguements/parameters can be given
# 2. Most places like tutorials for hacking challenges use the os.system(). the os module also seems perfectly functional to me.

import ast
import sys

def create_ast(file):
    test_code=open(file,"r").read()
   
    tree=ast.parse(test_code)
    # print(ast.dump(tree))
    return tree


def find_vuln_nodes(tree,l):

    for node in ast.walk(tree):

        if isinstance(node,ast.Call) and isinstance(node.func,ast.Attribute):
            if node.func.attr=="system":#os.system("<Cmd executed on shell>")
                # print("node.args:",node.args,node.lineno)
                for i in node.args:
                    if check(i,tree):

                        l.append(node)


    return l

def check(i,tree):
    if isinstance(i , ast.Call) and isinstance(i.func,ast.Attribute) and i.func.attr=="format" :
        # print(i)
        for j in i.args:
            #to avoid those where of the form .format(int()) or....bcz these are not sqli vuln. 
                #They will o/p error if we try to put " or # or --
            if isinstance(j,ast.Name):
                return True
            elif isinstance(j,ast.Call):
                if isinstance(j.func,ast.Name) and j.func.id=="str":   
                    return True
                
                if check(j,tree):
                    return True
                # print("Just testing",j.lineno,j.func.id)
            

    elif isinstance(i,ast.BinOp) and (isinstance(i.op,ast.Mod) or isinstance(i.op,ast.Add)):
        # print("right is ",i.right,i.lineno)
        if isinstance(i.right,ast.Name) :
            return True

        elif isinstance(i.right,ast.Tuple):
            for j in i.right.elts:

                if check(j,tree) or isinstance(j,ast.Name):
                    return True

        return check(i.right,tree)

    elif isinstance(i,ast.Name):
        res=check_name(i,tree,i.lineno)
        # print("res value is ",res.value)
        if check(res.value,tree):
            return True

    elif isinstance(i , ast.Call) and isinstance(i.func,ast.Name):

        node=find_func(i.func.id,tree)
        # print(node.body)
        ret_obj=node.body[-1]
        return check(ret_obj.value,tree)

    elif isinstance(i , ast.JoinedStr):
        # print(i.lineno,i)
        for j in i.values:
            if isinstance(j,ast.FormattedValue):

                if isinstance(j.value,ast.Name):
                    return True
                elif isinstance(j.value,ast.Call):
                    # print(j.lineno,j.value.func)
                    if check(j.value,tree):
                        return True
           
    
    return False

def check_if(tree,l):# this is a crude function to check if there has been some input sanitization or not
    d={}
    for node in ast.walk(tree):

        if isinstance(node,ast.If):
            possible={}#adds the operands to the dict
            # print(node.lineno,node.body)
            test=node.test
            if isinstance(test,ast.BoolOp):
                values=test.values
                for i in values:
                    if isinstance(i,ast.Compare):
                        for j in i.comparators:
                            if isinstance(j,ast.Name):
                                possible[j.id]=1
                        if isinstance(i.left,ast.Name):
                            possible[i.left.id]=1

                    
            elif isinstance(test,ast.Compare):
                for j in test.comparators:
                    if isinstance(j,ast.Name):
                        possible[j.id]=1
                if isinstance(test.left,ast.Name):
                    possible[test.left.id]=1
                


            # print(possible)
                

                # print(values)



            for i in node.body:#checks if the same operand is in query string and in if condition using the 'possible' dict
                # print("\t",i.lineno,i)
                if isinstance(i,ast.Expr) and isinstance(i.value,ast.Call) and isinstance(i.value.func,ast.Attribute):
                    # print("\t",i.lineno,i)
                    if i.value.func.attr=="system":
                        # print("\t",i.lineno,i)
                        d[i.value]=2#for High severity
                        temp=i.value.args[0]
                        if isinstance(temp , ast.Call) and isinstance(temp.func,ast.Attribute) and temp.func.attr=="format" :

                            for j in temp.args:
                                if isinstance(j,ast.Name) and j.id in possible:
                                    d[i.value]=1#medium Severity
                        elif isinstance(temp,ast.BinOp) and (isinstance(temp.op,ast.Mod) or isinstance(temp.op,ast.Add)):
                            if isinstance(temp.right,ast.Name) and temp.right.id in possible:
                                d[i.value]=1#medium severity

                        









                        


    return d

                    

if __name__=="__main__":
    tree=create_ast("test2.py")
    # print(ast.dump(tree))
    l=find_vuln_nodes(tree,[])
    d=check_if(tree,l)
    for i in l:
        if i in d:
            if d[i]==1:
                print("*Medium*",i.lineno,i)
            elif d[i]==2:
                print("*High*",i.lineno,i)

        else:
            print("*Critical*. No input validation/sanitation done:",i.lineno,i)
    
        


