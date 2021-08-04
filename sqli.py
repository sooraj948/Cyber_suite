import ast
#https://pybit.es/articles/ast-intro/
# test_code=open("test.py","r").read()

# tree=ast.parse(test_code)
# print(node.__getattribute__("execute"))
# print(type(node))
# print(ast.dump(ast.parse('123', mode='eval')))
# print(ast.dump(tree))
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
             
            if node.func.attr=="execute":
                for i in node.args:
                    # print(i)
                    # if isinstance(i , ast.Call) or isinstance(i,ast.BinOp) or isinstance(i,ast.Name):

                    #     l.append(i)
                    if isinstance(i , ast.Call) and isinstance(i.func,ast.Attribute) and i.func.attr=="format" :
                        # print(i.func)
                        l.append(node)

                    elif isinstance(i,ast.BinOp) and (isinstance(i.op,ast.Mod) or isinstance(i.op,ast.Add)):
                        l.append(node)

                    elif isinstance(i,ast.Name):
                        print("in finding vul nodes fn:",i,i.lineno)
                        print(check_new(i,tree,i.lineno))



                    



    return l

def check_assigns(tree):
    for node in ast.walk(tree):

        if isinstance(node,ast.Assign):
            print(node.lineno,node.value)
            # if isinstance(node.value,ast.Call) and isinstance(node.value.func,ast.Attribute) and node.value.func.attr=="format":
            #     print(node.lineno,node.value.func.attr)
            # elif isinstance(node.value,ast.BinOp):#+ and %
            #     print(node.lineno,node.value.op)

def check_new(node,tree,lineno):
    
    for some in ast.walk(tree):
        # if some.lineno==lineno:
        #     break
        if isinstance(some,ast.Assign):

            for i in some.targets:
                if i.id==node.id:
                    res=some

    print("res is ",res, res.lineno)
    


if __name__=="__main__":
    tree=create_ast("test.py")

    l=find_vuln_nodes(tree,[])
    # print("Vuln nodes:",l)
    # for i in l:
    #     print(i.lineno,i)

    # check_assigns(tree)

    # for i in l:
    #     if isinstance(i,ast.Name):
    #         print(i.id)









