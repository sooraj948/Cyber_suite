import ast
import sys
#https://pybit.es/articles/ast-intro/
# test_code=open("test.py","r").read()

# tree=ast.parse(test_code)
#print(ast.dump(tree))

# print(node.__getattribute__("execute"))
# print(type(node))
# print(ast.dump(ast.parse('123', mode='eval')))
# 
# print(ast.walk(node))
# for node in ast.walk(tree):
#     if node.__class__.__name__=="Call":

#         if (isinstance(node.func,ast.Attribute)): 
#             # print(node.func.attr)
#             if node.func.attr=="execute" and len(node.args)>0: #and isinstance(node.args[0],ast.Call) :
#                 # for i in node.args:
#                 #     print(i.lineno,i.__class__)
#                 print(node.lineno,node.args)
                # print((node.args[0].value))
        # print(node.func.value.id)
    # print(node.__class__)
# print()
# for node in ast.iter_child_nodes(tree):
#     print(node.__class__.__name__)
# print()
# for name, value in ast.iter_fields(tree):
#     print(name, value)


# class FuncLister(ast.NodeVisitor):
#     def visit_FunctionDef(self, node):
#         print(node.__class__)
#         self.generic_visit(node)

# a=FuncLister()
# a.visit(tree)



def create_ast(file):
    test_code=open(file,"r").read()

    tree=ast.parse(test_code)
    # print(ast.dump(tree))
    return tree
    
def find_vuln_nodes(tree,l):#also gives Names which are not sqli vuln

    for node in ast.walk(tree):
        if isinstance(node,ast.Call) and isinstance(node.func,ast.Attribute):
             
            if node.func.attr=="execute" or node.func.attr=="executemany":
                for i in node.args:
                    # print(i)
                    # if isinstance(i , ast.Call) or isinstance(i,ast.BinOp) or isinstance(i,ast.Name):

                    #     l.append(i)
                    if check(i,tree):
                        l.append(node)
                    
     

    return l


def find_func(func_name,tree):

    for node in ast.walk(tree):

        if isinstance(node,ast.FunctionDef) and node.name==func_name:

            return node



def check_name(node,tree,lineno):
    
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
                # print("Just testing",j.lineno,j.func.id)
            

    elif isinstance(i,ast.BinOp) and (isinstance(i.op,ast.Mod) or isinstance(i.op,ast.Add)):
        # print("right is ",i.right,i.lineno)
        if isinstance(i.right,ast.Name):
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

    

    
    return False
    
    

    


if __name__=="__main__":
    try:
        file=sys.argv[1]
        tree=create_ast(file)

        l=find_vuln_nodes(tree,[])

        for i in l:
            print(i.lineno,i)
        # rank="baseuser' or 1=1--"
        # a="SELECT username, rank FROM users WHERE rank = '{0}'".format(str(rank))
        # print(a)
    except IndexError:
        print("Usage: python3 sqli.py <filename>.py")
    








