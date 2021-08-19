import sqli
import cli
import sys

try:
    for i in range(1,len(sys.argv)):

        file=sys.argv[i]
        print("\n\nFile:",file)
        tree=sqli.create_ast(file)

        l=sqli.find_vuln_nodes(tree,[])#list of vulnerable lines
        print("Lines which might be sql injection vulnerable:")
        for i in l:
            print(i.lineno)
        

        print("****************\nLines which might be vulnerable to Command line injection")

        m=cli.find_vuln_nodes(tree,[])
        d=cli.check_if(tree,l)
        
        print("*Critical*. No input validation/sanitation done:")
        for i in m:
            if i not in d:
                print(i.lineno)
        print("*High*")
        for i in m:
            if i in d and d[i]==2:
                print(i.lineno)

        print("*Medium*")
        for i in m:
            if i in d and d[i]==1:
                print(i.lineno)

except Exception as ex:
    print(ex)
