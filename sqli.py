import ast
#https://pybit.es/articles/ast-intro/
test_code=open("test.py","r").read()

tree=ast.parse(test_code)
# print(node.__getattribute__("execute"))
# print(type(node))
# print(ast.dump(ast.parse('123', mode='eval')))
print(ast.dump(tree))
# print(ast.walk(node))
for node in ast.walk(tree):
    if node.__class__.__name__=="Call":

        if (isinstance(node.func,ast.Attribute)): 
            print(node.func.attr)
            if node.func.attr=="execute" and len(node.args)>0 and isinstance(node.args[0],ast.Call) :
                print((node.args[0].func.attr))
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